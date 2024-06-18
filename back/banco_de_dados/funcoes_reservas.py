def pesquisar_reserva(nome, bloco, apartamento):
    if not validar_nome(nome):
        messagebox.showerror("Erro", "Nome inválido. Deve conter apenas letras e até 50 caracteres.")
        return
    if not validar_bloco(bloco):
        messagebox.showerror("Erro", "Bloco inválido. Deve conter até 10 caracteres alfanuméricos.")
        return
    if not validar_apartamento(apartamento):
        messagebox.showerror("Erro", "Apartamento inválido. Deve conter até 4 números.")
        return

    conn = sqlite3.connect('condominio.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nome, bloco, apartamento, porteiro, data_entrega, id
        FROM reserva
        WHERE nome = ? AND bloco = ? AND apartamento = ?
        ORDER BY data_entrega ASC
    """, (nome, bloco, apartamento))  # Forneça os três valores aqui
    dados_encomenda = cursor.fetchall()
    conn.close()
    return dados_encomenda