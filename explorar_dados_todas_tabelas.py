import pandas as pd

# Caminho para os arquivos .parquet
caminho_base = 'Projeto_Big_Data_Analytics_Grupo3/Tabelas_renomeadas_por_numeros/'

# Loop para ler e imprimir todos os arquivos .parquet
for i in range(1, 8): 
    nome_arquivo = str(i)
    extensao_arquivo = '.parquet'
    arquivo_completo = nome_arquivo + extensao_arquivo  # Nome completo do arquivo
    caminho_arquivo = caminho_base + arquivo_completo  # Caminho completo do arquivo
    
    # Ler o arquivo .parquet
    df = pd.read_parquet(caminho_arquivo)
    
    # Exibir o conteúdo do arquivo
    print(f"Conteúdo do arquivo {arquivo_completo}:\n")
    print(df)
    print("\n" + "="*120 + "\n")  # Separador entre os arquivos
