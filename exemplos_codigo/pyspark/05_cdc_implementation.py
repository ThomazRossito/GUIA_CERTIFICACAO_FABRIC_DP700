"""
Exemplo 5: Implementação de Change Data Capture (CDC)
Tópico: Ingestão e Transformação
Seção do Exame: 2 (Ingerir e Transformar)
Complexidade: Avançado
Objetivo: Processar dados de mudança (Inserts, Updates, Deletes) eficientemente
"""

from delta.tables import *
from pyspark.sql.functions import *

# ============================================================================
# 1. CONCEITO: DELTA LAKE CHANGE DATA FEED (CDF)
# ============================================================================
# CDF permite que o Delta Lake rastreie as alterações em nível de linha entre versões.
# Deve ser habilitado na tabela.

table_name = "Customers_CDC"
table_path = "Tables/Customers_CDC"

# ============================================================================
# 2. HABILITANDO CHANGE DATA FEED
# ============================================================================

# Opção A: Habilitar na criação
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        CustomerID INT,
        Name STRING,
        Status STRING
    )
    USING DELTA
    TBLPROPERTIES (delta.enableChangeDataFeed = true)
""")

# Opção B: Habilitar em tabela existente
# spark.sql(f"ALTER TABLE {table_name} SET TBLPROPERTIES (delta.enableChangeDataFeed = true)")

# ============================================================================
# 3. GERANDO MUDANÇAS (SIMULAÇÃO)
# ============================================================================

# Versão 0: Carga Inicial
spark.sql(f"INSERT INTO {table_name} VALUES (1, 'Alice', 'Active'), (2, 'Bob', 'Active')")

# Versão 1: Update
spark.sql(f"UPDATE {table_name} SET Status = 'Inactive' WHERE CustomerID = 2")

# Versão 2: Delete
spark.sql(f"DELETE FROM {table_name} WHERE CustomerID = 1")

# Versão 3: Insert
spark.sql(f"INSERT INTO {table_name} VALUES (3, 'Charlie', 'Active')")

# ============================================================================
# 4. LENDO AS MUDANÇAS (CDC READ)
# ============================================================================

print("Lendo todas as mudanças a partir da versão 0...")

# `readChangeFeed` fornece as colunas adicionais:
# - _change_type: 'insert', 'update_preimage', 'update_postimage', 'delete'
# - _commit_version: Versão da tabela onde ocorreu
# - _commit_timestamp: Data/hora da mudança

changes_df = spark.read.format("delta") \
    .option("readChangeFeed", "true") \
    .option("startingVersion", 0) \
    .table(table_name)

changes_df.select("CustomerID", "Name", "Status", "_change_type", "_commit_version").show()

# ============================================================================
# 5. PADRÃO COMUM: PROPAGAR PARA TABELA SILVER/GOLD
# ============================================================================
# Em um pipeline real, você leria apenas as MUDANÇAS desde o último processamento
# e aplicaria (MERGE) no destino.

target_table_name = "Customers_Gold"

# (Simulação da tabela destino)
# spark.sql(f"CREATE TABLE IF NOT EXISTS {target_table_name} ...")

def process_micro_batch(micro_batch_df, batch_id):
    # Separação lógica das mudanças
    inserts = micro_batch_df.filter("_change_type = 'insert'")
    updates = micro_batch_df.filter("_change_type = 'update_postimage'")
    deletes = micro_batch_df.filter("_change_type = 'delete'")
    
    # Lógica de UPSERT (Merge) simplificada
    if not micro_batch_df.isEmpty():
        delta_target = DeltaTable.forName(spark, target_table_name)
        
        (delta_target.alias("t")
         .merge(
             micro_batch_df.alias("s"),
             "t.CustomerID = s.CustomerID"
         )
         .whenMatchedDelete(condition = "s._change_type = 'delete'")
         .whenMatchedUpdateAll(condition = "s._change_type != 'delete'")
         .whenNotMatchedInsertAll(condition = "s._change_type != 'delete'")
         .execute()
        )

# Exemplo de uso com Streaming:
# stream = spark.readStream.format("delta") \
#     .option("readChangeFeed", "true") \
#     .option("startingVersion", "latest") \
#     .table(table_name) \
#     .writeStream \
#     .foreachBatch(process_micro_batch) \
#     .start()

# ============================================================================
# PONTOS-CHAVE PARA O EXAME DP-700
# ============================================================================

"""
✅ MEMORIZE:

1. HABILITAÇÃO:
   - `TBLPROPERTIES (delta.enableChangeDataFeed = true)`
   - Sem isso, você não consegue ler o histórico de mudanças granular.

2. COLUNAS DE METADADOS:
   - `_change_type`: insert, update_preimage (valor antigo), update_postimage (novo valor), delete.
   - `_commit_version`: Essencial para processamento ordenado.

3. USO TÍPICO:
   - Sincronização Bronze -> Silver -> Gold.
   - Evita reprocessar a tabela inteira (Full Load).
   - Muito mais leve que comparar snapshots inteiros.

4. TIME TRAVEL vs CDF:
   - Time Travel: Vê o estado da tabela em um momento ("como era ontem").
   - CDF: Vê O QUE MUDOU entre momentos ("quais linhas foram deletadas").
   
5. PERFORMANCE:
   - Habilitar CDF tem um pequeno custo de write (gravação de arquivos extras de log),
     mas economiza muito custo de leitura/processamento downstream.
"""
