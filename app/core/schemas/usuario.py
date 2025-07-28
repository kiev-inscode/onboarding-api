from marshmallow import Schema, fields


class UsuarioSchema(Schema):
    id = fields.UUID()
    nome = fields.String()
    idade = fields.Integer()
    email = fields.Email()