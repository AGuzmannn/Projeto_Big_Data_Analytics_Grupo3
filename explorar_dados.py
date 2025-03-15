## IMPORTANTE TER INSTALADO O PANDAS E O PYARROW
# CASO NÃO TENHA RODE ESSE COMANDO NO TERMINAL: pip install pandas pyarrow

import pandas as pd

# Caminho para o arquivo .parquet
caminho_arquivo = 'Projeto_Big_Data_Analytics_Grupo3\Tabelas\exp_completa_filtrado.parquet'

# Ler o arquivo .parquet
df = pd.read_parquet(caminho_arquivo)

# Exibir o conteúdo do arquivo
print(df)
