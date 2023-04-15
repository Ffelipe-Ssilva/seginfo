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


# class criarBancos:
# Criar a coleção accesslog
# accesslog = self.db["accesslog"]
# accesslog.create_index([("idaccesslog", pymongo.ASCENDING)], unique=True)
# accesslog.create_index([("iduseracces", pymongo.ASCENDING)])
# accesslog.create_index([("context", pymongo.ASCENDING)])
# accesslog.create_index([("iduseranalysed", pymongo.ASCENDING)])

# accesslog.insert_many([
#     {"idaccesslog": 1, "iduseracces": 15, "context": "cobrança por email", "iduseranalysed": 0},
#     {"idaccesslog": 2, "iduseracces": 15, "context": "cobrança por email", "iduseranalysed": None}
# ])


        # documents1 = user.find()


# # Iterando sobre todos os documentos e inserindo na coleção de destino
# for doc in documents1:
#     # mongo_collection_dest.insert_one(doc)
#     print('Aqui temos o banco de dados de origem ')
#     print(doc)

# # Caso queira criar o banco 2, descomentar código abaixo
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["seginfo2"]

# # Criar a coleção sell
# sell2 = self.db["sell2"]
# sell2.create_index([("sellprod", pymongo.ASCENDING)])
# sell2.create_index([("sellsize", pymongo.ASCENDING)])


# # Criar coleção "user"
# user2 = self.db["user2"]

# # Criar índices
# user2.create_index("usermail", unique=True)
# user2.create_index("userloc", unique=True)
# user2.create_index("userage", unique=True)


# # sell2.insert_many([
# #     {   "sellprod": "celular", "sellsize": 1600},
# #     {   "sellprod": "computador", "sellsize": 100},
# #     {   "sellprod": "mouse", "sellsize": 230},
# #     {   "sellprod": "teclado", "sellsize": 500},
# #     {   "sellprod": "fone", "sellsize": 10},
# # ])

# # # Insere um usuário
# # user2.insert_one({"usermail": "joao@example.com", "userloc": "São Paulo", "userage": 25})

# # # Insere outro usuário
# # user2.insert_one({ "usermail": "maria@example.com", "userloc": "Rio de Janeiro", "userage": 30})

# # # Insere mais um usuário
# # user2.insert_one({ "usermail": "carlos@example.com", "userloc": "Belo Horizonte", "userage": 20})

# # # Insere mais um usuário
# # user2.insert_one({ "usermail": "ana@example.com", "userloc": "Curitiba", "userage": 35})

# # # Insere mais um usuário
# # user2.insert_one({ "usermail": "pedro@example.com", "userloc": "Porto Alegre", "userage": 40})

# documents2 = user2.find()

# for doc in documents2:
#     print('Aqui temos o banco de dados de destino ')
#     print(doc)
        
