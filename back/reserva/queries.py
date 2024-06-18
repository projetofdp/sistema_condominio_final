import sys
import os
import sqlite3
from tkinter import messagebox
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_path)
from back.entry.validar_entry import *

#Função para inserir uma nova reserva no banco de dados
def reservar(nome, bloco, apartamento, local, data):
    connection = sqlite3.connect('condominio.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO reservas (nome, bloco, apartamento, local, data) VALUES (?, ?, ?, ?, ?)",
              (nome, bloco, apartamento, local, data))
    connection.commit()
    connection.close()

# Função para exibir as reservas em uma nova janela
def pesquisar_reservas(nome, bloco, apartamento):
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return

    connection = sqlite3.connect('condominio.db')
    cursor = connection.cursor()
    cursor.execute("""
        SELECT nome, local, data, bloco, apartamento 
        FROM reservas 
        WHERE nome = ? AND bloco = ? AND apartamento = ?
        ORDER BY data ASC
    """, (nome, bloco, apartamento))
    dados_reservas = cursor.fetchall()
    connection.close()
    return dados_reservas


    



