from models import conexao
import getpass
from bson.objectid import ObjectId
import jwt

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']

def deleteUser(userId, token):
    try:
        decodedToken = jwt.decode(token, 'secret', algorithms=["HS256"])
        if decodedToken['userrole'] != 'admin':
            return 'Unauthorized'
    except:
        return 'Unauthorized'
    result = colecao.delete_one({'_id': ObjectId(userId)})
    if result.deleted_count == 1:
        return 'Deleted'
    else:
        return 'Not_Found'
