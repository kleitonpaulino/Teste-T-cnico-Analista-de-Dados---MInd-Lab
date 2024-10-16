import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leitura dos dados tratados a partir de um arquivo CSV
df = pd.read_csv('C:\\Users\\Kleiton\\Desktop\\Desafio Técnico\\Automação com Python\\Base_dados_financeiros_tratada.csv', sep=';', decimal='.', dtype=str)

# Verificação de dados carregados
print(df.head())

# Conversão da coluna 'Data' para o formato de data
df['Data'] = pd.to_datetime(df['Data'])

# Conversão das colunas numéricas 'Valor' e 'Quantidade' para o formato float
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
df['Quantidade'] = pd.to_numeric(df['Quantidade'], errors='coerce')

# Geraçãod e uma terceira coluna com o valor de venda por unidade
df['Valor_unidade']=df['Valor']/df['Quantidade']

# Cálculo da média e do desvio padrão para o Valor
media_valor = df['Valor'].mean()
desvio_valor = df['Valor'].std()

# Cálculo da média e do desvio padrão para a Quantidade
media_quantidade = df['Quantidade'].mean()
desvio_quantidade = df['Quantidade'].std()

# Cálculo da média e do desvio padrão para o valro por unidade
media_Valor_unidade = df['Valor_unidade'].mean()
desvio_Valor_unidade = df['Valor_unidade'].std()

# Impressão dos resultados
print("\nValor:")
print(f'Média Valor: {media_valor:.2f}, Desvio Padrão Valor: {desvio_valor:.2f}\n')
print("Quantidade:")
print(f'Média Quantidade: {media_quantidade:.2f}, Desvio Padrão Quantidade: {desvio_quantidade:.2f}\n')
print("Valor por unidade:")
print(f'Média valor por unidade: {media_Valor_unidade:.2f}, Desvio Padrão valor por unidade: {desvio_Valor_unidade:.2f}\n')

# Interpretação da média e desvio padrão
if desvio_valor > media_valor * 0.3:
    print("O desvio padrão do valor é alto, indicando grande variação nos valores.")
else:
    print("O desvio padrão do valor é baixo, indicando que os valores estão mais próximos da média.")

if desvio_quantidade > media_quantidade * 0.3:
    print("O desvio padrão da quantidade é alto, indicando grande variação nas quantidades.")
else:
    print("O desvio padrão da quantidade é baixo, indicando que as quantidades estão mais próximas da média.")

if desvio_Valor_unidade > media_Valor_unidade * 0.3:
    print("O desvio padrão do valor por unidade é alto, indicando grande variação nas quantidades.")
else:
    print("O desvio padrão do valor por unidade é baixo, indicando que as quantidades estão mais próximas da média.")

# Criando uma grade de subgráficos
fig, axs = plt.subplots(3, 1, figsize=(8, 6))  # 2 linhas, 1 coluna

# Criação de gráfico de evolução do valor ao longo do tempo
axs[0].plot(df['Data'], df['Valor'], marker='o', linestyle='-', label='Valor')
axs[0].set_title('Evolução dos Valores ao Longo do Tempo')
axs[0].set_xlabel('Data')
axs[0].set_ylabel('Valor')
axs[0].legend()

# Criação de gráfico de evolução da Quantidade ao longo do tempo)
axs[1].plot(df['Data'], df['Quantidade'], marker='o', linestyle='-', label='Quantidade')
axs[1].set_title('Evolução dos Valores ao Longo do Tempo')
axs[1].set_xlabel('Data')
axs[1].set_ylabel('Quantidade')
axs[1].legend()

# Criação de gráfico de evolução do valor por unidade ao longo do tempo)
axs[2].plot(df['Data'], df['Valor_unidade'], marker='o', linestyle='-', label='Valor por unidade')
axs[2].set_title('Evolução dos Valores ao Longo do Tempo')
axs[2].set_xlabel('Data')
axs[2].set_ylabel('Valor por unidade')
axs[2].legend()


plt.tight_layout()
plt.show()

# A análise gráfica da distribuição dos dados ao longo do tempo revela que os valores não demonstram nenhuma tendência clara, seja de crescimento ou de diminuição. Essa observação é corroborada pelo alto valor do desvio padrão, que indica uma considerável variabilidade nos dados.