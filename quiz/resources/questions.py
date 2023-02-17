from flask_restx import Resource
from ..schemas import (
    question_model, question_namespace,
    question_with_option_model
                       )
from ..models import Question, admin_required
from http import HTTPStatus
from ..extensions import db
from flask_jwt_extended import jwt_required


@question_namespace.route("/question")
class addAndGetQuestions(Resource):
    @jwt_required()
    @question_namespace.expect(question_model)
    @question_namespace.marshal_with(question_model)
    @admin_required
    def post(self):
        data = question_namespace.payload

        question = Question(question=data["question"].lower())
        question.save()
        return question, HTTPStatus.CREATED

    @jwt_required()
    @question_namespace.marshal_with(question_with_option_model)
    def get(self):
        questions = Question.query.all()
        return questions, HTTPStatus.OK


@question_namespace.route("/question/<int:question_id>")
class eachQuestions(Resource):
    @jwt_required()
    @question_namespace.marshal_with(question_with_option_model)
    def get(self, question_id):
        question = Question.get_by_id(question_id)
        return question, HTTPStatus.OK

    @jwt_required()
    @question_namespace.expect(question_model)
    @question_namespace.marshal_with(question_model)
    @admin_required
    def patch(self, question_id):
        question_to_update = Question.get_by_id(question_id)
        data = question_namespace.payload

        question_to_update.question = data["question"].lower()
        db.session.commit()
        return question_to_update

    @jwt_required()
    @admin_required
    def delete(self, question_id):
        question_to_delete = Question.get_by_id(question_id)
        db.session.delete(question_to_delete)
        db.session.commit()
        return {"message": "Question deleted"}
