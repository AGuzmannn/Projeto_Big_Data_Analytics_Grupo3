# Tabela Gold - Comércio Exterior Brasil (Exportação)
Com base na descrição detalhada das tabelas e seus respectivos campos, podemos criar uma tabela gold que centralize os dados relevantes para análise de comércio exterior, considerando as exportações de mercadorias. Uma tabela gold tem como objetivo reunir as informações mais relevantes, de forma otimizada, para facilitar a análise e a criação de relatórios.


## Descrição dos Campos:
CO_ANO: Ano da transação comercial (1997-2021).

CO_MES: Mês da transação comercial (1-12).

CO_NCM: Código NCM que classifica o produto de acordo com a Nomenclatura Comum do Mercosul (exemplo: 9012100).

NO_NCM_POR: Descrição do NCM em português.

CO_UNID: Código de unidade de medida estatística (exemplo: quilograma, metro, tonelada).

NO_UNID: Nome da unidade de medida estatística (exemplo: Quilograma, Metro, Litro).

SG_UNID: Sigla da unidade de medida (exemplo: KGL para quilograma líquido).

CO_PAIS: Código do país com o qual foi realizada a transação comercial (exportação).

NO_PAIS: Nome do país (exemplo: Afeganistão, Espanha).

CO_VIA: Código do meio de transporte utilizado (exemplo: 1 para transporte marítimo).

NO_VIA: Nome do meio de transporte (exemplo: Marítima, Ferroviária).

CO_URF: Código da Unidade da Receita Federal responsável pelo desembaraço aduaneiro.

NO_URF: Nome da Unidade da Receita Federal.

SG_UF_NCM: Sigla da Unidade Federativa (UF) de origem (para exportação).

QT_ESTAT: Quantidade do produto em unidades estatísticas, com base no NCM e unidade de medida (exemplo: quilograma, dúzias, pares).

KG_LIQUIDO: Peso líquido da mercadoria em quilogramas (desconsiderando embalagens).

VL_FOB: Valor FOB (Free On Board) da mercadoria em dólares americanos.


## Considerações para a Tabela Gold:
Integração de Dados: As tabelas são relacionadas através dos campos CO_NCM, CO_PAIS, CO_UNID, CO_VIA, CO_URF, etc. Esses campos serão usados para associar e cruzar informações de diferentes fontes (mercadorias, países, unidades de medida, transporte, etc.).

Qualidade e Consistência: A tabela gold deve garantir que as informações sejam consistentes, como a descrição de NCMs e países, bem como unidades de medida padronizadas.

Otimização para Relatórios: O modelo final da tabela pode ser otimizado para relatórios de análise, como: volume de exportação por país, por meio de transporte, ou por produto (NCM).

Agregações: A tabela permite agregações por ano, mês, país, ou NCM para criar relatórios como total exportado, peso total, e valores FOB.

Com esse modelo, podemos facilmente consultar e analisar os dados de comércio exterior com foco na quantidade, valor e características das mercadorias exportadas no Brasil.