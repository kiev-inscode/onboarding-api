from marshmallow import Schema, fields


class LivroSchema(Schema):
    id = fields.UUID()
    titulo = fields.String()
    autor = fields.String()
    editor = fields.String()
    publicado_em = fields.Date()
    
    