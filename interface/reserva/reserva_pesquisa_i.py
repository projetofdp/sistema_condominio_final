import os
import sys
import subprocess
from pathlib import Path
import json
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
project_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_path))
from back.banco_de_dados.funcoes_visitantes import * 


script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = Path(script_dir).parents[0]  # Isto assumindo que 'dashboard' está dentro de 'interface'

# Defina OUTPUT_PATH como a raiz do projeto
OUTPUT_PATH = project_root
ASSETS_PATH = os.path.join(script_dir, "assets", "frame7")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def voltar():
    script_path = os.path.join(OUTPUT_PATH, "reserva", "reserva_cadastro_i.py")
    args = [sys.executable, script_path]
    subprocess.run(args)
    window.destroy()

def atualizar_dados_canvas(canvas,dados_reservas):
    # Limpa apenas os elementos dinâmicos do canvas
    for item in canvas.find_withtag("dinamico"):
        canvas.delete(item)

    for i, dado in enumerate(dados_reservas):
        nome = dado[0]
        local = dado[1]
        data = dado[2]
        bloco = dado[3]
        apartamento = dado[4]
        if i == 0:
            preencher_reserva1(nome, local, data, bloco,apartamento )
        elif i == 1:
            preencher_reserva2(nome, local, data, bloco, apartamento)
        elif i == 2:
            preencher_reserva3(nome, local, data, bloco, apartamento)




def preencher_reserva1(nome, data, local, bloco, apartamento):
    criar_elemetos_reserva1(canvas)
    canvas.create_text( 87.0, 152.0, anchor="nw",text=nome, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 242.0, 156.0, anchor="nw", text=local, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 87.0, 196.0, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 284.0, 196.0, anchor="nw", text=bloco, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 332.0, 196.0, anchor="nw", text=apartamento, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def preencher_reserva2(nome, data,local, bloco, apartamento):
    criar_elemetos_reserva2(canvas)
    canvas.create_text( 87.0, 305.0, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 242.0, 309.0, anchor="nw", text=local, fill="#000000", font=("BeVietnamPro Medium", 14 * -1),tags="dinamico")
    canvas.create_text( 87.0, 349.0, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1),tags="dinamico")
    canvas.create_text(284.0,349.0,anchor="nw",text=bloco,fill="#000000",font=("BeVietnamPro Medium", 14 * -1) ,tags="dinamico")
    canvas.create_text( 332.0, 349.0, anchor="nw", text=apartamento, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")

def preencher_reserva3(nome, data, local, bloco, apartamento):
    criar_elemetos_reserva3(canvas)
    canvas.create_text( 87.0, 458.0, anchor="nw", text=nome, fill="#000000", font=("BeVietnamPro MediumItalic", 14 * -1), tags="dinamico")
    canvas.create_text( 242.0, 462.0, anchor="nw", text=local, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 87.0, 502.0, anchor="nw", text=data, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 284.0, 502.0, anchor="nw", text=bloco,fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 332.0, 502.0, anchor="nw", text=apartamento, fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Condomínio")


canvas = Canvas(window,bg = "#FFFFFF",height = 680,width = 950,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=voltar,relief="flat")
button_1.place( x=69.0, y=34.0, width=30.0, height=15.0)
canvas.create_text( 724.0, 25.0, anchor="nw", text="reservas condomínio", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))

def criar_elemetos_reserva1(canvas):
    global image_image_3
    image_image_3 = PhotoImage( file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(221.0,196.0,image=image_image_3 , tags="dinamico")
    canvas.create_text(87.0, 184.0, anchor="nw", text="espaço", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 184.0,anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 87.0, 143.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 241.0, 144.0, anchor="nw", text="data", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 196.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 296.0, 196.0, anchor="nw", text="apto", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


def criar_elemetos_reserva2(canvas):
    global image_image_1
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image( 221.0, 349.0, image=image_image_1 , tags="dinamico")
    canvas.create_text( 87.0, 337.0, anchor="nw", text="horário", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 337.0, anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 87.0, 296.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 241.0, 297.0, anchor="nw", text="data", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 349.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text(296.0,349.0,anchor="nw",text="apto",fill="#000000",font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


def criar_elemetos_reserva3(canvas):
    global image_image_2
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(221.0,502.0,image=image_image_2)
    canvas.create_text( 87.0, 490.0, anchor="nw", text="espaço", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 490.0, anchor="nw", text="Unidade Vinculada", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 87.0, 449.0, anchor="nw", text="nome", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 241.0, 450.0, anchor="nw", text="data", fill="#7C7C7C", font=("BeVietnamPro Medium", 10 * -1), tags="dinamico")
    canvas.create_text( 242.0, 502.0, anchor="nw", text="bloco ", fill="#000000", font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")
    canvas.create_text( 296.0, 502.0, anchor="nw", text="apto", fill="#000000",font=("BeVietnamPro Medium", 14 * -1), tags="dinamico")


button_image_6 = PhotoImage( file=relative_to_assets("button_6.png"))
button_6 = Button( image=button_image_6, borderwidth=0, highlightthickness=0, command=lambda: print("button_6 clicked"), relief="flat")

button_6.place( x=73.0, y=77.0, width=180.0, height=40.0)

if len(sys.argv) > 1:
    dados_reserva_json = sys.argv[1]
    try:
        dados_reserva = json.loads(dados_reserva_json)
        atualizar_dados_canvas(canvas, dados_reserva)
    except json.JSONDecodeError:
        print("erro ao decodificar os dados das reservas. verifique o formato JSON.")

window.resizable(False, False)
window.mainloop()
