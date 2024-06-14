import sys
import os
import sqlite3
from tkinter import messagebox
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_path)
from back.entry.validar_entry import *

def inserir_morador(nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):

    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido. Deve conter exatamente 11 números.")
        return
    if not validar_telefone(telefone):
        messagebox.showerror("Erro", "Telefone inválido. Deve conter exatamente 11 números.")
        return
    if not validar_data_nascimento(data_nascimento):
        messagebox.showerror("Erro", "Data de nascimento inválida. Deve estar no formato DDMMAAAA.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return
    if not validar_placa_carro(placa_carro):
        messagebox.showerror("Erro", "Placa de Carro inválida. Deve conter 7 caracteres alfanuméricos.")
        return
    

    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO moradores (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Morador inserido com sucesso.")


def pesquisar_morador(nome, bloco, apartamento):
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return
    conexao = sqlite3.connect('condominio.db')
    cursor = conexao.cursor()
    query ="SELECT nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro FROM moradores WHERE nome = ? AND bloco = ? AND apartamento = ?"
    cursor.execute(query, (nome, bloco, apartamento))
    dados = cursor.fetchone()
    conexao.close()
    return dados

def editar_morador(nome, cpf, data_nascimento, telefone, bloco, apartamento, placa_carro):
    try:
        # Conectar-se ao banco de dados
        conn = sqlite3.connect("condominio.db")
        cursor = conn.cursor()

        # Query SQL para atualizar os dados do morador
        # Atualize as informações do morador no banco de dados
        cursor.execute("""
            UPDATE moradores SET 
                nome = ?, 
                bloco = ?, 
                apartamento = ?, 
                placa_carro = ?, 
                telefone = ?, 
                data_nascimento = ?
            WHERE cpf = ?
        """, (nome, bloco, apartamento, placa_carro, telefone, data_nascimento, cpf))
        
        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()
        
        return affected_rows > 0  # Retorna True se alguma linha foi afetada, caso contrário False
    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
        raise e
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise e
    
def deletar_morador(nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento):
    try:
        conn = sqlite3.connect('condominio.db')
        cursor = conn.cursor()

        # Deleta todas as informações dos moradores no banco de dados
        cursor.execute("""
            DELETE FROM moradores 
            WHERE nome = ? AND cpf = ? AND bloco = ? AND apartamento = ? AND placa_carro = ? AND telefone = ? AND data_nascimento = ?
        """, (nome, cpf, bloco, apartamento, placa_carro, telefone, data_nascimento))
        
        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()
        
        return affected_rows > 0  # Retorna True se alguma linha foi afetada, caso contrário False
    except sqlite3.Error as e:
        print(f"Erro de banco de dados: {e}")
        raise e
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise e
    