from flask_restx import Namespace, fields
from .question import question_model

option_namespace = Namespace("option", description="option endpoint")

option_model = option_namespace.model(
    "Option", {
        "id": fields.Integer(dump_only=True),
        "a": fields.String(required=True, description="option A"),
        "b": fields.String(required=True, description="option B"),
        "c": fields.String(required=True, description="option C"),
        "d": fields.String(required=True, description="option D"),
        "e": fields.String(required=True, description="option E"),
        "question_id": fields.Integer(required=True, load_only=True, description="the question's id")
    }
)

option_with_question = option_namespace.model(
    "Option Q&A", {
        "id": fields.Integer(dump_only=True),
        "a": fields.String(required=True, description="option A"),
        "b": fields.String(required=True, description="option B"),
        "c": fields.String(required=True, description="option C"),
        "d": fields.String(required=True, description="option D"),
        "e": fields.String(required=True, description="option E"),
        "question_id": fields.Integer(required=True, load_only=True, description="the question's id"),
        "question": fields.Nested(question_model, description="the question for that options")
    }
)
