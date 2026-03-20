import pandas as pd

data = pd.read_excel(r"C:\Users\micha\Desktop\25.0082\10794_PyAvan\Ex11-Pandas\ex1.xlsx", sheet_name="Folha1")
print("--- Todos os Dados ---")
print(data)
print("\n--- Apenas a Coluna Nome_Cliente ---")
dados_fich = pd.DataFrame(data, columns=["Nome_Cliente"])
print(dados_fich)