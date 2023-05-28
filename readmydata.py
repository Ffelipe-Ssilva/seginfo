from models import conexao
import getpass
from bson.objectid import ObjectId
import jwt
from bson import json_util, ObjectId
import json

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']

def findUser(token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
    except:
        return 'Unauthorized'
    foundUser = colecao.find_one({"_id": ObjectId(decodedToken['_id']['$oid'])})
    print(foundUser)
    return json.loads(json_util.dumps(foundUser))