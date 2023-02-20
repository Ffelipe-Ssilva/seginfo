import mysql.connector as sqlcon

conexao = sqlcon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bdinfosecurity',
)
cursor = conexao.cursor()
produto ='pedra redonda'
valor=600000
comando=f"delete from bdinfosecurity.sell where sellprod = '{produto}'"
cursor.execute(comando)
conexao.commit()
resultado=cursor.fetchall()
cursor.close()
conexao.close()
