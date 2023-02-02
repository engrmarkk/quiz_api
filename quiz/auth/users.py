from flask_restx import Resource, abort

from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from ..schemas import user_namespace, login_model, register, get_user_model
from ..models import Users
from sqlalchemy import or_
from ..extensions import db
from http import HTTPStatus


@user_namespace.route("/register")
class UserRegister(Resource):
    @user_namespace.expect(register)
    @user_namespace.marshal_with(register)
    def post(self):
        data = user_namespace.payload
        if Users.query.filter(
            or_(Users.username == data["username"], Users.email == data["email"])
        ).first():
            abort(400, message="this username/email is already in the database")

        new_user = Users(
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=data["username"],
            email=data["email"],
            password=generate_password_hash(data["password"]),
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
        # return {"message":"user has been registered, you can login in now"}


@user_namespace.route("/login")
class login(Resource):
    @user_namespace.expect(login_model)
    def post(self):
        data = user_namespace.payload
        user = Users.query.filter(Users.username == data["username"]).first()
        if user and check_password_hash(user.password, data["password"]):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        abort(400, message="incorrect username/password")


@user_namespace.route("/users")
class getAllUsers(Resource):
    @user_namespace.marshal_list_with(get_user_model)
    def get(self):
        return Users.query.all(), HTTPStatus.OK
