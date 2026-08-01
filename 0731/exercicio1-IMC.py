import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

janela.title("Calcular IMC")
janela.geometry("800x600")

peso_label = tk.Label(janela, text="Peso(kg):")
peso_label.pack()

peso_entrada = tk.Entry(janela)
peso_entrada.pack()

altura_label = tk.Label(janela, text="Altura(m):")
altura_label.pack()

altura_entrada = tk.Entry(janela)
altura_entrada.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

def calcular_imc():
    peso = float(peso_entrada.get())
    altura = float(altura_entrada.get())

    imc = peso / (altura * altura)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Saudável"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    resultado.config(
        text=f"Seu IMC é: {imc:.2f} \nClassificao: {classificacao}"
    )

botao_calcular = tk.Button(
    janela,
    text="Calcular",
    command=calcular_imc
    )

botao_calcular.pack()
janela.mainloop()