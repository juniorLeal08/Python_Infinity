# Login E Senha

import tkinter as tk

def fazer_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if len(senha) > 6 and '@' in email:
        label_resultado.config(text="Login Bem Sucedido!")
    else:
        label_resultado.config(text="Login Falhou.Verifique E Tente Novamente. ")

root = tk.Tk()
root.title("Tela De Login")

label_email = tk.Label(root,text="E-mail:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

label_senha = tk.Label(root,text="Senha (minimo 6 digitos):")
label_senha.pack()

entry_senha = tk.Entry(root,show="*")
entry_senha.pack()

button_login = tk.Button(root,text="Login:",command=fazer_login)
button_login.pack()

label_resultado = tk.Label(root,text="")
label_resultado.pack()

root.mainloop()