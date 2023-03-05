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
    comando=f"select user.userid from bdinfosecurity.user where user.username = '{name}' and user.userpassword = '{passw}'"
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
    comando=f"select * from bdinfosecurity.user where user.userid = {idsession}"
    cursor.execute(comando)
    resultado=cursor.fetchall()
    print(resultado)
    cursor.close()