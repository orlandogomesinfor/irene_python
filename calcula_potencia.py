#https://www.youtube.com/watch?v=SPiq6S5qARw&t=206s
import tkinter as tk
from tkinter import ttk

#Criar Janela
janela = tk.Tk()
janela.title("Captura numeros")


def calcular_potencia():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 ** num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text=f"Erro: insira valores validos")

#Criar entry e label para o primeiro numero
label_num1 = ttk.Label(janela, text="Numero 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_num1 = ttk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

#Criar entry e label para o segundo numero
label_num2 = ttk.Label(janela, text="Numero 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_num2 = ttk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

#botao para efetuar o calaculo
botao_calcular = ttk.Button(janela, text="Calcular", command=calcular_potencia)
botao_calcular.grid(row=2, columnspan=2, padx=10, pady=10)

#label para resultado
label_resultado = ttk.Label(janela, text="")
label_resultado.grid(row=3, columnspan=2, padx=10, pady=5)

#iniciar loop
janela.mainloop()