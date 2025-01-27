import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Simulando um dataset de COVID-19
data = {
    "Date": pd.date_range(start="2025-01-01", periods=30, freq="D"),
    "Country": ["Brasil"] * 30,
    "Confirmed": [
        1000, 1200, 1400, 1800, 2000, 2300, 2500, 2700, 3000, 3300,
        3700, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000,
        8500, 9000, 9700, 10500, 11000, 11500, 12000, 13000, 14000, 15000
    ],
    "Deaths": [
        20, 25, 30, 40, 50, 55, 60, 65, 70, 75,
        80, 90, 100, 120, 130, 140, 150, 160, 170, 180,
        190, 200, 210, 220, 230, 250, 270, 300, 320, 350
    ],
    "Recovered": [
        200, 250, 300, 400, 500, 600, 700, 800, 900, 1000,
        1100, 1300, 1500, 1800, 2000, 2300, 2600, 3000, 3300, 3700,
        4000, 4500, 5000, 5500, 6000, 6700, 7400, 8200, 9000, 10000
    ],
    "Vaccinated": [
        100, 200, 400, 700, 1000, 1500, 2000, 2500, 3000, 3700,
        4500, 5000, 5700, 6500, 7500, 8500, 9500, 11000, 12000, 13500,
        15000, 17000, 19000, 21000, 23000, 26000, 30000, 35000, 40000, 45000
    ],
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Estatísticas básicas
total_confirmed = df["Confirmed"].iloc[-1]
total_deaths = df["Deaths"].iloc[-1]
total_recovered = df["Recovered"].iloc[-1]
total_vaccinated = df["Vaccinated"].iloc[-1]

print(f"Total de casos confirmados: {total_confirmed}")
print(f"Total de mortes: {total_deaths}")
print(f"Total de recuperados: {total_recovered}")
print(f"Total de vacinados: {total_vaccinated}")

# Taxa de letalidade
fatality_rate = (total_deaths / total_confirmed) * 100
print(f"Taxa de letalidade: {fatality_rate:.2f}%")

# Visualizações
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Confirmed"], label="Casos Confirmados", marker="o")
plt.plot(df["Date"], df["Deaths"], label="Mortes", marker="x")
plt.plot(df["Date"], df["Recovered"], label="Recuperados", marker="s")
plt.plot(df["Date"], df["Vaccinated"], label="Vacinados", marker="d")
plt.xlabel("Data")
plt.ylabel("Número de Pessoas")
plt.title("COVID-19 no Brasil - Evolução")
plt.legend()
plt.grid()
plt.show()

# Análise de casos diários
df["New_Cases"] =  df["Confirmed"].diff().fillna(0)
df["New_Deaths"] = df["Deaths"].diff().fillna(0)

# Gráfico de barras - Novos casos e mortes diários
plt.figure(figsize=(12, 6))
sns.barplot(x=df["Date"], y=df["New_Cases"], color="blue", label="Novos Casos")
sns.barplot(x=df["Date"], y=df["New Deaths"], color="red", label="Novas Mortes")
plt.xticks(rotation=45)
plt.title("Novos Casos e Mortes Diários")
plt.xlabel("Data")
plt.ylabel("Quantidade")
plt.legend()
plt.show()

# Taxa de recuperação
recovery_rate = (total_recovered / total_confirmed) * 100
print(f"Taxa de recuperação: {recovery_rate:.2f}%")

