import sqlite3
#Função para criar o banco de dados e a tabela
def create_db():
    connection = sqlite3.connect('condominio.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservas
                (id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                bloco TEXT NOT NULL,
                apartamento TEXT NOT NULL,
                local TEXT NOT NULL,
                data TEXT NOT NULL)''')
    connection.commit()
    connection.close()

# Criação do banco de dados ao iniciar o aplicativo
create_db()