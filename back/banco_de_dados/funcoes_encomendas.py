import sys
import os
import sqlite3
from tkinter import messagebox
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_path)
from back.entry.validar_entry import *


def inserir_encomenda(nome, data_entrega, bloco, apartamento, porteiro):
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_data_nascimento(data_entrega):
        messagebox.showerror("Erro", "Data de entrega inválida. Deve estar no formato DDMMAAAA.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return
    if not validar_nome(porteiro):
        messagebox.showerror("Erro", "Nome do porteiro inválido. Deve conter apenas letras e até 50 caracteres.")
        return

    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO encomenda (nome, data_entrega, bloco, apartamento, porteiro)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, data_entrega, bloco, apartamento, porteiro))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Encomenda inserida com sucesso.")

def pesquisar_encomenda(nome, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nome, bloco, apartamento, porteiro, data_entrega, id
        FROM encomenda
        WHERE nome = ? AND bloco = ? AND apartamento = ?
        ORDER BY data_entrega ASC
    """, (nome, bloco, apartamento))  # Forneça os três valores aqui
    dados_encomenda = cursor.fetchall()
    conn.close()
    return dados_encomenda

def pesquisar_encomenda_antigas(nome, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM encomendas_antigas
        WHERE nome = ? AND bloco = ? AND apartamento = ?
        ORDER BY data_entrega ASC
        """, (nome, bloco, apartamento))# Forneça os três valores aqui
    dados_encomenda_antigas = cursor.fetchall()
    conn.close()
    return dados_encomenda_antigas


def inserir_informacoes_encomendas_antigas(nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou):
    # Conectar ao banco de dados
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    
    # Criar um cursor para executar consultas SQL
    cursor = conn.cursor()
    
    # Inserir os dados na tabela encomenda_antigas
    cursor.execute('''INSERT INTO encomenda_antigas (nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (nome, apartamento, bloco, data_entrega, data_retirada, porteiro, cpf, nome_de_quem_retirou))
    
    # Commit para salvar as alterações no banco de dados
    conn.commit()
    
    # Fechar a conexão com o banco de dados
    conn.close()

