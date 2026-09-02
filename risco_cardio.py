from sklearn.linear_model import LogisticRegression

x = [[30], [35], [18], [40], [45], [80], [65], [16]]
y = [0, 0, 0, 1, 1, 1, 0, 1] #1 - Teve um ataque cardiaco, 0 - Não teve um ataque cardiaco

modelo = LogisticRegression()
modelo.fit(x,y)

idade = [[int(input("Informe sua idade: "))]]
resultado = modelo.predict(idade)

if resultado[0] == 1:
    print ("❤️ Risco alto de ter um ataque cardiáco")
else:
    print("💚 Risco baixo de ter um ataque cardiáco")