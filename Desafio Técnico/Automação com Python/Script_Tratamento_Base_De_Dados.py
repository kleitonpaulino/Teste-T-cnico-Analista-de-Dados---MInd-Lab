import pandas as pd
import numpy as np

# Leitura dos dados a partir de um arquivo CSV
df = pd.read_csv('C:\\Users\\Kleiton\\Desktop\\Desafio Técnico\\Automação com Python\\dados_financeiros.csv', sep=';', decimal='.', dtype=str)

# Verificação de dados carregados
print(df.head())

# Limpeza e formatação da coluna 'Valor' para conversão dos dados para o formato numérico
df['Valor'] = df['Valor'].str.strip() # Remover espaço em branco
df['Valor'] = df['Valor'].str.replace(',', '.', regex=False) # Substitui todas as virgulas por ponto para padronizar o separador decimal
df['Valor'] = df['Valor'].str.replace(r'[^0-9.]', '', regex=True) # Remove todos os caracteres qeu não sejam número ou ponto
df['Valor'] = df['Valor'].str.replace('.', '', n=1, regex=False)  # Remove o ponto na casa do milhar
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce') # Converte a coluna para numérico
# Remover linhas com valores faltantes em 'Valor' ou que não puderam ser convertidas para numérico por algum motivo
df = df.dropna(subset=['Valor'])

# Ajustar a linha da coluna categoria com o valor 'Receitx' apra 'Receita'
df.loc[df['Categoria'] == 'Receitx', 'Categoria'] = 'Receita'

# Processar a coluna 'Data' para garantir que as datas estejam no formato dia/mês/ano
for index, row in df.iterrows():
    temp = row['Data'].split('/') # Separa os valores da data 
    
    # Verifica o formato da data
    if len(temp) == 3:
        if len(temp[1]) == 2 and int(temp[1]) > 12:  # Dia como mês
            valor = temp.pop(1)
            temp.insert(0, valor)  # Move o dia para o início
        if len(temp[2]) == 2 and int(temp[2]) > 12:  # Dia como ano
            valor = temp.pop(2)
            temp.insert(0, valor)  # Move o dia para o início
        if len(temp[0]) == 4:  # Ano em formato de dia
            valor = temp.pop(0)
            temp.append(valor)  # Adiciona o ano no final
        if len(temp[1]) == 4:  # Ano em formato de mês
            valor = temp.pop(1)
            temp.append(valor)  # Adiciona o ano no final
    
    # Atualiza a linah da coluna 'Data' com o valor ajustado
    df.at[index, 'Data'] = '/'.join(temp)
    
# Converte apra o formato data    
df['Data'] = pd.to_datetime(df['Data'], errors='coerce', format='%d/%m/%Y')

# organizar os dados com base na data
df = df.sort_values(by='Data')

# Verificação dos dados tratados
print(df.head())

# Salvar o DataFrame limpo em um novo CSV
df.to_csv('C:\\Users\\Kleiton\\Desktop\\Desafio Técnico\\Automação com Python\\Base_dados_financeiros_tratada.csv', index=False, sep=";")
