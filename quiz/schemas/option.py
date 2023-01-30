from marshmallow import fields,Schema

class plainOptionSchema(Schema):
    id=fields.Int(dump_only=True)
    a=fields.Str(required=True)
    b=fields.Str(required=True)
    c=fields.Str(required=True)
    d=fields.Str(required=True)
    e=fields.Str(required=True)

class OptionSchema(plainOptionSchema):
    question_id=fields.Int(load_only=True,required=True)
    