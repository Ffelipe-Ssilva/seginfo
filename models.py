import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Criar a conexão com o banco de dados
class conexao:
    def get_client(self):
        return self.client

    def __init__(self):
        self.name = "conexao"
        uri = "mongodb+srv://m001-student:m001-student@cluster0.3lcb5rw.mongodb.net/?retryWrites=true&w=majority"
        # self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.client = MongoClient("mongodb+srv://m001-student:m001-student@cluster0.3lcb5rw.mongodb.net/test")
        self.db = self.client["seginfo"]
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        # self.users = self.db["user"]
        # self.user_data = [
        #         {"username": "Alice", "usermail": "alice@example.com", "userpassword": "password123", "userrole": "admin"},
        #         {"username": "Bob", "usermail": "bob@example.com", "userpassword": "password123", "userrole": "user"},
        #         {"username": "Charlie", "usermail": "charlie@example.com", "userpassword": "password123", "userrole": "user"},
        #         {"username": "Dave", "usermail": "dave@example.com", "userpassword": "password123", "userrole": "user"},
        #         {"username": "Eve", "usermail": "eve@example.com", "userpassword": "password123", "userrole": "user"}
        # ]
        # self.users.insert_many(self.user_data)

        # # criando a coleção sell e inserindo dados de exemplo
        # self.sells = self.db["sell"]
        # self.sell_data = [
        #         {"sellprod": "celular", "sellprice": 1000, "user_id":  self.users.find_one({"username": "Alice"})["_id"]},
        #         {"sellprod": "notebook", "sellprice": 3000, "user_id":  self.users.find_one({"username": "Bob"})["_id"]},
        #         {"sellprod": "tablet", "sellprice": 1500, "user_id":  self.users.find_one({"username": "Charlie"})["_id"]},
        #         {"sellprod": "smartwatch", "sellprice": 800, "user_id":  self.users.find_one({"username": "Alice"})["_id"]},
        #         {"sellprod": "televisão", "sellprice": 4000, "user_id":  self.users.find_one({"username": "Eve"})["_id"]},
        #         {"sellprod": "fones de ouvido", "sellprice": 100, "user_id":  self.users.find_one({"username": "Dave"})["_id"]},
        #         {"sellprod": "caixa de som", "sellprice": 200, "user_id":  self.users.find_one({"username": "Bob"})["_id"]},
        #         {"sellprod": "computador", "sellprice": 5000, "user_id":  self.users.find_one({"username": "Charlie"})["_id"]},
        #         {"sellprod": "impressora", "sellprice": 700, "user_id":  self.users.find_one({"username": "Eve"})["_id"]},
        #         {"sellprod": "mouse", "sellprice": 50, "user_id":  self.users.find_one({"username": "Dave"})["_id"]}
        # ]
        # self.sells.insert_many(self.sell_data)


        # Criar a coleção accesslog
        # accesslog = self.db["accesslog"]