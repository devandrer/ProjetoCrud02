import mysql.connector

class Banco():
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',   
            password = 'root',
            database = 'andre_db'
        )
        self.createTable()
    def createTable(self):
        c=self.conexao.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS tb_usuario(
            id_usuario INT AUTO INCREMENT PRIMARY KEY, 
            nome TEXT(255),
            telefone TEXT(255),
            email TEXT(255),
            usuario TEXT(255),
            senha TEXT(255))''')
        self.conexao.commit()
        c.close()
  #ANDRÉ RICARDO BORGES