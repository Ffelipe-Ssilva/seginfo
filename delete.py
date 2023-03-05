import mysql.connector as sqlcon
import getpass

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
        passw=getpass.getpass(prompt="Enter password:")
        validate = conexao.cursor()
        comando=f"select * from bdinfosecurity.user where user.username = '{name}' and user.userpassword = '{passw}' and user.userrole='admin'"
        validate.execute(comando)
        resultado=validate.fetchall()
        
        for row in resultado:
            authorize=row
        if(authorize):
            idu = input("ID do usuario a ser excluido:")    
            check = conexao.cursor()
            existingquery=f"select * from bdinfosecurity.user where user.userid = {idu}"
            print("query que verifica se uxuario existe")
            print(existingquery)
            check.execute(existingquery)
            finduser=check.fetchall()
            print(finduser)
            for row in finduser:
                authorize=row
                print("autorizou ou nao depois de buscar o usuario")
                print(authorize)
            if(authorize):
                deleter = conexao.cursor()
                deletequery=f"delete from bdinfosecurity.user where user.userid = {idu}"
                print("comando")
                print(deletequery)
                deleter.execute(deletequery)
                conexao.commit()
                resultado=deleter.fetchall()
                print("achou ou nao")
                print(resultado)
                deleter.close()
                conexao.close()
                print("dado excluido")
                
            else:
                print("usuário não encontrado")
            check.close() 
        else:
            print("acesso negado")
        validate.close()
    except:
        validation = None
        print("acesso negado")
else:
    print("processo encerrado")
