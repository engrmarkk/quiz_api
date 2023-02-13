# Answer routes goes here
from flask_restx import Resource,abort
from ..schemas import answer_model,answer_namespace,answer_question_options,correctANSWER_model
from ..extensions import db
from ..models import Answer,Is_answered,Question,Users
from sqlalchemy import and_
from flask_jwt_extended import jwt_required,get_jwt_identity

@answer_namespace.route("/answer")
class InputAnswer(Resource):
    @answer_namespace.expect(answer_model)
    @answer_namespace.marshal_with(answer_question_options)
    def post(self):
        data= answer_namespace.payload
        answer_=Answer(answer=data["answer"],
        question_id=data["question_id"])
        db.session.add(answer_)
        db.session.commit()
        return answer_
@answer_namespace.route("/answer/<int:question_id>")
class chooseAnswer(Resource):
    @jwt_required()
    @answer_namespace.expect(correctANSWER_model)
    def post(self,question_id):
        user_id=get_jwt_identity()
        user=Users.query.get(user_id)
        if Is_answered.query.filter(and_(Is_answered.user_id==user_id,Is_answered.question_id==question_id)).first():
            abort(400,message="you have already answered this question")
        else:
            data=answer_namespace.payload
    
            question=Question.query.filter(Question.id==question_id).first()
            for quest in question.answer:

                if data["answer"].upper()==quest.answer.name:
                    answered=Is_answered(user_id=user_id,question_id=question_id)
                    db.session.add(answered)
                    db.session.commit()
                     
                    user.scores+=10
                    db.session.commit() 
                    return {"message":"answer is correct"}
                else:
                    answered=Is_answered(user_id=user_id,question_id=question_id)
                    db.session.add(answered)
                    db.session.commit()
                    return {"message":"answer is incorrect"}
