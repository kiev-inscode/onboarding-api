from marshmallow import fields, Schema

from core.schemas import LivroSchema, UsuarioSchema

class EmprestimoSchema(Schema):
    id = fields.UUID()
    livro = fields.Nested(LivroSchema)
    usuario = fields.Nested(UsuarioSchema)
    devolvido_em = fields.Date(allow_none=True)
    emprestado_em = fields.Date()
    vencimento_em = fields.Date()
    is_atrasado = fields.Boolean()