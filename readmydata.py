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

def importUser(request):
    data = json.load(request.files['user'])
    accept = (request.form.get('accept')).split(',')
    userParsed = {"_id": ObjectId(data['_id']['$oid'])}
    if('name' in accept):
        userParsed = {**userParsed, 'username': data['username']}
    if('usermail' in accept):
        userParsed = {**userParsed, 'usermail': data['usermail']}
    if('userrole' in accept):
        userParsed = {**userParsed, 'userrole': data['userrole']}
    if('useradds' in accept):
        userParsed = {**userParsed, 'useradds': data['useradds']}
    if('userpref' in accept):
        userParsed = {**userParsed, 'userpref': data['userpref']}

    createdUserId = colecao.insert_one(userParsed).inserted_id
    createdUser = colecao.find_one({"_id": ObjectId(createdUserId)})

    return {'parsedUser': json.loads(json_util.dumps(createdUser))}