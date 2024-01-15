

import tkinter as tk
def exibir_mensagem():
    lbl_mensagem.config(text="pablo gay!")


#cria a janela 
janela = tk.Tk()

# define o titulo da janela 

janela.title("minha janela")
'bg'
janela.config(bg='lightblue')

#define as dimensnoes da janela 
janela.geometry("400x300")


# cria o botão

lbl_mensagem =tk.Label(janela, text="clique no botão para exibir uma mensagem")
lbl_mensagem.pack(pady=20)

btn_exibir = tk.Button(janela, text="exibir", command=exibir_mensagem)
btn_exibir.pack()

#cores e texto do botão

"""bg', 'FG' # para cor e texo
'font' 'relief' # para estilo da borda
'btn_salvar.config(bt='green'), 
fg='white', font=('arial, 12', relief=tk.RAISED)"""

# codigo 
fg:str
btn_salvar = tk.Button(janela,  text="salvar", bg="green", fg="white", font=("Arial", 12), relief=tk.RAISED)
 
btn_salvar.pack()





# O loop da janela 
janela.mainloop()

