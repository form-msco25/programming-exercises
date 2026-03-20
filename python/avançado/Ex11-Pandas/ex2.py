import pandas as pd

data = pd.read_csv("european_housing_prices_clean.csv")
print("--- Todos os Dados ---")
print(data)
print("\n--- Campo Específico: country ---")
print(data["country"])
lista_precos = data["price_index"].tolist()
print("\n--- Dados guardados em lista ---")
print(lista_precos[:10])