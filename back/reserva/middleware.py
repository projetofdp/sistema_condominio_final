# Criação do banco de dados ao iniciar o aplicativo
from back.reserva.queries import reservar
from tkinter import messagebox



def check_reserva(nome, bloco, apartamento, local, data):
    validar_nome = verify_empty(nome)
    validar_bloco = verify_empty(bloco)
    validar_apartamento = verify_empty(apartamento)
    funcao_verify_local = verify_local(local)
    validar_entrada = validar_entry(nome,bloco,apartamento)
    check_all = validar_nome[0] +  validar_bloco[0] + funcao_verify_local[0] + validar_apartamento[0] + validar_entrada[0]
    


    # for item in funcao_verify_local:
    #     if item[0] is False: 
    #         return item[1]
    #     pass

    if check_all >= 4:
        reservar(nome, bloco, apartamento, local, data)              
        msg =  "Reservado"
        return msg
    # return (funcao_verify_local[1])
    return "Opss Erro :("
    
def verify_local(local):
    msg = [False, f"{local} não é válido."]
    lista_local = ["Salão de Festas", "Piscina", "Quadra de Tênis", "Spa", "Espaço Gourmet", "Churrasqueira", "Quadra de Futebol"]
    if local in lista_local:
        return([True])
    #return msg
    return(False)

def verify_empty(value):
    msg = [False, "todos os campos devem ser preenchidos."]
    if len(value) > 0:
        return([True])
    return msg

def validar_entry(nome, bloco, apartamento):
    
    if not nome.isalpha():
        return ([False, "O nome deve conter apenas letras"])
    
    if not bloco.isalpha() or len(bloco) != 1:
        return ([False, "O bloco deve ser composto por apenas uma letra"])
    
    if not apartamento.isdigit() or len(apartamento) > 3:
        return([False, "O número do apartmento deve ser composto apenas por números e ter no máximo 3 dígitos."])

    return(True, "Validação bem-sucedida.")

