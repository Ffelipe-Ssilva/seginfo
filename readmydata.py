from models import conexao
import getpass
from bson.objectid import ObjectId
import jwt
from bson import json_util, ObjectId
import json

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']

def findUser(token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
    except:
        return 'Unauthorized'
    foundUser = colecao.find_one({"_id": ObjectId(decodedToken['_id']['$oid'])})
    print(foundUser)
    return json.loads(json_util.dumps(foundUser))

def importUser(request):
    # Obter dados do JSON recebido

    # Extrair nome e e-mail do JSON
    nome = request.get('nome')
    email = request.get('email')

    # Verificar se nome e e-mail estão presentes no JSON
    if nome and email:
        # Criar documento a ser inserido no banco de dados
        documento = {'nome': nome, 'email': email}

        # Inserir documento no banco de dados
        colecao.insert_one(documento)

        return 'Cadastro realizado com sucesso!'
    else:
        return 'Erro: nome e/ou e-mail ausentes no JSON.'