from .extensions import db, migrate, jwt, app
from .config import config_object
from .models import Question, Options, Answer, Users


# This is the function that creates the app
def create_app(configure=config_object["appcon"]):
    # This line of code configures the application using the configuration object specified.
    # The configuration object contains settings that will be used by the application.
    app.config.from_object(configure)

    # This line of code initializes the extensions imported above
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

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
                "Users": Users
                }

    return app