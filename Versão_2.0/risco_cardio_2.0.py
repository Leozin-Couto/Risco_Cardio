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

# Normaliza os dados para o modelo funcionar melhor
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

modelo = LogisticRegression()
modelo.fit(x_scaled, y)

print("=== 🫀 Avaliador de Risco Cardíaco ===\n")

try:
    idade       = int(input("Idade: "))
    pressao     = int(input("Pressão sistólica (ex: 120): "))
    colesterol  = int(input("Colesterol total (ex: 200): "))
    fumante     = int(input("Fumante? (1 = Sim / 0 = Não): "))
    imc         = float(input("IMC (ex: 25.4): "))
except ValueError:
    print("❌ Entrada inválida. Use apenas números.")
    exit()

entrada = scaler.transform([[idade, pressao, colesterol, fumante, imc]])

resultado    = modelo.predict(entrada)
probabilidade = modelo.predict_proba(entrada)[0][1] * 100  # % de risco

print("\n=== Resultado ===")
print(f"Probabilidade de risco: {probabilidade:.1f}%")

if probabilidade >= 70:
    print("❤️  Risco ALTO de ataque cardíaco. Consulte um médico!")
elif probabilidade >= 40:
    print("🟡 Risco MODERADO. Fique atento aos seus hábitos.")
else:
    print("💚 Risco BAIXO. Continue mantendo hábitos saudáveis!")