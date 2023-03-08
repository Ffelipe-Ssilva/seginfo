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
consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")

while consent !="OK":
    if consent=="termos":
        print("esses são os termos de serviço")
    elif consent=="privacy":
        print("essa é a politica de privacidade")
    consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")
if consent == "OK":
    comando=f"insert into bdinfosecurity.user (username, usermail, userpassword, userrole) values ('{name}', '{mail}', '{passw}', 'user')"

    cursor.execute(comando)
    conexao.commit()
    resultado=cursor.fetchall()
    cursor.close()
    conexao.close()