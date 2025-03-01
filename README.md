# Eixo-4
Projeto de Big Data Analytics

# DADOS DE IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL
`BANCO DE DADOS`
`2025/01`

Este *repositório* contém um conjunto de dados abrangente sobre o comércio internacional do Brasil, com informações detalhadas sobre as operações de importação e exportação entre 1997 e 2021. Os dados foram extraídos do Comex Stat, uma plataforma oficial do Ministério da Indústria, Comércio Exterior e Serviços (MDIC), e foram organizados em um formato SQLite para facilitar o acesso e análise.

## Descrição do Conjunto de Dados
O conjunto de dados abrange informações de importação e exportação, incluindo dados como ano, mês, produtos (classificados pelo código NCM), valores de mercadorias, quantidades e outras variáveis relevantes.

## Estrutura dos Dados
O arquivo contém 8 tabelas organizadas em SQLite. Abaixo estão as descrições dos principais campos:

* ###### **CO_ANO:** Ano da operação comercial (1997 a 2021).
* ###### **CO_MES:** Código do mês da operação comercial (1: Janeiro a 12: Dezembro).
* ###### **CO_NCM:** Código NCM (Nomenclatura Comum Mercosul), utilizado para identificar produtos comercializados no Brasil e no Mercosul.
* ###### **CO_UNID:** Código da Unidade de Medida Estatística, utilizado para padronizar a medição dos produtos (por exemplo, quilogramas, metros, litros, pares, toneladas, etc.).
* ###### **CO_PAIS:** Código do país com o qual a operação comercial foi realizada (importação ou exportação).
* ###### **SG_UF_NCM:** Sigla da Unidade Federativa (estado) de origem (na exportação) ou destino (na importação) da mercadoria.
* ###### **CO_VIA:** Código que identifica o meio de transporte utilizado (aéreo, marítimo, rodoviário, ferroviário, entre outros).
* ###### **CO_URF:** Código da Unidade da Receita Federal, responsável pela execução dos procedimentos aduaneiros.
* ###### **QT_ESTAT:** Quantidade estatística do produto, expressa em unidades ou pesos (quilos, pares, dúzias, etc.).
* ###### **KG_LIQUIDO:** Peso líquido da mercadoria, expresso em quilogramas, desconsiderando embalagem ou outros adicionais de transporte.

* ###### **VL_FOB**: Valor FOB (Free on Board), indicando o preço da mercadoria em dólares americanos (US$) sob a modalidade FOB, onde o vendedor assume o custo de embarque e o comprador arca com o transporte e seguros pós-embarque.

### Tabelas Relacionadas
###### **NCM_UNIDADE:** Relaciona cada NCM com sua unidade estatística correspondente.
###### **CO_ANO_MES:** Tabela com o código de ano e mês das operações comerciais

## Integrantes
* Alexandre Guzmán Siácara
* Ana Paula de Moraes
* Douglas Pereira Martin
* Gustavo Zagnoli
* Lucas Mamede Pacheco Novais
* Matheus Augusto Venancio Andrade

## Orientador
* Prof. Marco Paulo
