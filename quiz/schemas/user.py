from marshmallow import Schema,fields

class userLoginSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str(required=True)
    password=fields.Str(required=True)

class userRegisterSchema(Schema):
    id=fields.Int(dump_only=True)
    first_name=fields.Str(required=True)
    last_name=fields.Str(required=True)
    email=fields.Str(required=True)
    username=fields.Str(required=True)
    password=fields.Str(required=True)


