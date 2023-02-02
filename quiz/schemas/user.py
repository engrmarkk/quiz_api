from flask_restx import fields, Namespace

user_namespace = Namespace('user', description="user endpoint")
register = user_namespace.model("register", {
    "id": fields.Integer(dump_only=True),
    'email': fields.String(required=True, description="An email"),
    'password': fields.String(required=True, description="A password"),
    "first_name": fields.String(required=True, description="user's firstname"),
    "last_name": fields.String(required=True, description="user's lastname"),
    "username": fields.String(required=True, description="user's username")
})
login_model = user_namespace.model(
    'Login', {
        'username': fields.String(required=True, description="username"),
        'password': fields.String(required=True, description="A password")
    }
)

get_user_model = user_namespace.model(
    "Get User", {
        "id": fields.Integer(dump_only=True),
        'email': fields.String(required=True, description="An email"),
        "first_name": fields.String(required=True, description="user's firstname"),
        "last_name": fields.String(required=True, description="user's lastname"),
        "username": fields.String(required=True, description="user's username"),
        "scores": fields.Integer(required=True, description="user's scores"),
        "is_admin": fields.Boolean(required=True, description="user's admin status"),
        "taken": fields.Boolean(required=True, description="has user taken the quiz"),
    }
)
