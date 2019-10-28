from flask_restful import Resource, reqparse
from model.assinante import Assinante
from dao.assinante_dao import AssinanteDao

class AssinanteController(Resource):
    def __init__(self):
        self.dao = AssinanteDao()#erro corrigido, uma classe sempre deve ser chamada com ()
        self.req = reqparse.RequestParser()
        self.req.add_argument("nome")
        self.req.add_argument("cpf")

    def get(self, id=None):
        if id is not None:
            return self.dao.assinante_by_id(id)
        return self.dao.list_all()
        #Quando se chama um método de outra classe que possui apenas 'self' como parâmetro não é necessário passar o 'self', corrigido isso na linha 15 do assinantes_control.py.
    def post(self):
        args = self.req.parse_args()
        nome = args['nome']
        cpf = args['cpf']
        assinante = Assinante(nome, cpf)
        return self.dao.create(assinante), 201

    def put(self, id):
        args = self.req.parse_args()
        nome = args['nome']
        cpf = args['cpf']
        assinante = Assinante(nome, cpf, id)
        return self.dao.update(assinante)

    def delete(self, id):
        self.dao.delete(id) # Faltou passar o paramentro 'id' para o metodo delete, fiz isso na linha 32 do assinantes_control.py
        return "pota que pariuuu", 204

