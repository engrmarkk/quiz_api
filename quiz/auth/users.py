from flask_restx import Resource, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, \
    jwt_required, get_jwt_identity
from ..schemas import user_namespace, login_model, register, get_user_model
from ..models import Users, admin_required
from sqlalchemy import or_
from ..extensions import db
from http import HTTPStatus
from datetime import timedelta


@user_namespace.route("/register")
class UserRegister(Resource):
    @user_namespace.expect(register)
    @user_namespace.marshal_with(register)
    def post(self):
        data = user_namespace.payload
        if Users.query.filter(
            or_(Users.username == data["username"].lower(), Users.email == data["email"].lower())
        ).first():
            abort(400, message="this username/email is already in the database")

        if len(Users.query.all()) == 0:
            is_admin = 1
        else:
            is_admin = 0
        new_user = Users(
            first_name=data["first_name"].lower(),
            last_name=data["last_name"].lower(),
            username=data["username"].lower(),
            email=data["email"].lower(),
            password=generate_password_hash(data["password"]),
            is_admin=is_admin
        )
        new_user.save()
        return new_user, HTTPStatus.CREATED
        # return {"message":"user has been registered, you can login in now"}


@user_namespace.route("/login")
class login(Resource):
    @user_namespace.expect(login_model)
    def post(self):
        data = user_namespace.payload
        user = Users.query.filter(Users.username == data["username"].lower()).first()
        if user and check_password_hash(user.password, data["password"]):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        abort(400, message="incorrect username/password")


@user_namespace.route("/users")
class getAllUsers(Resource):
    @jwt_required()
    @user_namespace.marshal_list_with(get_user_model)
    @admin_required
    def get(self):
        users = Users.query.all()
        return users, HTTPStatus.OK


@user_namespace.route("/user/<int:user_id>")
class getEachUser(Resource):
    @jwt_required()
    @user_namespace.marshal_with(get_user_model)
    def get(self, user_id):
        user = Users.get_by_id(user_id)
        return user, HTTPStatus.OK

    @jwt_required()
    def delete(self, user_id):
        user = Users.get_by_id(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}

    @jwt_required()
    def patch(self, user_id):
        user = Users.get_by_id(user_id)
        if user.is_admin:
            user.is_admin = 0
            db.session.commit()
            return {"message": "User has been demoted from being an admin"}
        user.is_admin = 1
        db.session.commit()
        return {"message": "User has been promoted to be an admin"}


@user_namespace.route("/refresh")
class RefreshToken(Resource):

    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(
            identity=current_user, fresh=False, expires_delta=timedelta(days=5)
        )

        return {"access_token": new_token}
