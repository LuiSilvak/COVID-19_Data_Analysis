import pandas as pd
import random
import datetime

# Função para gerar uma data inicial
def gerar_data_inicial(anos_atras=3):
    """Gera uma data inicial para simular registros desde anos passados."""
    inicio = datetime.datetime.now() - datetime.timedelta(days=anos_atras * 365)
    return inicio

# Lista com 100 países reais
lista_paises = [
    "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Arábia Saudita", "Argélia", 
    "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bahrein", "Bangladesh", "Barbados", 
    "Belarus", "Bélgica", "Belize", "Benin", "Bermudas", "Bolívia", "Bósnia e Herzegovina", "Botswana", "Brasil", 
    "Brunei", "Bulgária", "Burkina Faso", "Burundi", "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", 
    "Catar", "Cazaquistão", "Chile", "China", "Chipre", "Colômbia", "Comores", "Congo", "Coréia do Norte", 
    "Coréia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba", "Dinamarca", "Djibouti", "Dominica", 
    "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia", "Eslováquia", "Eslovênia", "Espanha", 
    "Estados Unidos", "Estônia", "Eswatini", "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", 
    "Gâmbia", "Gana", "Geórgia", "Grécia", "Grenada", "Guatemala", "Guiana", "Guiné", "Guiné-Bissau", 
    "Guiné Equatorial", "Haiti", "Holanda", "Honduras", "Hungria", "Iêmen", "Ilhas Fiji", "Índia", "Indonésia", 
    "Irã", "Iraque", "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Kiribati", 
    "Kuwait", "Laos", "Lesoto", "Letônia"
]

# Gerando dados fictícios para 200 registros
datas = [(gerar_data_inicial() + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(200)]
paises = [random.choice(lista_paises) for _ in range(200)]
casos_confirmados = [random.randint(1000, 100000) for _ in range(200)]
obitos = [random.randint(10, 5000) for _ in range(200)]
recuperados = [random.randint(500, 90000) for _ in range(200)]
vacinas = [random.randint(1000, 1000000) for _ in range(200)]

# Criando o DataFrame
df_covid_200 = pd.DataFrame({
    "Data": datas,
    "País": paises,
    "Casos_Confirmados": casos_confirmados,
    "Óbitos": obitos,
    "Recuperados": recuperados,
    "Vacinas": vacinas
})

# Salvando o arquivo CSV
df_covid_200.to_csv("exemplo_covid19.csv", index=False)

print("Arquivo 'exemplo_covid19.csv' gerado com sucesso!")


