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
    name= input("Enter new username:")
    mail= input("Enter new email:")
    comando=f"update bdinfosecurity.user set username = '{name}', usermail = '{mail}' where userid = {idsession}"
    cursor.execute(comando)
    conexao.commit()
    resultado=cursor.fetchall()
    cursor.close()
    conexao.close()



