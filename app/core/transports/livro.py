from marshmallow import Schema, fields


class LivroTransport(Schema):
    id = fields.UUID()
    titulo = fields.String()
    autor = fields.String()
    editor = fields.String()
    publicado_em = fields.Date()
    
    