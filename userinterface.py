from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId

from datetime import datetime


conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]
colecao = db['sell']
acceptance= db['acceptance']

import pymongo
from pymongo import MongoClient
import getpass

try:
    name= input("Enter username:")
    passw= getpass.getpass(prompt="Enter password:")

    # Faz a consulta no banco de dados
    user = db.user.find_one({'username': name, 'userpassword': passw})
    if user !='':
        idsession = user['_id']
        private=user['useradds']
        pref=user['userpref']
        name=user['username']
        validation = "ok"
        print("login concluido")
    else:
        validation = None
        print("acesso negado")
except Exception as e:
    validation = None
    print(f"Erro ao realizar o login: {e}")

if validation == "ok":


    acceptquery = db.acceptance.find_one({'userid': idsession},sort=[("_id", pymongo.DESCENDING)])
    latestaccept=int(acceptquery['version'])

    termos = db.terms.find_one({},sort=[( '_id', pymongo.DESCENDING )])
    versiontermo=int(termos['version'])

    if versiontermo>latestaccept:
        termos = db.terms.find_one({},sort=[( '_id', pymongo.DESCENDING )])
        conteudotermo=str(termos['conditions'])
        versiontermo=str(termos['version'])
        idtermo=str(termos['_id'])

        print("Há uma nova versão dos temos de privacidade")
        print(conteudotermo)
        consent=""
        while consent !="OK":
            checkmail=input("Deseja receber emails?")
            if checkmail == "sim":
                acceptemail=True
            if checkmail == "nao":
                acceptemail=False

            checksensible=input("Deseja user dados sensiveis?")
            if checksensible == "sim":
                acceptsensible=True
            if checksensible == "nao":
                acceptsensible=False

            checkads=input("Deseja customizar anuncios?")
            if checkads == "sim":
                acceptads=True
            if checkads == "nao":
                acceptads=False

            #checkwpp=input("Deseja receber whatsapp?")
            #if checkwpp == "sim":
            #    acceptwpp=True
            #if checkwpp == "nao":
            #    acceptwpp=False

            consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")
        accept = {'userid': idsession, 'termid' : idtermo, 'user': name, 'version': versiontermo, 'date': datetime.now(),'acceptadds':acceptads,'acceptemail':acceptemail,'acceptsensible':acceptsensible}
        result = acceptance.insert_one(accept)

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