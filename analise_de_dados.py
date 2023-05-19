# Passo 1: Importar a base de dados

import pandas as pd
import plotly.express as px

tabela = pd.read_csv("clientes.csv", encoding = "latin", sep = ";")

# Deletar colunas inúteis
# axis = 0 -> deletar uma linha, axis = 1 -> deletar uma coluna

tabela = tabela.drop("Unnamed: 8", axis=1)

# Passo 2: Visualizar a base de dados
    # Entender as informações disponíveis
    # Procurar os problemas da base de dados
    
print("tabela")
      
    
# Passo 3: Tratamento de dados
    # Valores e formatos errados

tabela["Salário Anual (R$)"] = pd.to_numeric(["Salário Anual (R$)"], errors="coerce")

    # Valores vazios

tabela = tabela.dropna()
print(tabela.info())
    
print("tabela.info()")    
    
    
    
# Passo 4: Análise inicial dos dados

print("tabela.describe()")

# Passo 5: Análise completa dos dados
    # criar gráfico
for coluna in tabela.coluns:
    grafico = px.histogram(tabela, x= "Salário Anual (R$)", y="Nota (1-100)", histfunc="avg", text_auto= True, nbins=10)
    grafico.show()

