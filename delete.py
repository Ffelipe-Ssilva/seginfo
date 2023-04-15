from models import conexao
import getpass
from bson.objectid import ObjectId


conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']

confirm = input("Tem certeza que deseja excluir esse dado? ele não poderá ser restaurado... ")
if confirm == "sim":
    try:
        name = input("Enter username:")
        passw = getpass.getpass(prompt="Enter password:")
        user = colecao.find_one({'username': name, 'userpassword': passw, 'userrole': 'admin'})
        
        if user:
            idu = input("ID do usuario a ser excluido:")
            result = colecao.delete_one({'_id': ObjectId(idu)})
            
            if result.deleted_count == 1:
                print("dado excluido")
            else:
                print("usuário não encontrado")
        else:
            print("acesso negado")
    except Exception as e:
        print(f"Erro ao excluir o usuário: {e}")
else:
    print("processo encerrado")

