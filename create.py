import getpass,pymongo
from models import conexao
from datetime import datetime

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']
terms = db['terms']
aceite = db['acceptance']
consentlist=[]
name= input("Enter username:")
mail= input("Enter email:")
passw= getpass.getpass(prompt="Enter password:")

#buscando dados do banco de termos
termos = db.terms.find_one({},sort=[( '_id', pymongo.DESCENDING )])
conteudotermo=str(termos['conditions'])
versiontermo=str(termos['version'])
print(versiontermo)
idtermo=str(termos['_id'])

print("Termos de politica e privacidade")
print(conteudotermo)
consent=""
while consent !="OK":
    
    sensible= input("Nosso sistema conta com indicadores que utilizam dados sensíveis. Voce consente fornecer dados como etnia, idade e genero? Essas informações são completamente opcionais e não prejudicarão sua experiência com o sistema.")
    if sensible=="sim":
        print("Okay, por favor preencha as seguintes informações")
        eth= input("Enter ethnicity:")
        gen= input("Enter gender:")
        age= input("Enter age:")
        acceptsensible=True
        consentlist.append("Uso de dados sensíveis")
    else:
        print("Okay, não utilizaremos informações sensíveis")
        acceptsensible=False
   
    ads= input("Deseja utilizar informações das suas comprar para personalizar seus anuncios? (Isso não influenciara na aparição de anúncios, apenas seu conteúdo)")
    if ads=="sim":
        userads=True
        acceptads=True
        consentlist.append("Personalização de anúncios")
    else:
        userads=False
        acceptads=False

    checkmail=input("Deseja receber emails?")
    if checkmail == "sim":
        acceptemail=True
        consentlist.append("Envio de Emails")
    if checkmail == "nao":
        acceptemail=False

#    checkwpp=input("Deseja receber whatsapp?")
#    if checkwpp == "sim":
#        acceptwpp=True
#    else:
#        acceptwpp=False

    consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")

#consentimento dos dados sensíveis



#if consent == "OK":
#    ads=input("deseja utilizar seus dados para customizar sua experiencia?")
#    while ads !="sim" or ads !="não":
#        if ads=="sim":
#            print("seus anuncios serão customizado de acordo com seus gostos")
#        elif ads=="não":
#            print("seus anuncios serão gerados aleatoriamente")
#        ads= input("")
print(consent)
if consent == "OK":
        print("entrou")
        if sensible=="sim":
            print("entrou")
            dados = {'username': name, 'usermail' : mail, 'userpassword': passw, 'userrole': 'user','usergender': gen, 'userethnicity':eth, 'userage': age, 'useradds': userads, 'userpref': ''}
            result = colecao.insert_one(dados)
            print(result.inserted_id)
            useratual=result.inserted_id
        else:
            print("entrou")
            dados = {'username': name, 'usermail' : mail, 'userpassword': passw, 'userrole': 'user', 'useradds': userads, 'userpref': ''}
            result = colecao.insert_one(dados)
            print(result.inserted_id)
            useratual=result.inserted_id
usuarios = colecao.find()
for usuario in usuarios:
    print(usuario)

print(name)
print(passw)
user = db.user.find_one({'username': name, 'userpassword': passw})
print(user)
if user !='':
    useratual = user['_id']
#registrar aceite do usuario
acceptance = {'userid': useratual, 'termid' : idtermo, 'user': name, 'version': versiontermo, 'date': datetime.now(),'acceptarray':consentlist}
#,'acceptwpp': acceptwpp
result = aceite.insert_one(acceptance)