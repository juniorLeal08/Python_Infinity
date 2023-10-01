from tkinter import *


def saudacao():
    
    print(f"Seja Bem Vindos{nome_entrado.get()}")
    nome_entrado.delete(0,END)



janela = Tk()

titulo = Label(text="Bem Vindo",bg= "red",foreground="white")
titulo.pack()

nome_texto = Label(text="Nome")
nome_texto.pack()

nome_entrado = Entry(bg="#7593f9")
nome_entrado.pack

botao_enviar = Button(janela, text="Enviar",width=20,command=saudacao)
botao_enviar.pack()


janela.mainloop()
















