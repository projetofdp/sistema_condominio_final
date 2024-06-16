import sys
import os
import sqlite3
from tkinter import messagebox
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_path)
from back.entry.validar_entry import *


def pesquisar_visitante(nome, bloco, apartamento):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.nome_visitante, v.horario1, v.horario2, v.data, v.bloco, v.apartamento, m.nome
        FROM visitantes v
        INNER JOIN moradores m ON v.morador_id = m.id
        WHERE m.nome = ? AND v.bloco = ? AND v.apartamento = ?
    """, (nome, bloco, apartamento))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def obter_informacoes_do_banco_de_dados():
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.nome_visitante, v.horario1, v.horario2, v.data, v.bloco, v.apartamento, m.nome
        FROM visitantes v
        INNER JOIN moradores m ON v.morador_id = m.id
        ORDER BY v.data ASC, v.horario1 ASC, v.horario2 ASC
    """)
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def mover_pessoa_para_antigos():
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()

    # Seleciona os dados da primeira pessoa e do morador relacionado
    cursor.execute("""
        SELECT v.id, v.nome_visitante, v.horario1, v.horario2, v.data, v.bloco, v.apartamento, m.id, m.nome
        FROM visitantes v
        INNER JOIN moradores m ON v.morador_id = m.id
        ORDER BY v.data ASC, v.horario1 ASC, v.horario2 ASC
        LIMIT 1
    """)
    pessoa = cursor.fetchone()

    if pessoa:
        visitante_id, nome_visitante, horario1, horario2, data, bloco, apartamento, morador_id, nome_morador = pessoa

        # Move os dados para a tabela visitantes_antigos
        cursor.execute("""
            INSERT INTO visitantes_antigos (morador_id, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (morador_id, nome_visitante, horario1, horario2, data, nome_morador, bloco, apartamento))

        # Remove os dados da primeira pessoa da tabela visitantes
        cursor.execute("""
            DELETE FROM visitantes 
            WHERE id = ?
        """, (visitante_id,))

        conn.commit()

    conn.close()