import sys
import os
import sqlite3
from tkinter import messagebox
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_path)
from back.entry.validar_entry import *


def buscar_visitantes(nome_morador):
    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT nome_visitante, horario1, horario2, data
    FROM visitantes
    WHERE nome_morador = ?
    ''', (nome_morador,))
    visitantes = cursor.fetchall()
    conn.close()
    return visitantes
