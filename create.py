import mysql.connector as sqlcon

conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)
cursor = conexao.cursor()
produto ='pedra redonda'
valor = 2
comando=f"insert into bdinfosecurity.sell (sellprod, sellprice) values ('{produto}', {valor})"
print("print")
print(comando)
cursor.execute(comando)
conexao.commit()
resultado=cursor.fetchall()
print(resultado)
cursor.close()
conexao.close()
