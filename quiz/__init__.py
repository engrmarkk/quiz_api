from .extensions import db, migrate, jwt, app, api
from .config import config_object
from .models import Question, Options, Answer, Users, Is_answered
from .auth import user_namespace
from .resources import *
from datetime import timedelta


# This is the function that creates the app
def create_app(configure=config_object["appcon"]):
    # This line of code configures the application using the configuration object specified.
    # The configuration object contains settings that will be used by the application.
    app.config.from_object(configure)

    # This line of code initializes the extensions imported above
    db.init_app(app)
    migrate.init_app(app, db)

    app.config["JWT_SECRET_KEY"] = "overstuffed"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

    jwt.init_app(app)
    api.init_app(app)

    api.add_namespace(user_namespace, path="/user")
    api.add_namespace(question_namespace)
    api.add_namespace(option_namespace)
    api.add_namespace(answer_namespace)
    # api.add_namespace(answer_namespace)

    # This line of code imports the routes from the routes package
    @app.shell_context_processor
    # This function returns the database, Question, Options, and Answer models
    def make_shell_context():
        # This returns the database, Question, Options, and Answer models
        return {
                "db": db,
                "Question": Question,
                "Options": Options,
                "Answer": Answer,
                "Users": Users,
                "Is_answered": Is_answered
                }

    return app
