import pandas as pd

# Carregar os arquivos Parquet
df_1 = pd.read_parquet(r's3://inputdados/co_ncm.parquet')  # Tabela de NCM
df_2 = pd.read_parquet(r's3://inputdados/co_pais.parquet')  # Tabela de Países
df_3 = pd.read_parquet(r's3://inputdados/co_unid.parquet')  # Tabela de Unidades
df_4 = pd.read_parquet(r's3://inputdados/co_urf.parquet')  # Tabela de URFs
df_5 = pd.read_parquet(r's3://inputdados/co_via.parquet')  # Tabela de Meios de Transporte
df_6 = pd.read_parquet(r's3://inputdados/exp_completa_filtrado.parquet')  # Tabela de Transações
df_7 = pd.read_parquet(r's3://inputdados/ncm_unidade.parquet')  # Tabela de Unidades

# Tabela de NCM: Selecionando as colunas de interesse (Código NCM e Nome em Português)
df_ncm = df_1[['CO_NCM', 'NO_NCM_POR']]

# Tabela de Países: Selecionando código e nome do país
df_paises = df_2[['CO_PAIS', 'NO_PAIS']]

# Tabela de Unidades: Selecionando código da unidade e nome
df_unidades = df_3[['CO_UNID', 'NO_UNID', 'SG_UNID']]

# Tabela de URFs: Selecionando código e nome da URF
df_urf = df_4[['CO_URF', 'NO_URF']]

# Tabela de Meios de Transporte: Selecionando código e nome do meio de transporte
df_vias = df_5[['CO_VIA', 'NO_VIA']]

# Tabela de Transações: Selecionando as colunas relevantes para a tabela gold
df_comercio = df_6[['CO_ANO', 'CO_MES', 'CO_NCM', 'CO_UNID', 'CO_PAIS', 'CO_VIA', 'CO_URF', 'SG_UF_NCM', 'QT_ESTAT', 'KG_LIQUIDO', 'VL_FOB']]

# Tabela de Unidades: Para garantir que as unidades de medida estão completas
df_unidades_repetidas = df_7[['CO_UNID', 'NO_UNID', 'SG_UNID']]


# Juntar a tabela de comércio com a tabela de NCM
df_comercio_ncm = pd.merge(df_comercio, df_ncm, how='left', on='CO_NCM')

# Juntar com a tabela de Países
df_comercio_pais = pd.merge(df_comercio_ncm, df_paises, how='left', left_on='CO_PAIS', right_on='CO_PAIS')

# Juntar com a tabela de Unidades
df_comercio_unid = pd.merge(df_comercio_pais, df_unidades, how='left', on='CO_UNID')

# Juntar com a tabela de Vias
df_comercio_via = pd.merge(df_comercio_unid, df_vias, how='left', on='CO_VIA')

# Juntar com a tabela de URFs
df_comercio_urf = pd.merge(df_comercio_via, df_urf, how='left', on='CO_URF')

# Juntar com a tabela de Unidades repetidas
df_comercio_final = pd.merge(df_comercio_urf, df_unidades_repetidas, how='left', on='CO_UNID', suffixes=('', '_repetida'))


# Remover colunas duplicadas ou irrelevantes
df_comercio_gold = df_comercio_final.drop(columns=['SG_UNID_repetida', 'NO_UNID_repetida'])

# Renomear as colunas para um formato mais claro e consistente
df_comercio_gold = df_comercio_gold.rename(columns={
    'NO_NCM_POR': 'Nome NCM',
    'NO_UNID': 'Nome Unidade',
    'NO_VIA': 'Nome Via',
    'NO_URF': 'Nome URF',
    'NO_PAIS': 'Nome País Destino',
    'SG_UF_NCM': 'UF Origem'
})

# Ordenar a tabela por Ano, Mês, NCM e País
df_comercio_gold = df_comercio_gold.sort_values(by=['CO_ANO', 'CO_MES', 'CO_NCM', 'CO_PAIS'])

# Filtrar para manter apenas registros com CO_NCM igual a 9012100 que seria o café
df_comercio_gold = df_comercio_gold.query('CO_NCM == 9012100')

# Resetar o índice
df_comercio_gold.reset_index(drop=True, inplace=True)

# Exibir o DataFrame final
print(df_comercio_gold)

# Salvar como CSV
df_comercio_gold.to_csv('s3://outputdados/tabela_gold_comercio_exterior.csv', index=False)
