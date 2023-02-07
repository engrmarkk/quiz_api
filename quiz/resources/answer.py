# Answer routes goes here
from flask_restx import Resource
from ..schemas import answer_model,answer_namespace,answer_question_options
from ..extensions import db
from ..models import Answer

@answer_namespace.route("/answer")
class Answer(Resource):
    @answer_namespace.expect(answer_model)
    @answer_namespace.marshal_with(answer_question_options)
    def post(self):
        data= answer_namespace.payload
        answer_=Answer(answer=data["answer"],
        question_id=data["question_id"])
        db.session.add(answer_)
        db.session.commit()
        return answer_