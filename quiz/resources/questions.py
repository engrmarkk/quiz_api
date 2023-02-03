from flask_restx import Resource
from ..schemas import (
    question_model, question_namespace,
    question_with_option_model
                       )
from ..models import Question
from http import HTTPStatus
from ..extensions import db


@question_namespace.route("/question")
class addAndGetQuestions(Resource):
    @question_namespace.expect(question_model)
    @question_namespace.marshal_with(question_model)
    def post(self):
        data = question_namespace.payload

        question = Question(question=data["question"].lower())
        question.save()
        return question, HTTPStatus.CREATED

    @question_namespace.marshal_list_with(question_with_option_model)
    def get(self):
        questions = Question.query.all()
        return questions, HTTPStatus.OK


@question_namespace.route("/question/<int:question_id>")
class eachQuestions(Resource):
    @question_namespace.marshal_with(question_with_option_model)
    def get(self, question_id):
        question = Question.get_by_id(question_id)
        return question, HTTPStatus.OK
    
    @question_namespace.expect(question_model)
    @question_namespace.marshal_with(question_model)
    def patch(self, question_id):
        question_to_update = Question.get_by_id(question_id)
        data = question_namespace.payload

        question_to_update.question = data["question"].lower()
        db.session.commit()
        return question_to_update

    def delete(self, question_id):
        question_to_delete = Question.get_by_id(question_id)
        db.session.delete(question_to_delete)
        db.session.commit()
        return {"message": "Question deleted"}
