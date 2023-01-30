from marshmallow import fields,Schema
from  .option import plainOptionSchema
from  .answer import plainAnswerSchema
class plainQuestionSchema(Schema):
    id=fields.Int(dump_only=True)
    question=fields.Str(required=True)
    
class  Questionschema(plainQuestionSchema):
    answer=fields.Nested(plainAnswerSchema(),dump_only=True)
    options=fields.Nested(plainOptionSchema(),dump_only=True)