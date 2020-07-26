import sqlite3

conexao = sqlite3.connect('UserData.db')

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Usuário TEXT NOT NULL,
    Senha TEXT NOT NULL)
""")
print('Conectado ao Banco de Dados')
