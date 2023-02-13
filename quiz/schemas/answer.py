from flask_restx import Namespace, fields

answer_namespace = Namespace("answer", description="answer endpoint")

enum = ["A", "B", "C", "D", "E", ]

answer_model = answer_namespace.model(
    "Answer", {
        "id": fields.Integer(dump_only=True),
        "answer": fields.String(required=True,
                                description="the answer to a question",
                                enum=enum
                                ),
        "question_id": fields.Integer(required=True, load_only=True, description="the question's id")
    }
)

# this import has to stay here so as not to encounter circular import error
from .question import question_with_option

answer_question_options = answer_namespace.model(
    "Answer with Q&Opt", {
        "id": fields.Integer(dump_only=True),
        "answer": fields.String(required=True,
                                description="the answer to a question",
                                enum=enum
                                ),
        "question_id": fields.Integer(required=True, load_only=True, description="the question's id"),
        "q_to_ans": fields.Nested(question_with_option, description="question and option for the answer")
    }
)
correctANSWER_model = answer_namespace.model(
    "CorrectAnswer", {
        "id": fields.Integer(dump_only=True),
        "question_id": fields.Integer(required=True, load_only=True, description="the question's id"),
        "answer": fields.String(required=True,
                                description="the  correct answer to a question",
                                enum=enum
                                )})
