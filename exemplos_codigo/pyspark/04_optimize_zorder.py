"""
Exemplo 4: Otimização de Tabelas Delta (V-Order & Z-ORDER)
Tópico: Otimização de Desempenho
Seção do Exame: 3 (Monitorar e Otimizar)
Complexidade: Intermediário
Objetivo: Aplicar técnicas avançadas de otimização em tabelas Delta Lake
"""

from delta.tables import *
from pyspark.sql.functions import *

# ============================================================================
# 1. ENTENDENDO V-ORDER
# ============================================================================
# V-Order é uma otimização de gravação específica do Fabric (baseada no Verti-Scan).
# Melhora a compressão e a velocidade de leitura.
# Por padrão, já vem habilitado no Fabric Runtime 1.2+.

# Verificar se V-Order está habilitado na sessão
print(f"V-Order Enabled: {spark.conf.get('spark.sql.parquet.vorder.enabled')}")

# ============================================================================
# 2. CENÁRIO: TABELA DE VENDAS DESORGANIZADA
# ============================================================================

table_name = "Sales_Large"
table_path = "Tables/Sales_Large"

# Simular dados desorganizados (se necessário)
if not DeltaTable.isDeltaTable(spark, table_path):
    df = spark.range(0, 1000000).withColumn("Region", expr("case when id % 2 = 0 then 'North' else 'South' end")) \
                                .withColumn("Date", expr("date_add('2024-01-01', cast(id % 365 as int))")) \
                                .withColumn("Amount", expr("rand() * 1000"))
    
    # Gravando SEM otimizações primeiro
    spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "false")
    df.write.format("delta").mode("overwrite").saveAsTable(table_name)
    print("Tabela criada (potencialmente muitos arquivos pequenos).")

# ============================================================================
# 3. COMANDO OPTIMIZE (Bin-Packing)
# ============================================================================
# O 'OPTIMIZE' compacta arquivos pequenos em arquivos maiores (~1GB).
# Essencial após muitas inserções pequenas ou streamings.

print("Executando OPTIMIZE (Bin-packing)...")

# Via SQL API (mais comum)
spark.sql(f"OPTIMIZE {table_name}")

# ============================================================================
# 4. COMANDO Z-ORDER (Data Skipping Multidimensional)
# ============================================================================
# O Z-ORDER reorganiza os dados fisicamente para colocar valores similares próximos.
# Excelente para colunas usadas frequentemente em filtros (WHERE) e joins.
# Diferente de Partitioning, funciona bem colunas de alta cardinalidade (Ex: CustomerID, Timestamp).

print("Executando OPTIMIZE com Z-ORDER BY (Region, Date)...")

# Via SQL API
spark.sql(f"""
    OPTIMIZE {table_name}
    ZORDER BY (Region, Date)
""")

# ============================================================================
# 5. MANUTENÇÃO: VACUUM
# ============================================================================
# Remove arquivos antigos que não são mais referenciados pelo log de transação.
# Economiza espaço, mas impede Time Travel para versões muito antigas.

# Retenção padrão: 7 dias.

print("Executando VACUUM (remoção de arquivos obsoletos)...")

# Dry Run (Simulação - mostra o que seria deletado)
spark.sql(f"VACUUM {table_name} RETAIN 168 HOURS DRY RUN").show()

# Execução Real
# spark.sql(f"VACUUM {table_name} RETAIN 168 HOURS")

# ============================================================================
# 6. FUNÇÃO PARA ANALISAR DETALHES DA TABELA
# ============================================================================

delta_table = DeltaTable.forName(spark, table_name)
history_df = delta_table.history()

print("\nHistórico de Operações (Últimas 5):")
history_df.select("version", "timestamp", "operation", "operationParameters").show(5, truncate=False)

# Procure por operação 'OPTIMIZE' e parâmetros como 'zOrderBy'

# ============================================================================
# PONTOS-CHAVE PARA O EXAME DP-700
# ============================================================================

"""
✅ MEMORIZE:

1. OPTIMIZE vs VACUUM:
   - OPTIMIZE: Melhora performance de LEITURA (Compactação + Z-Order). Cria novos arquivos.
   - VACUUM: Limpa armazenamento. Remove arquivos antigos. Não melhora performance de leitura diretamente.

2. QUANDO USAR Z-ORDER:
   - Colunas frequentemente usadas em filtros (WHERE col = val).
   - Colunas de alta cardinalidade (muitos valores únicos) onde Particionamento seria ruim.
   
3. PARTITIONING vs Z-ORDER:
   - Partitioning: Bom para colunas de BAIXA cardinalidade (Ano, Região, Departamento). Separa pastas físicas.
   - Z-Order: Bom para ALTA cardinalidade dentro das partições ou tabela não particionada.

4. V-ORDER:
   - Exclusivo/Padrão no Fabric.
   - Otimiza o formato Parquet para leituras mais rápidas (especialmente Power BI DirectLake).
   - Aplicado durante a escrita.

5. CUSTO:
   - OPTIMIZE é uma operação pesada (Compute intensive).
   - Não rodar a cada micro-batch. Rodar periodicamente (ex: 1x ao dia ou após cargas pesadas).
"""
