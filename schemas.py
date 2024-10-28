from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    due_date = fields.Str()
    priority = fields.Str()
    status = fields.Str()
    user_id = fields.Int(dump_only=True)