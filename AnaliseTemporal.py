import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml

# Carregar dados do arquivo YAML
with open('Projetoaula8/empresa.yaml','r') as file:
    dados = yaml.safe_load(file)

# Dados de vendas
vendas = [
    {"data": '2023-01-05', "produto": "Banheira", "quantidade": 2},
    {"data": '2023-02-12', "produto": "Ofurô", "quantidade": 1},
    {"data": '2023-03-20', "produto": "Spa", "quantidade": 3},
    # Adicione o restante dos dados aqui
]

# Converter para DataFrame do Pandas
df_vendas = pd.DataFrame(vendas)

# Extrair mês e ano da data
df_vendas['data'] = pd.to_datetime(df_vendas['data'])
df_vendas['ano'] = df_vendas['data'].dt.year
df_vendas['mes'] = df_vendas['data'].dt.month

# Agrupar por mês, ano e produto
df_vendas_agrupado = df_vendas.groupby(['ano', 'mes', 'produto']).sum().reset_index()

# Plotar gráfico de linha
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Loop sobre os produtos
for produto in df_vendas_agrupado['produto'].unique():
    df_produto = df_vendas_agrupado[df_vendas_agrupado['produto'] == produto]
    plt.plot(df_produto['mes'], df_produto['quantidade'], marker='o', label=produto)

plt.title('Evolução das Vendas por Produto')
plt.xlabel('Mês')
plt.ylabel('Quantidade Vendida')
plt.xticks(np.arange(1, 13), ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.legend()
plt.grid(True)
plt.show()
