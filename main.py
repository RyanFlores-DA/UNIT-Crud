from flask import Flask
from flask_restful import Resource, Api
from models import Usuarios

app = Flask(__name__)
api = Api(app)

class Usuario(Resource):
    def get(self, id):
        try:
            usuario = Usuarios.query.filter_by(id=id).first()
            response = {
                'id': usuario.id,
                'nome': usuario.nome,
                'email': usuario.email
            }
            return response
        except:
            return {
                'erro': 'Algo deu errado!'
            }
class Usuarios(Resource):
    def get(self):
        usuarios = Usuarios.query.all()
        return usuarios


api.add_resource(Usuario, '/usuarios/<int:id>')
api.add_resource(Usuarios, '/usuarios')

if __name__ == '__main__':
    app.run(debug=True)