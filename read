import mysql.connector as sqlcon

conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)
cursor = conexao.cursor()
comando='select * from bdinfosecurity.sell'
cursor.execute(comando)
resultado=cursor.fetchall()
print(resultado)
cursor.close()
conexao.close()
