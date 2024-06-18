import sys
import subprocess
import os
import json
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from tkcalendar import DateEntry
project_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_path))

from back.reserva import middleware
from back.reserva.queries import pesquisar_reservas

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = Path(script_dir).parents[0]  # Isto assumindo que 'dashboard' está dentro de 'interface'

# Defina OUTPUT_PATH como a raiz do projeto
OUTPUT_PATH = project_root
ASSETS_PATH = os.path.join(script_dir, "assets", "frame0")

def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)

def voltar():
    script_path = os.path.join(OUTPUT_PATH, "dashboard", "dashboard_i.py")
    args = [sys.executable, script_path]
    subprocess.run(args)
    window.destroy()

def on_reservar_click():
    nome = entry_1.get()
    bloco = entry_2.get()
    apartamento = entry_3.get()
    data = sel.get()
    local = combo_places.get()

    call_db = middleware.check_reserva(nome, bloco, apartamento, local, data)
    messagebox.showinfo(message=call_db)
    limpar_campos()

def pesquisar():
    nome = entry_4.get()
    bloco = entry_5.get()
    apartamento = entry_6.get()

    if nome and bloco and apartamento:
        # Pesquisar no banco de dados
        dados_reservas = pesquisar_reservas(nome, bloco, apartamento)

        if dados_reservas:
            abrir_pesquisa(dados_reservas)
        else:
            messagebox.showinfo("Erro", "Morador não encontrado.")
    else:
        messagebox.showinfo("Erro", "Por favor, preencha todos os campos.")

def abrir_pesquisa(dados_reservas):
    print("Comprimento dos dados da reserva:", len(dados_reservas))
    if len(dados_reservas) >= 1 :
        script_path = Path(OUTPUT_PATH, "reserva", "reserva_pesquisa_I.py")
        args = [sys.executable, str(script_path),json.dumps(dados_reservas)]
        subprocess.run(args)
        window.destroy()
    else:
        messagebox.showerror("Erro", "Dados insuficientes para abrir a edição.")

def limpar_campos():
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')


window = Tk()

window.geometry("950x680")
window.configure(bg = "#FFFFFF")


canvas = Canvas( window, bg = "#FFFFFF", height = 680, width = 950, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
canvas.create_text(54.0,71.0,anchor="nw",text="Reservar",fill="#8EBC4F",font=("BeVietnamPro Medium", 45 * -1))

sel = ctk.StringVar() 
data_label = ctk.CTkLabel(canvas, text="Data (dd/mm/yyyy):",)
data_label.place(x =227, y = 280)
calendario = DateEntry(canvas, selectmode ="day", textvariable=sel)
calendario.place(x =227, y = 265)
calendario.bind("<Key>", lambda e: "break")
def my_upd(*args):
    print(sel.get())


espaco_label = ctk.CTkLabel(canvas,text="Espaços:", bg_color="#FFFFFF", fg_color="#8EBC4F")
espaco_label.place(x = 52 , y = 265)
places =["Salão de Festas","Piscina","Quadra de Tênis","Spa","Espaço Gourmet","Churrasqueira","Quadra"]
combo_places = ctk.CTkComboBox(canvas, values=places, state="readonly" ,bg_color="#FFFFFF")
combo_places.set(places[0])
combo_places.place(x = 52 , y = 265)



#voltar
button_image_1 = PhotoImage( file=relative_to_assets("button_1.png"))
button_1 = Button( image=button_image_1, borderwidth=0, highlightthickness=0, command=voltar, relief="flat")
button_1.place( x=37.0, y=27.0, width=30.0, height=15.0)

canvas.create_text(  709.0, 18.0, anchor="nw", text="reservas condomínio", fill="#B9B9B9", font=("BeVietnamPro Light", 19 * -1))

#nome reservar
canvas.create_text( 52.0, 135.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_1 = PhotoImage( file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image( 208.0, 172.66262912750244, image=entry_image_1)
entry_1 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place( x=61.0, y=157.0, width=294.0, height=29.325258255004883)

#bloco reservar
canvas.create_text( 52.0, 195.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_2 = PhotoImage( file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image( 129.5, 232.66262912750244, image=entry_image_2)
entry_2 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place( x=61.0, y=217.0, width=137.0, height=29.325258255004883)


#apartamento reservar
canvas.create_text( 227.0, 195.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_3 = PhotoImage( file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image( 304.5, 232.66262912750244, image=entry_image_3)
entry_3 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_3.place( x=236.0, y=217.0, width=137.0, height=29.325258255004883)

button_image_2 = PhotoImage( file=relative_to_assets("button_2.png"))
button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command=pesquisar, relief="flat")
button_2.place( x=664.0, y=284.0, width=112.0, height=40.78125)

button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
button_3 = Button( image=button_image_3, borderwidth=0, highlightthickness=0, command=on_reservar_click, relief="flat")
button_3.place(x=153.0, y=325.0, width=112.0, height=40.78125)

canvas.create_text( 564.0, 71.0, anchor="nw", text="Pesquisa", fill="#8EBC4F", font=("BeVietnamPro Bold", 45 * -1))

#pesquisar nome
canvas.create_text( 564.0, 149.0, anchor="nw", text="nome:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_4 = PhotoImage( file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image( 720.0, 186.66262912750244, image=entry_image_4)
entry_4 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_4.place( x=573.0, y=171.0, width=294.0, height=29.325258255004883)

#bloco pesquisar
canvas.create_text( 564.0, 208.0, anchor="nw", text="bloco:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_5 = PhotoImage( file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image( 634.0, 245.66262912750244, image=entry_image_5)
entry_5 = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_5.place( x=573.0, y=230.0, width=122.0, height=29.325258255004883)

#apartamento pesquisar
canvas.create_text( 736.0, 208.0, anchor="nw", text="apartamento:", fill="#000000", font=("BeVietnamPro SemiBold", 17 * -1))
entry_image_6 = PhotoImage( file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image( 806.0, 245.66262912750244, image=entry_image_6)
entry_6 = Entry( bd=0, bg="#FFFFFF",fg="#000716",highlightthickness=0)
entry_6.place(x=745.0,y=230.0,width=122.0,height=29.325258255004883)


window.resizable(False, False)
window.mainloop()

