import tkinter as tk
from tkinter import ttk
from sklearn.linear_model import LogisticRegression

x = [[30], [35], [18], [40], [45], [80], [65], [16], [34], [56]]
#1 - Teve um ataque cardiaco, 0 - Não teve um ataque cardiaco
y = [0, 0, 0, 1, 1, 1, 0, 1, 0, 1]

modelo = LogisticRegression()
modelo.fit(x,y)

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
