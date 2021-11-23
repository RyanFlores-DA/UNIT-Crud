from models import Usuarios

# Inserir usuário
def insere_usuario():
    pessoa = Usuarios(nome='Luke Skywallker', idade=150)
    pessoa.save()

# Listar usuário
def lista_usuario():
    pessoas = Usuarios.query.all()
    print(pessoas)

# Consultar usuário
def consulta_pessoa():
    pessoa = Usuarios.query.filter_by(nome='Skywallker').first()
    print(pessoa.id)

# Atualizar usuário
def atualiza_pessoa():
    pessoa = Usuarios.query.filter_by(id=2).first()
    pessoa.nome = "Leia"
    pessoa.save()

# # Deletar usuário
def remove_pessoa():
    pessoa = Usuarios.query.filter_by(id=2).first()
    pessoa.delete()

if __name__ == '__main__':
     insere_usuario()
    # consulta_usuario()
    # atualiza_usuario()
    # remove_usuario()
