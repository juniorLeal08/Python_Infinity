from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.geometry("460x620")

numero1 = ""
numero2 = ""
operacao = ""
resultado = 0


def registrar_operacao(op):
    global operacao
    operacao = op
    resultado_tela.config(text=f"{numero1}{operacao}")

def registrar_numero(numero):
    global numero1
    global numero2
    if operacao =="":
        numero1 = f"{numero1}{numero}"
        resultado_tela.config(text=numero1)
    else:
        numero2 = f"{numero2}{numero}"
        resultado_tela.config(text=f"{numero1}{operacao}{numero2}")

def calcular():
    global resultado
    global numero1
    global numero2

    numero1_sem_espaco = numero1.strip()
    numero1_float = float(numero1_sem_espaco)

    numero2_sem_espaco = numero2.strip()
    numero2_float = float(numero2_sem_espaco)

    if operacao == "/":
        resultado = numero1_float / numero2_float
    elif operacao == "*":
        resultado = numero1_float * numero2_float
    elif operacao == "+":
        resultado = numero1_float + numero2_float
    elif operacao == "-":
        resultado = numero1_float - numero2_float
    resultado_tela.config(text=resultado)

    





















