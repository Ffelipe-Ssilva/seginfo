import mysql.connector as sqlcon

conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)
cursor = conexao.cursor()
name= input("Enter username:")
mail= input("Enter email:")
passw= input("Enter password:")
consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")

while consent !="OK":
    if consent=="termos":
        print("esses são os termos de serviço")
    elif consent=="privacy":
        print("essa é a politica de privacidade")
    consent= input("By typing OK button, you are creating an account, and agree to Terms of Service and Privacy Policy:")
if consent == "OK":
    comando=f"insert into bdinfosecurity.user (username, usermail, userpassword) values ('{name}', '{mail}', '{passw}')"
    print("print")
    print(comando)
    cursor.execute(comando)
    conexao.commit()
    resultado=cursor.fetchall()
    print(resultado)
    cursor.close()
    conexao.close()