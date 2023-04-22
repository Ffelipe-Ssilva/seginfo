import getpass
from models import conexao

conexao = conexao()
client = conexao.get_client()
db = client["seginfo"]

colecao = db['user']
name= input("Enter username:")
mail= input("Enter email:")
passw= getpass.getpass(prompt="Enter password:")


consent= input("Termos de politica e privacidade versão 1")
while consent !="OK":
    if consent=="sensivel":
        sensible= input("Nosso sistema conta com indicadores que utilizam dados sensíveis. Voce consente fornecer dados como etnia, idade e genero? Essas informações são completamente opcionais e não prejudicarão sua experiência com o sistema.")
        if sensible=="sim":
            print("Okay, por favor preencha as seguintes informações")
            eth= input("Enter ethnicity:")
            gen= input("Enter gender:")
            age= input("Enter age:")
        elif sensible=="não":
            print("Okay, não utilizaremos informações sensíveis")
    elif consent=="adds":
        ads= input("Deseja utilizar informações das suas comprar para personalizar seus anuncios? (Isso não influenciara na aparição de anúncios, apenas seu conteúdo)")
        if ads=="sim":
            userads=True
        else:
            userads=False
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
if consent == "OK":
        if sensible=="sim":
            dados = {'username': name, 'usermail' : mail, 'userpassword': passw, 'userrole': 'user','usergender': gen, 'userethnicity':eth, 'userage': age, 'useradds': userads, 'userpref': ''}
            result = colecao.insert_one(dados)
            print(result.inserted_id)
        elif sensible=="não":
            dados = {'username': name, 'usermail' : mail, 'userpassword': passw, 'userrole': 'user', 'useradds': userads, 'userpref': ''}
            result = colecao.insert_one(dados)
            print(result.inserted_id)

usuarios = colecao.find()
for usuario in usuarios:
    print(usuario)