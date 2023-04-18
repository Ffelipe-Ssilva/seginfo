from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId


conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
colecao = db['sell']

import pymongo
from pymongo import MongoClient
import getpass

try:
    name= input("Enter username:")
    passw= getpass.getpass(prompt="Enter password:")

    # Faz a consulta no banco de dados
    user = db.user.find_one({'username': name, 'userpassword': passw})
    if user !='':
        idsession = str(user['_id'])
        private=user['useradds']
        pref=user['userpref']
        validation = "ok"
        print("login concluido")
    else:
        validation = None
        print("acesso negado")
except Exception as e:
    validation = None
    print(f"Erro ao realizar o login: {e}")

if validation == "ok":
    if private:
        print("anuncio: ESPECÍFICO!!!")
        print(f"oferta de ["+pref+"]")
    else:
        print("anuncio: ALEATÓRIO!!!")
        
 
    print("Escolha um produto: ")
    print("Celular - R$1000,00")
    print("Notebook - R$3000,00")
    print("Tablet - R$1500,00")
    print("Smartwatch - R$800,00")
    print("Televisão - R$4000,00")
    print("Fones de ouvido - R$100,00")
    print("Caixa de som - R$200,00")
    print("Computador - R$5000,00")
    print("Impressora - R$700,00")
    print("Mouse - R$50,00")
    prodesc= input("...")
    price=0
    if prodesc == "celular":
        price = 1000
    elif prodesc == "notebook":
        price = 3000
    elif prodesc == "tablet":
        price = 1500
    elif prodesc == "smartwatch":
        price = 800
    elif prodesc == "televisao":
        price = 4000
    elif prodesc == "fone":
        price = 100
    elif prodesc == "caixa":
        price = 200
    elif prodesc == "computador":
        price = 5000
    elif prodesc == "impressora":
        price = 700
    elif prodesc == "mouse":
        price = 50

    dados = {'sellprod': prodesc, 'sellprice' : price, 'userpassword': idsession}
    result = colecao.insert_one(dados)


 
    if private:
        personalizar = db['user']
        myquery = {"_id": ObjectId(idsession)}
        newvalues = {"$set": {"userpref": str(prodesc)}}
        result = personalizar.find_one_and_update(myquery, newvalues)