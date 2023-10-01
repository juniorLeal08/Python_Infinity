
# FAÇA UM PROGRAMA QUE RECEBE O NOME DE UM ALUNO
# RECEBE 4 NOTAS DESSE ALUNO
# E MOSTRA NA TELA QUAL FOI A MÉDIA DAS NOTAS
# E TAMBÉM MOSTRE UM TEXTO DA COR VERDE ESCRITO "APROVADO"
# SE A MÉDIA FOR MAIOR OU IGUAL A 6 E UM TEXTO VERMELHO ESCRITO
# "REPROVADO" SE A NOTA FOR ABAIXO DE 6

from tkinter import * 

def cal_media():
    nota01 = int(nota01_entry.get())
    nota02 = int(nota02_entry.get())
    nota03 = int(nota03_entry.get())
    nota04 = int(nota04_entry.get())

    media = (nota01 + nota02 + nota03 + nota04)/4 
    
    if media >= 6:
        resultado.config(text=f"{aluno_entry.get()} foi aprovado com média:{media}",fg="green")
    else:
        resultado.config(text=f"{aluno_entry.get()} foi REPROVADO com média:{media}",fg="red")
        

janela = Tk()

titulo = Label(text="BOLETIN")
titulo.pack()

nome_aluno = Label(text="Nome do Aluno: ").pack()

aluno_entry = Entry()
aluno_entry.pack()

nota01_label = Label(text=" Nota01: ").pack()
nota01_entry = Entry()
nota01_entry.pack()

nota02_label = Label(text=" Nota02: ").pack()
nota02_entry = Entry()
nota02_entry.pack()

nota03_label = Label(text=" Nota03: ").pack()
nota03_entry = Entry()
nota03_entry.pack()

nota04_label = Label(text=" Nota04: ").pack()
nota04_entry = Entry()
nota04_entry.pack()

calcular_media = Button(janela,text="Calculando a Media: ",command=cal_media)
calcular_media.pack()

resultado = Label(text="")
resultado.pack()


janela.mainloop()




