import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi

class conexao:
    def __init__(self):
        self.name = "conexao"
        uri = "mongodb+srv://m001-student:m001-student@cluster0.3lcb5rw.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["seginfo2"]
        
        # Inserir alguns usuários na coleção "users"
        self.user = self.db["user"]
        self.user_data = [
            {"username": "João", "usermail": "joao@example.com", "userpassword": "senha123", "userrole": "user"},
            {"username": "Maria", "usermail": "maria@example.com", "userpassword": "senha456", "userrole": "admin"},
            {"username": "Pedro", "usermail": "pedro@example.com", "userpassword": "senha789", "userrole": "user"}
        ]
        self.user.insert_many(self.user_data)

        # Inserir algumas vendas na coleção "sells"
        self.sell = self.db["sell"]
        self.sell_data = [
            {"sellprod": "camisa", "sellprice": 50, "user_id":  self.user.find_one({"username": "João"})["_id"]},
            {"sellprod": "tênis", "sellprice": 200, "user_id":  self.user.find_one({"username": "Maria"})["_id"]},
            {"sellprod": "calça", "sellprice": 100, "user_id":  self.user.find_one({"username": "Pedro"})["_id"]}
        ]
        self.sell.insert_many(self.sell_data)

        # Criar a coleção "accesslog"
        self.accesslog = self.db["accesslog"]
