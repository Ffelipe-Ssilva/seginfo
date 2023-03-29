import mysql.connector as sqlcon
import getpass


conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)
cursor = conexao.cursor()
name= input("Enter username:")
mail= input("Enter email:")
passw= getpass.getpass(prompt="Enter password:")

#consentimento dos dados sensíveis
sensible= input("Nosso sistema conta com indicadores que utilizam dados que podem ser considerados sensíveis para alguns usuários. Voce consente fornecer dados como etnia, idade e genero? Essas informações são completamente opcionais e não prejudicarão sua experiência com o sistema.")
if sensible=="sim":
    print("Okay, por favor preencha as seguintes informações")
    eth= input("Enter ethnicity:")
    gen= input("Enter gender:")
    age= input("Enter age:")
elif sensible=="não":
    print("Okay, não utilizaremos informações sensíveis")

consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")
while consent !="OK":
    if consent=="termos":
        print("esses são os termos de serviço")
    elif consent=="privacy":
        print("essa é a politica de privacidade")
    consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")
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
            comando=f"insert into bdinfosecurity.user (username, usermail, userpassword, userrole, usergender, userethnicity, userage) values ('{name}', '{mail}', '{passw}', 'user', '{gen}', '{eth}', {age})"
        elif sensible=="não":
             comando=f"insert into bdinfosecurity.user (username, usermail, userpassword, userrole) values ('{name}', '{mail}', '{passw}', 'user')"    

        cursor.execute(comando)
        conexao.commit()
        resultado=cursor.fetchall()
        cursor.close()
        conexao.close()