# Answer routes goes here
from flask_restx import Resource, abort
from ..schemas import (
    answer_model,
    answer_namespace,
    answer_question_options,
    correctANSWER_model,
    enum,
    update_answer_model
)
from http import HTTPStatus
from ..extensions import db
from ..models import Answer, Is_answered, Question, Users, admin_required
from sqlalchemy import and_
from flask_jwt_extended import jwt_required, get_jwt_identity


@answer_namespace.route("/answer")
class InputAnswer(Resource):
    @jwt_required()
    @answer_namespace.expect(answer_model)
    @answer_namespace.marshal_with(answer_question_options)
    @admin_required
    def post(self):
        data = answer_namespace.payload
        answer = Answer.query.filter_by(question_id=data["question_id"]).first()
        question = Question.query.get(data["question_id"])
        if not question:
            abort(400, message="No question has been posted for this id")
        if answer:
            abort(400, message="You posted an answer already for this question")
        answer_ = Answer(answer=data["answer"].upper(), question_id=data["question_id"])
        db.session.add(answer_)
        db.session.commit()
        return answer_, HTTPStatus.CREATED


@answer_namespace.route("/answer/<int:answer_id>")
class EachAnswer(Resource):
    @jwt_required()
    @answer_namespace.expect(update_answer_model)
    @answer_namespace.marshal_with(update_answer_model)
    @admin_required
    def patch(self, answer_id):
        data = answer_namespace.payload
        answer_ = Answer.query.filter_by(id=answer_id).first()
        if data["answer"]:
            answer_.answer = data["answer"].upper()

        db.session.commit()
        return answer_
        

@answer_namespace.route("/question/answer")
class chooseAnswer(Resource):
    @jwt_required()
    @answer_namespace.expect(correctANSWER_model)
    def post(self):
        user_id = get_jwt_identity()
        data = answer_namespace.payload
        if not Question.query.get(data["question_id"]):
            abort(404, message="No question with this id")
        if data["answer"].upper() not in enum:
            abort(400, message="Not a valid option")
        user = Users.query.get(user_id)
        if user.taken:
            abort(400, message="You took the quiz already")
        if Is_answered.query.filter(
            and_(Is_answered.user_id == user_id,
                 Is_answered.question_id == data["question_id"])
        ).first():
            abort(400, message="you have already answered this question")
        else:

            question = Question.query.filter(Question.id == data["question_id"]).first()
            for quest in question.answer:

                if data["answer"].upper() == quest.answer.name:
                    answered = Is_answered(user_id=user_id,
                                           question_id=data["question_id"])
                    db.session.add(answered)
                    db.session.commit()
                    
                    user.scores += 10
                    db.session.commit() 
                    return {"message": "answer is correct"}
                else:
                    answered = Is_answered(user_id=user_id,
                                           question_id=data["question_id"])
                    db.session.add(answered)
                    db.session.commit()
                    return {"message": "answer is incorrect"}, HTTPStatus.CREATED


@answer_namespace.route("/submit")
class SubmitQuiz(Resource):
    @jwt_required()
    def patch(self):
        user = Users.get_by_id(get_jwt_identity())
        question = Question.query.all()

        if not question:
            abort(400, message="No question yet")
        # if the user has already submitted
        # abort the operation
        if user.taken:
            abort(400, message="You submitted already")
        # if not, then updated the taken column of the current user
        user.taken = 1
        db.session.commit()
        return {"message": "Quiz submitted successfully",
                "scores": f"{user.scores}/{len(question) * 10}"
                }, HTTPStatus.OK
