import unittest
from ..extensions import db
from ..config import config_object
from .. import create_app
from ..models import Users


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(configure=config_object['testcon'])

        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()

    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None

    def test_user_register(self):
        data = {"first_name": "gabu",
                "last_name": "depay",
                "username": "gabuuu",
                "password": "counter",
                "email": "debryne123@gmail.com"}

        signup_response = self.client.post('/user/register', json=data)
        user = Users.query.filter_by(first_name=data["first_name"]).first()
        assert user.username == "gabuuu"
        assert user.first_name == "gabu"
        assert signup_response.status_code == 201
        

