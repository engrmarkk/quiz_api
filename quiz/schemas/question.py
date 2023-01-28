from marshmallow import fields,Schema
class plainQuestionSchema(Schema):
    id=fields.Int(dump_only=True)
    question=fields.Str(required=True)
    
