from flask_restx import Namespace, fields
from .answer import answer_model
from .option import option_model

question_namespace = Namespace("question", description="question endpoint")

question_model = question_namespace.model(
    "Question", {
        "id": fields.Integer(dump_only=True),
        "question": fields.Integer(required=True, description="the question")
    }
)

question_with_option_model = question_namespace.model(
    "Question_answer", {
        "id": fields.Integer(dump_only=True),
        "question": fields.String(required=True, description="the question"),
        "answer": fields.Nested(answer_model, description="question answer"),
        "option": fields.Nested(option_model, description="question options")
    }
)
