# Exemplo de Notebook PySpark para Transformação de Dados no Microsoft Fabric Lakehouse

# Este script simula um processo de ETL comum em um notebook do Fabric.
# Ele lê dados brutos (bronze), aplica transformações para criar uma tabela limpa (silver),
# e depois agrega os dados para criar uma tabela de resumo (gold).

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, when, year, month, dayofmonth

# Em um notebook real do Fabric, a sessão Spark já é criada automaticamente como 'spark'.
# spark = SparkSession.builder.appName("ExemploTransformacao").getOrCreate()

# --- 1. Leitura da Camada Bronze ---
# Suponha que temos uma tabela 'vendas_brutas' no Lakehouse, carregada por um pipeline.
# Vamos criar um DataFrame de exemplo para simular isso.
data_bruta = [
    (1, "2025-10-01", 101, 1, 150.00, None),
    (2, "2025-10-01", 102, 2, 25.50, "SP"),
    (3, "2025-10-02", 101, 1, 150.00, "RJ"),
    (4, "2025-10-02", 103, 3, 99.99, "MG"),
    (5, "2025-10-03", 102, 2, 25.50, "SP"),
    (6, "2025-10-03", 101, 5, None, "RJ"), # Preço nulo
    (7, "2025-10-03", 104, 1, 75.00, "BA"),
    (2, "2025-10-01", 102, 2, 25.50, "SP") # Registro duplicado
]
columns = ["id_venda", "data_venda", "id_cliente", "id_produto", "valor", "estado"]
df_bronze = spark.createDataFrame(data_bruta, columns)

# Em um notebook real, você leria a tabela diretamente:
# df_bronze = spark.read.table("meu_lakehouse.vendas_brutas")

print("--- Dados Brutos (Bronze) ---")
df_bronze.show()

# --- 2. Transformação para a Camada Silver ---
# - Remover duplicatas
# - Tratar valores nulos (preencher preço médio)
# - Enriquecer dados (adicionar colunas de ano, mês, dia)

# Calcular o preço médio para preencher os nulos
preco_medio = df_bronze.select(avg(col("valor"))).first()[0]

df_silver = df_bronze.distinct() \
    .withColumn("valor_tratado", when(col("valor").isNull(), preco_medio).otherwise(col("valor"))) \
    .withColumn("ano", year(col("data_venda"))) \
    .withColumn("mes", month(col("data_venda"))) \
    .withColumn("dia", dayofmonth(col("data_venda"))) \
    .drop("valor") # Remove a coluna original com nulos

print("--- Dados Limpos e Enriquecidos (Silver) ---")
df_silver.show()

# Salvar a tabela Silver no Lakehouse
# df_silver.write.mode("overwrite").format("delta").saveAsTable("meu_lakehouse.vendas_silver")

# --- 3. Agregação para a Camada Gold ---
# Criar uma tabela agregada com o total de vendas e a média por cliente e estado.

df_gold = df_silver.groupBy("id_cliente", "estado") \
    .agg(
        count("id_venda").alias("total_vendas"),
        avg("valor_tratado").alias("valor_medio_venda")
    )

print("--- Dados Agregados para Análise (Gold) ---")
df_gold.show()

# Salvar a tabela Gold no Lakehouse ou Data Warehouse
# df_gold.write.mode("overwrite").format("delta").saveAsTable("meu_lakehouse.vendas_agregadas_gold")

# Para escrever no Data Warehouse:
# df_gold.write.mode("overwrite").format("delta").saveAsTable("meu_warehouse.dbo.vendas_agregadas_gold")
