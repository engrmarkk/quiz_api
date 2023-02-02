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
