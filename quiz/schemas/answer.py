from marshmallow import fields,Schema
class plainAnswerSchema(Schema):
    id=fields.Int(dump_only=True)
    answer=fields.Str(required=True)
    
class AnswerSchema(plainAnswerSchema):
    question_id=fields.Int(load_only=True,required=True)