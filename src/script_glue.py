
# Script de tratamento de dados no AWS Glue.

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# setup de variaveis do glue e spark 
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# caminho dos arquivos brutos e do resultado final 
path_s3 = "s3://codecafe-bi-analyses-csv/dados-brutos/"
final_path_s3 = "s3://codecafe-bi-analyses-csv/dados-completos-para-analise/"

# carrega os dados dos arquivos de csv
exp_completa = spark.read.format("csv").option("header", "true").load(path_s3+"exp_completa.csv")
co_ncm = spark.read.format("csv").option("header", "true").load(path_s3+"co_ncm.csv")
co_pais = spark.read.format("csv").option("header", "true").load(path_s3+"co_pais.csv")
co_unid = spark.read.format("csv").option("header", "true").load(path_s3+"co_unid.csv")
co_urf = spark.read.format("csv").option("header", "true").load(path_s3+"co_urf.csv")
co_via = spark.read.format("csv").option("header", "true").load(path_s3+"co_via.csv")

# filtra as linhas e colunas desejadas dos arquivos csv
exportacao_cafe = exp_completa[exp_completa["CO_NCM"].isin(["9012100", "9012200"])] # 20.000.000 para 12000
co_ncm_limpo = co_ncm.select("CO_NCM", "NO_NCM_POR")
co_pais_limpo = co_pais.select("CO_PAIS", "NO_PAIS")

# realiza a juncao dos arquivos csv baseado nos respectivos colunas_selecionadas_co_pais
exp_cafe_completo = (
    exportacao_cafe
    .join(co_ncm_limpo, on="CO_NCM", how="inner")
    .join(co_pais_limpo, on="CO_PAIS", how="inner")
    .join(co_unid, on="CO_UNID", how="inner")
    .join(co_urf, on="CO_URF", how="inner")
    .join(co_via, on="CO_VIA", how="inner")
)

# seleciona o numero de particionamentos do csv de resultado
exportacao_cafe_final = exp_cafe_completo.coalesce(1)

# salva o csv de resultado no s3
exportacao_cafe_final.write.option("header",True).mode("overwrite").csv(final_path_s3)

job.commit()
