import mysql.connector as sqlcon

conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)


confirm= input("Tem certeza que deseja excluir esse dado? ele não poderá ser restaurado... ")
if(confirm=="sim"):
    try:
        name= input("Enter username:")
        passw= input("Enter password:")
        validate = conexao.cursor()
        comando=f"select * from bdinfosecurity.user where user.username = '{name}' and user.userpassword = '{passw}'"
        validate.execute(comando)
        resultado=validate.fetchall()
        validate.close()
        print("resultado")
        print(resultado)
        if(resultado !="[]"):
            deleter = conexao.cursor()
            ID = input("ID do usuario a ser excluido:")
            comando=f"delete from bdinfosecurity.user where user.userid = '{ID}'"
            deleter.execute(comando)
            conexao.commit()
            resultado=deleter.fetchall()
            deleter.close()
            conexao.close()

            print("dado excluido")
        else:
            print("acesso negado")
    except:
        validation = None
        print("acesso negado")
else:
    print("processo encerrado")
