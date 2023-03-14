import mysql.connector as sqlcon
from pymongo import MongoClient

# Conectar ao banco de dados MySQL
conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)

# Conectar ao banco de dados MongoDB
mongo_client = MongoClient("mongodb+srv://admin-fatec:adminadmin@clustersi.4kdc2kp.mongodb.net/?retryWrites=true&w=majority")
mongo_db = mongo_client['Login-Usuarios']
mongo_collection = mongo_db['usuarios']


# Recuperar os dados do MySQL
mysql_cursor = conexao.cursor()
mysql_cursor.execute('SELECT * FROM bdinfosecurity.user')
mysql_data = mysql_cursor.fetchall()

# Inserir os dados do MySQL no MongoDB
for row in mysql_data:
    data = {
        'campo1': row[0],
        'campo2': row[1],
        'campo3': row[2],
        # ...
    }
    mongo_collection.insert_one(data)
