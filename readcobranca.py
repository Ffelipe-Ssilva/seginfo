import mysql.connector as sqlcon
import getpass

conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)

try:
    name= input("Enter username:")
    passw= getpass.getpass(prompt="Enter password:")
    validate = conexao.cursor()
    comando=f"select user.userid from bdinfosecurity.user where user.username = '{name}' and user.userpassword = '{passw}' and user.userrole='admin'"

    validate.execute(comando)
    queryresult=validate.fetchone()
    for row in queryresult:
        idsession=row

    if idsession != None:
        validation = "ok"
        print("login concluido")
    else:
        validation = None
        print("acesso negado")
    validate.close()
except:
    validation = None
    print("acesso negado")

if(validation=="ok"):
    cursor = conexao.cursor()
    comando='select user.usermail from bdinfosecurity.user'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    print("Emails de usuarios devedores. Dados devem ser utilizados apenas para cobrança")
    print(resultado)
    cursor.close()

    log = conexao.cursor()
    comando=f"insert into bdinfosecurity.accesslog (iduseracces, context) values ('{idsession}', 'cobrança por email')"
    log.execute(comando)
    conexao.commit()
    log.close()