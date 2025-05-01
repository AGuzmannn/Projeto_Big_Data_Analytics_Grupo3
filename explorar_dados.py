## IMPORTANTE TER INSTALADO O PANDAS E O PYARROW
# CASO NÃO TENHA RODE ESSE COMANDO NO TERMINAL: pip install pandas pyarrow

import pandas as pd

# Nome do arquivo .parquet (pode ser alterado conforme necessário)
nome_arquivo = 'exp_completa_filtrado'

extensao_arquivo = '.parquet'

arquivo_completo = nome_arquivo + extensao_arquivo

# Caminho para o arquivo .parquet
caminho_arquivo = f'Projeto_Big_Data_Analytics_Grupo3/Tabelas/{arquivo_completo}'

# Ler o arquivo .parquet
df = pd.read_parquet(caminho_arquivo)

# Exibir o conteúdo do arquivo
print(df)
