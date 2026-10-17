import tkinter as tk
from tkinter import ttk
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# [idade, pressão sistólica, colesterol, fumante (1=sim), IMC]
x = [
    [30, 110, 180, 0, 22.1],
    [35, 120, 195, 0, 24.3],
    [18, 105, 160, 0, 20.5],
    [40, 135, 220, 1, 27.8],
    [45, 145, 240, 1, 30.2],
    [80, 170, 280, 1, 28.9],
    [65, 160, 260, 0, 31.5],
    [16, 100, 155, 0, 19.8],
    [55, 150, 250, 1, 33.1],
    [60, 165, 270, 1, 35.4],
    [48, 140, 230, 1, 29.6],
    [52, 155, 245, 0, 32.0],
    [38, 125, 205, 0, 25.7],
    [70, 168, 275, 1, 30.8],
    [42, 138, 215, 1, 28.3],
    [25, 112, 175, 0, 21.9],
    [33, 118, 190, 0, 23.5],
    [58, 158, 255, 1, 34.2],
    [47, 142, 235, 0, 27.1],
    [63, 162, 265, 1, 36.0],
]

y = [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

modelo = LogisticRegression()
modelo.fit(x_scaled, y)

def resposta ():
    idade = int(entrada_idade.get())
    resultado = modelo.predict([[idade]])
    if resultado[0] == 1:
        mensagem_label['text'] = " Risco alto de ter um ataque cardíaco"
        mensagem_label['fg'] = "red"
    else:
        mensagem_label['text'] = " Risco baixo de ter um ataque cardíaco"
        mensagem_label['fg'] = "green"
    return



janela = tk.Tk()
janela.title("Risco Cardio")
janela.geometry("520x380")
janela.configure(bg="#2b2b2b")

titulo = tk.Label(janela, text="Teste de Risco de Ataque Cardíaco\n", font=("default", 12),bg="#2b2b2b" , fg="#EBE5DA")
titulo.place(x=20, y=10, width=480, height=30)

texto = tk.Label(janela, text="Digite sua Idade:", font=("default", 11),bg="#2b2b2b" , fg="#EBE5DA")
texto.place(x=60, y=50, width=110, height=30)

entrada_idade = tk.Entry(janela)
entrada_idade.grid(column=1, row=1)
entrada_idade.place(x=185, y=52, width=150, height=28)

botao = tk.Button(janela, text="Calcular", command=resposta)
botao.place(x=195, y=100, width=130, height=30)

mensagem_label = tk.Label(janela, text="Resultado vai aparecer aqui", font=("default", 12),bg="#2b2b2b" , fg="#EBE5DA")
mensagem_label.place(x=80, y=175, width=360, height=30)




janela.mainloop()
