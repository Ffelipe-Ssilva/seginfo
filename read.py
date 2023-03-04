import mysql.connector as sqlcon

conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)

try:
    name= input("Enter username:")
    passw= input("Enter password:")
    validate = conexao.cursor()
    comando=f"select user.userid from bdinfosecurity.user where user.username = '{name}' and user.userpassword = '{passw}'"
    print(comando)
    validate.execute(comando)
    idsession=validate.fetchone()
    print("ID DA SESSÃO")
    print(idsession)
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
    comando=f"insert into bdinfosecurity.accesslog (iduseracces, context) values ('{idsession}', 'combrança por email')"
    print("print")
    print(comando)
    log.execute(comando)
    conexao.commit()
    log.close()