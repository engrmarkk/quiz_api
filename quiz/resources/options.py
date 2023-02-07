from flask_restx import Resource
from ..schemas import option_model, option_namespace, option_with_question
from ..models import Options
from http import HTTPStatus
from ..extensions import db


@option_namespace.route("/option")
class addAndGetQuestions(Resource):
    @option_namespace.expect(option_model)
    @option_namespace.marshal_with(option_with_question)
    def post(self):
        data = option_namespace.payload

        option = Options(
            a=data["a"].lower(),
            b=data["b"].lower(),
            c=data["c"].lower(),
            d=data["d"].lower(),
            e=data["e"].lower(),
            question_id=data["question_id"]
        )
        option.save()
        return option, HTTPStatus.CREATED

    @option_namespace.marshal_list_with(option_with_question)
    def get(self):
        questions = Options.query.all()
        return questions, HTTPStatus.OK


@option_namespace.route("/option/<int:option_id>")
class eachOptions(Resource):
    @option_namespace.marshal_with(option_with_question)
    def get(self, option_id):
        question = Options.get_by_id(option_id)
        return question, HTTPStatus.OK

    @option_namespace.expect(option_model)
    @option_namespace.marshal_with(option_with_question)
    def put(self, option_id):
        option_to_update = Options.get_by_id(option_id)
        data = option_namespace.payload

        if data["a"]:
            option_to_update.a = data["a"].lower()
        if data["b"]:
            option_to_update.b = data["b"].lower()
        if data["c"]:
            option_to_update.c = data["c"].lower()
        if data["d"]:
            option_to_update.d = data["d"].lower()
        if data["e"]:
            option_to_update.e = data["e"].lower()
        db.session.commit()
        return option_to_update

    def delete(self, option_id):
        option_to_delete = Options.get_by_id(option_id)
        db.session.delete(option_to_delete)
        db.session.commit()
        return {"message": "Option deleted"}
