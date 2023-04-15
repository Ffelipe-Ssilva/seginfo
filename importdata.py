    import pymongo

    # Conectando ao banco de dados MongoDB de origem
    mongo_client_src = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo_db_src = mongo_client_src["teste1"]
    mongo_collection_src = mongo_db_src["usuarios1"]

    # Conectando ao banco de dados MongoDB de destino
    mongo_client_dest = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo_db_dest = mongo_client_dest["teste2"]
    mongo_collection_dest = mongo_db_dest["usuarios2"]

# documents = [
#     {'name': 'Alice', 'age': 25, 'city': 'London'},
#     {'name': 'Bob', 'age': 35, 'city': 'Paris'},
#     {'name': 'Charlie', 'age': 40, 'city': 'Berlin'}
# ]
# result = mongo_collection_src.insert_many(documents)
# print('Inserted', len(result.inserted_ids), 'documents')

# Obtendo todos os documentos da coleção de origem
documents1 = mongo_collection_src.find()
documents2 = mongo_collection_dest.find()


# Iterando sobre todos os documentos e inserindo na coleção de destino
for doc in documents2:
    # mongo_collection_dest.insert_one(doc)
    print('Aqui temos o banco de dados de destino ')
    print(doc)
for doc in documents1:
    # mongo_collection_dest.insert_one(doc)
    print('Aqui temos o banco de dados de origem ')
    print(doc)