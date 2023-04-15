from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId


conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

import pymongo
from pymongo import MongoClient
import getpass

try:
    name= input("Enter username:")
    passw= getpass.getpass(prompt="Enter password:")

    # Faz a consulta no banco de dados
    user = db.user.find_one({'username': name, 'userpassword': passw, 'userrole': 'admin'})

    if user:
        idsession = str(user['_id'])
        validation = "ok"
        print("login concluido")
    else:
        validation = None
        print("acesso negado")
except Exception as e:
    validation = None
    print(f"Erro ao realizar o login: {e}")

if validation == "ok":
    # Faz a consulta dos e-mails dos usuários
    users = db.user.find({}, {'usermail': 1})
    resultado = [u['usermail'] for u in users]

    print("Emails de usuarios devedores. Dados devem ser utilizados apenas para cobrança")
    print(resultado)

    # Registra a ação no log
    db.accesslog.insert_one({'iduseracces': idsession, 'context': 'cobrança por email'})
    print("Ação registrada no log")
