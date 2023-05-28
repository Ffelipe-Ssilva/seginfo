import getpass,pymongo
from models import conexao
from datetime import datetime
from flask import make_response
from bson import json_util, ObjectId
import json
import jwt

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']

def loginUser(request):
    user = colecao.find_one({'username': request.get('username'), 'userpassword': request.get('password')})
    if user is not None:
        encoded_jwt = jwt.encode(json.loads(json_util.dumps(user)), 'secret', algorithm="HS256")
    return encoded_jwt
