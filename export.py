from typing import Any

import getpass,pymongo
from models import conexao
from datetime import datetime
from flask import make_response
from bson import json_util, ObjectId
import json

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']

import json

id = input('Insira o iD do usuario')

foundUser = colecao.find_one({"_id": ObjectId(id)})

json_object = json.dumps(foundUser, default=json_util.default)

with open("sample.json", "w") as outfile:
    outfile.write((json_object))