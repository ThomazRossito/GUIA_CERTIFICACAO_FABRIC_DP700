"""
Exemplo 8: Spark Structured Streaming
Tópico: Dados em Streaming
Seção do Exame: 2 (Ingerir e Transformar)
Complexidade: Avançado
Objetivo: Configurar stream reader, transformações em janela e writer com checkpoint
"""

from pyspark.sql.functions import *
from pyspark.sql.types import *

# ============================================================================
# 1. DEFINIÇÃO DA FONTE (READ STREAM)
# ============================================================================
# Cenário: Lendo dados IoT de arquivos JSON que chegam numa pasta (Files)
# ou de um Eventstream (conectado via OneLake).

schema = StructType([
    StructField("deviceId", StringType()),
    StructField("temperature", DoubleType()),
    StructField("timestamp", TimestampType())
])

source_path = "Files/iot_data/"

df_stream = spark.readStream \
    .format("json") \
    .schema(schema) \
    .option("maxFilesPerTrigger", 1) \
    .load(source_path)

# ============================================================================
# 2. TRANSFORMAÇÕES (COM WINDOW E WATERMARK)
# ============================================================================
# Watermark: Define quanto tempo aceitamos dados atrasados.
# Window: Agregação temporal.

windowed_counts = df_stream \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        window("timestamp", "5 minutes"), # Janela tumulando de 5 min
        "deviceId"
    ) \
    .agg(avg("temperature").alias("avg_temp"))

# ============================================================================
# 3. ESCRITA (WRITE STREAM) - DELTA TABLE
# ============================================================================
# O checkpointLocation é CRUCIAL para tolerância a falhas.
# O outputMode define como os dados são escritos (append, update, complete).

query = windowed_counts.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "Files/checkpoints/iot_agg") \
    .trigger(processingTime='1 minute') \
    .toTable("IoT_Aggregations")

# ============================================================================
# 4. TRIGGERS ALTERNATIVOS (MUITO IMPORTANTE)
# ============================================================================

# Trigger: ProcessingTime (Padrão) - Processa a cada X tempo se houver dados
# .trigger(processingTime='30 seconds')

# Trigger: AvailableNow (Recomendado para Batch Regular) - Processa TUDO que tem e para.
# Simula um comportamento de Batch usando a engine de Streaming (incremental).
# .trigger(availableNow=True)

# Trigger: Once (Depreciado, usar AvailableNow)
# .trigger(once=True)

# ============================================================================
# 5. GERENCIAMENTO
# ============================================================================

print(f"Streaming Query Name: {query.name}")
print(f"Streaming Query ID: {query.id}")
print(f"Is Active: {query.isActive}")

# Esperar terminar (apenas para testes/scripts blocking, não para notebooks interativos)
# query.awaitTermination()

# ============================================================================
# PONTOS-CHAVE PARA O EXAME DP-700
# ============================================================================

"""
✅ MEMORIZE:

1. CHECKPOINTING:
   - OBRIGATÓRIO para garantir "Exactly-Once" (ou "At-Least-Once") e tolerância a falhas.
   - Armazena o offset (onde parei) no OneLake/ADLS.
   - Se mudar a query logicamente, muitas vezes precisa limpar o checkpoint e reiniciar.

2. OUTPUT MODES:
   - Append: Só novas linhas são adicionadas ao destino. (Bom para INSERT-only).
   - Complete: A tabela/resultado inteiro é reescrito a cada trigger. (Bom para Agregações Totais).
   - Update: Apenas linhas que mudaram (agregadas) são atualizadas (Upsert-like).

3. WATERMARK:
   - Define o limite de "late arrival data".
   - Dados mais velhos que o watermark são descartados pelo engine.
   - Essencial para limpeza de estado em agregações long-running (senão a memória explode).

4. TRIGGER availableNow=True:
   - Melhor prática para jobs agendados no Fabric Pipeline que processam dados incrementalmente.
   - Inicia, processa tudo desde o último offset, e desliga o cluster (economia de custo).
"""
