from models import Usuarios

# Inserir usuário
def insere_usuario():
    usuario = Usuarios(nome='Luke Skywallker', idade=150)
    usuario.save()

# Listar usuário
def lista_usuario():
    usuarios = Usuarios.query.all()
    print(usuarios)

# Consultar usuário
def consulta_usuario():
    usuario = Usuarios.query.filter_by(nome='Skywallker').first()
    print(usuario.id)

# Atualizar usuário
def atualiza_usuario():
    usuario = Usuarios.query.filter_by(id=1).first()
    usuario.nome = "Leia"
    usuario.save()

# # Deletar usuário
def remove_usuario():
    usuario = Usuarios.query.filter_by(id=1).first()
    usuario.delete()

if __name__ == '__main__':
     insere_usuario()
    # consulta_usuario()
    # atualiza_usuario()
    # remove_usuario()
