import tkinter as tk 

def salvar_mome():
    nome= entrada.get()
    lbl_nome_salvo.config(text="nome salvo: " + nome)

janela= tk.Tk()
janela.title("Meu aplicativo")
janela.geometry("300x700")
janela.config(bg="lightblue")

lbl_nome =tk.Label(janela, text="nome")
lbl_nome.config(font="arial, 12")

