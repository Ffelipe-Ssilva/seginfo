from models import conexao
import getpass
from bson.objectid import ObjectId


conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']

try:
    name = input("Enter username:")
    passw = getpass.getpass(prompt="Enter password:")

    # Consulta o usuário no banco de dados
    user = db.user.find_one({
        'username': name,
        'userpassword': passw
    })

    if user and user['userrole'] == 'admin':
        idsession = user['_id']
        validation = "ok"
        print("login concluido")
    else:
        validation = None
        print("acesso negado")
except:
    validation = None
    print("acesso negado")

if validation == "ok":
    # Consulta as informações do usuário utilizando o ID da sessão
    resultado = db.user.find_one({'_id': idsession})
    print(resultado)
