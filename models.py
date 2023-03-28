import pymongo

# Criar a conexão com o banco de dados
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["seginfo"]

# # Criar a coleção accesslog
# accesslog = db["accesslog"]
# accesslog.create_index([("idaccesslog", pymongo.ASCENDING)], unique=True)
# accesslog.create_index([("iduseracces", pymongo.ASCENDING)])
# accesslog.create_index([("context", pymongo.ASCENDING)])
# accesslog.create_index([("iduseranalysed", pymongo.ASCENDING)])

# # Criar a coleção sell
# sell = db["sell"]
# sell.create_index([("idsell", pymongo.ASCENDING)], unique=True)
# sell.create_index([("sellprod", pymongo.ASCENDING)])
# sell.create_index([("sellprice", pymongo.ASCENDING)])


# # Criar coleção "user"
user = db["user"]

# # Criar índices
# user.create_index("userid", unique=True)
# user.create_index("usermail", unique=True)

# accesslog.insert_many([
#     {"idaccesslog": 1, "iduseracces": 15, "context": "cobrança por email", "iduseranalysed": 0},
#     {"idaccesslog": 2, "iduseracces": 15, "context": "cobrança por email", "iduseranalysed": None}
# ])

# sell.insert_many([
#     {"idsell": 1, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 2, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 3, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 4, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 5, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 6, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 7, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 8, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 9, "sellprod": "{produto}", "sellprice": 1000},
#     {"idsell": 10, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 11, "sellprod": "celular", "sellprice": 1000},
#     {"idsell": 12, "sellprod": "pedra", "sellprice": 1000}
# ])


# # Inserir documentos
# user.insert_many([
#     {"userid": 1, "username": "Alice", "usermail": "alice@example.com", "userpassword": "password123", "userrole": "admin"},
#     {"userid": 2, "username": "Bob", "usermail": "bob@example.com", "userpassword": "password456", "userrole": "user"},
#     {"userid": 3, "username": "Charlie", "usermail": "charlie@example.com", "userpassword": "password789", "userrole": "user"}
# ])

documents1 = user.find()


# Iterando sobre todos os documentos e inserindo na coleção de destino
for doc in documents1:
    # mongo_collection_dest.insert_one(doc)
    print('Aqui temos o banco de dados de origem ')
    print(doc)

# Caso queira criar o banco 2, descomentar código abaixo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["seginfo2"]

# Criar a coleção sell
sell2 = db["sell2"]
sell2.create_index([("idsell", pymongo.ASCENDING)], unique=True)
sell2.create_index([("sellprod", pymongo.ASCENDING)])
sell2.create_index([("sellsize", pymongo.ASCENDING)])


# Criar coleção "user"
user2 = db["user2"]

# Criar índices
user2.create_index("userid", unique=True)
user2.create_index("usermail", unique=True)
user2.create_index("userloc", unique=True)
user2.create_index("userage", unique=True)


# sell2.insert_many([
#     {"idsell": 1, "sellprod": "celular", "sellsize": 1600},
#     {"idsell": 2, "sellprod": "computador", "sellsize": 100},
#     {"idsell": 3, "sellprod": "mouse", "sellsize": 230},
#     {"idsell": 4, "sellprod": "teclado", "sellsize": 500},
#     {"idsell": 5, "sellprod": "fone", "sellsize": 10},
# ])

# # Insere um usuário
# user2.insert_one({"userid": 1, "usermail": "joao@example.com", "userloc": "São Paulo", "userage": 25})

# # Insere outro usuário
# user2.insert_one({"userid": 2, "usermail": "maria@example.com", "userloc": "Rio de Janeiro", "userage": 30})

# # Insere mais um usuário
# user2.insert_one({"userid": 3, "usermail": "carlos@example.com", "userloc": "Belo Horizonte", "userage": 20})

# # Insere mais um usuário
# user2.insert_one({"userid": 4, "usermail": "ana@example.com", "userloc": "Curitiba", "userage": 35})

# # Insere mais um usuário
# user2.insert_one({"userid": 5, "usermail": "pedro@example.com", "userloc": "Porto Alegre", "userage": 40})

documents2 = user2.find()

for doc in documents2:
    print('Aqui temos o banco de dados de destino ')
    print(doc)
