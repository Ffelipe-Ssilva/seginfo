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
    comando='select user.userethnicity,count(user.userethnicity) as contador from bdinfosecurity.user where user.userethnicity is not null group by user.userethnicity'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    print("Contagem de etnias dos usuários")
    print(resultado)
    cursor.close()

    cursor = conexao.cursor()
    comando='select user.userage,count(user.userage) as etnia from bdinfosecurity.user where user.userage is not null group by user.userage'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    print("Contagem de idades dos usuários")
    print(resultado)
    cursor.close()

    cursor = conexao.cursor()
    comando='select user.usergender,count(user.usergender) as etnia from bdinfosecurity.user where user.usergender is not null group by user.usergender'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    print("Contagem de genero dos usuários")
    print(resultado)
    cursor.close()

    log = conexao.cursor()
    comando=f"insert into bdinfosecurity.accesslog (iduseracces, context) values ({idsession}, 'geração de indicadores')"
    log.execute(comando)
    conexao.commit()
    log.close()