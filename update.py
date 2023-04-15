from models import conexao
import pymongo
from getpass import getpass
from bson.objectid import ObjectId


conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

try:
    name= input("Enter username:")
    passw= getpass(prompt="Enter password:")
    user_collection = db["user"]
    user = user_collection.find_one({"username": name, "userpassword": passw})
    idsession = user["_id"]

    if idsession != None:
        validation = "ok"
        print("login concluido")
    else:
        validation = None
        print("acesso negado")
except Exception as e:
    validation = None
    print(f"Erro ao logar o usuário: {e}")

if(validation=="ok"):
    user_collection = db["user"]
    name= input("Enter new username:")
    mail= input("Enter new email:")
    user_collection.update_one({"_id": idsession}, {"$set": {"username": name, "usermail": mail}})
    print("Update concluido")
