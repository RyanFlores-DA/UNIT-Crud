from flask import Flask, request
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

users = [{
    "userName": 'Ryan Flores',
    "email": "contato@alianca.org",
    "senha": "******"
}
]

class Users(Resource):
    def get(self):
        return users

    def post(self):
        newUser = json.loads(request.data)
        users.append(newUser)
        return {
            "Confirmacao": "Usuário Cadastrado com sucesso!",
            "User": newUser
        }

class User(Resource):
    def get(self, indice):
        try:
            return {
                "id": indice + 1,
                "User": users[indice]
            }
        except IndexError:
            message = "User {} not found".format(indice)
            return {
                "Warning": message,
                "user state": "Error"
            }
        except:
            message = "User {} not found".format(indice)
            return {
                "Warning": message,
                "Error": "Unknow error"
            }

    def delete(self, indice):
        users.pop(indice)
        return{
            "Warning": "Deleted",
            "Users": users
        }

    def put(self, indice):
        newValue = json.loads(request.data)
        users[indice] = newValue
        return {
            "Message": "Updated!",
            "New": newValue
        }

api.add_resource(User, '/users/<int:indice>')
api.add_resource(Users, '/users')

if __name__ == "__main__":
    app.run(debug=True)