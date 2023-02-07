from flask_restx import Namespace, fields

question_namespace = Namespace("question", description="question endpoint")

question_model = question_namespace.model(
    "Question", {
        "id": fields.Integer(dump_only=True),
        "question": fields.String(required=True, description="the question")
    }
)

# This import has to remain here to avoid circular import error,
# and that is because I imported the question_model schema in the option.py file
# and I needed to import the option_model from the option.py file
from .option import option_model

question_with_option = question_namespace.model(
    "Question_answer", {
        "id": fields.Integer(dump_only=True),
        "question": fields.String(required=True, description="the question"),
        "option": fields.Nested(option_model, description="question options")
    }
)


# This import has to remain here too, to avoid circular import error
from .answer import answer_model

question_with_option_model = question_namespace.model(
    "Question_answer", {
        "id": fields.Integer(dump_only=True),
        "question": fields.String(required=True, description="the question"),
        "answer": fields.Nested(answer_model, description="question answer"),
        "option": fields.Nested(option_model, description="question options")
    }
)
