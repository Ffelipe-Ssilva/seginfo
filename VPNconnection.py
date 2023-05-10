import pymongo
import json
from models import conexao
from getpass import getpass
from bson.objectid import ObjectId


# Conecte-se ao banco de dados
conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
collection = db["nome_da_colecao"]

# Defina o ID do usuário que você deseja buscar
user_id = "id_do_usuario"

# Busque o usuário pelo ID
user = collection.find_one({"_id": user_id})

# Verifique se o usuário foi encontrado
if user:
  # Se o usuário foi encontrado, crie um arquivo JSON com seus dados
  with open("dados_do_usuario.json", "w") as file:
    json.dump(user, file)
else:
  print("Usuário não encontrado.")
#Cadastrando dados do json no banco:

import pymongo
import json

# Conecte-se ao banco de dados
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nome_do_banco_de_dados"]
collection = db["nome_da_colecao"]

# Leia o arquivo JSON com os dados a serem cadastrados
with open("dados.json", "r") as file:
    data = json.load(file)

# Insira os dados na coleção
for user in data:
    user_data = {
        "nome": user["nome"],
        "email": user["email"],
        "cpf": user["cpf"]
    }
    result = collection.insert_one(user_data)

# Exiba o número de documentos inseridos
print("Documentos inseridos: ", len(data))