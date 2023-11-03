import tkinter as tk

def converter():
    try:
        cm = float(entry_cm.get())
        metros = cm / 100
        label_resultado.config(text=f"{cm} Centimetros Equevalem Á {metros} Metros. ")
    except ValueError:
        label_resultado.config(text="Por Favor Insira Um Numero Valido.")

root = tk.Tk()
root.title("Conversor de Centimetros Para Metros")

label_cm = tk.Label(root, text="Digite O Valor Em Centimetros: ")
label_cm.pack()

entry_cm = tk.Entry(root)
entry_cm.pack()

button_Converter = tk.Button(root,text="Converter",command=converter)
button_Converter.pack()

label_resultado = tk.Label(root,text="")
label_resultado.pack()

root.mainloop()