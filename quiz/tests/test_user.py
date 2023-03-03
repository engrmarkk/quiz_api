import unittest
from ..extensions import db
from ..config import config_object
from .. import create_app
from ..models import Users


"""
 1. Create an instance of the test client by passing in the configuration for the test configuration.
 2. Push the application context so that all the database operations take place within the context of the application.
 3. Create all the tables needed for this test.
 4. Execute any additional setup steps needed.
"""


# class to test the user model
class UserTestCase(unittest.TestCase):

    # set up the test environment
    # create a test client
    def setUp(self):
        # create a test client
        # create a test database
        self.app = create_app(configure=config_object['testcon'])

        self.appctx = self.app.app_context()
        # push the app context
        self.appctx.push()

        self.client = self.app.test_client()
        # create all the tables
        db.create_all()

    """
    1. tearDown() is a method to clean up resources used by the unit test. 
    2. db.drop_all() drops all tables from the db.
    3. self.appctx.pop() removes the app context from the stack of contexts.
    4. self.app is set to None, indicating it has been destroyed. 
    5. self.client is also set to None, indicating that the client to the app has been disconnected.
    """
    # clean up after the test
    # drop all the tables
    # remove the app context
    # remove the test client
    # remove the test database
    # remove the app
    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app = None

        self.client = None

    """
    1. The first line is making a call to the API endpoint with the request data as a JSON object.
    2. The second line is querying the Users table to see if the user with the provided first name exists.
    3. The third line is making an assertion that the user's username should be the same as the one given in the request.
    4. The fourth line is making an assertion that the user's first name should be the same as the one given in the request.
    5. The fifth line is making an assertion that the API should return a status code of 201 (Created) when the request is successful.
    """
    # test the user registration
    def test_user_register(self):
        # create a user
        data = {"first_name": "gabu",
                "last_name": "depay",
                "username": "gabuuu",
                "password": "counter",
                "email": "debryne123@gmail.com"}
        # make a post request to the user register endpoint
        # send the data as a json object
        signup_response = self.client.post('/user/register', json=data)
        # check if the user has been created
        # if yes, check if the user's username is the same as the one given in the request
        user = Users.query.filter_by(first_name=data["first_name"]).first()
        # check if the user's username is the same as the one given in the request
        # check if the user's first name is the same as the one given in the request
        assert user.username == "gabuuu"
        assert user.first_name == "gabu"
        # check if the response status code is 201
        # 201 means the user has been created
        assert signup_response.status_code == 201
        