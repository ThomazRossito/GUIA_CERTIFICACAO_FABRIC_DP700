"""
Exemplo 1: Configuração de Spark Environment
Tópico: Workspace Configuration
Seção do Exame: 1 (Implementar e Gerenciar)
Complexidade: Básico
Objetivo: Demonstrar como configurar bibliotecas e runtime em Spark Environment

IMPORTANTE: Este código demonstra conceitos. A configuração real é feita via UI do Fabric.
"""

# ============================================================================
# PARTE 1: VERIFICAR AMBIENTE ATUAL
# ============================================================================

# Verificar versão do Spark
print(f"Spark Version: {spark.version}")

# Verificar versão do Python
import sys
print(f"Python Version: {sys.version}")

# Listar bibliotecas instaladas
import pkg_resources
installed_packages = [d.project_name for d in pkg_resources.working_set]
print(f"Total de bibliotecas instaladas: {len(installed_packages)}")

# Verificar bibliotecas específicas importantes para DP-700
important_libs = ['pandas', 'numpy', 'delta-spark', 'pyspark']
for lib in important_libs:
    if lib in installed_packages:
        version = pkg_resources.get_distribution(lib).version
        print(f"✓ {lib}: {version}")
    else:
        print(f"✗ {lib}: NÃO INSTALADO")

# ============================================================================
# PARTE 2: INSTALAR BIBLIOTECAS (TEMPORÁRIO - APENAS PARA ESTE NOTEBOOK)
# ============================================================================

# Método 1: Instalar biblioteca inline (temporário)
# NOTA: Isso só funciona para a sessão atual do notebook
# %pip install pandas==2.0.0

# Método 2: Instalar múltiplas bibliotecas
# %pip install pandas==2.0.0 scikit-learn==1.3.0 matplotlib==3.7.0

# ============================================================================
# PARTE 3: CONFIGURAÇÕES DO SPARK
# ============================================================================

# Ver todas as configurações do Spark
spark_configs = spark.sparkContext.getConf().getAll()
print(f"\nTotal de configurações Spark: {len(spark_configs)}")

# Configurações importantes para DP-700
important_configs = [
    'spark.sql.parquet.vorder.enabled',  # V-Order
    'spark.sql.adaptive.enabled',         # AQE
    'spark.databricks.delta.optimizeWrite.enabled',
    'spark.sql.shuffle.partitions'
]

print("\nConfigurações Importantes:")
for config in important_configs:
    value = spark.conf.get(config, "NOT SET")
    print(f"{config}: {value}")

# ============================================================================
# PARTE 4: MODIFICAR CONFIGURAÇÕES (PARA SESSÃO ATUAL)
# ============================================================================

# Aumentar partições de shuffle (padrão: 200)
spark.conf.set("spark.sql.shuffle.partitions", "400")

# Habilitar Adaptive Query Execution (geralmente já habilitado)
spark.conf.set("spark.sql.adaptive.enabled", "true")

# Habilitar coalesce de partições
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")

# Verificar mudanças
print(f"\nNovo valor de shuffle.partitions: {spark.conf.get('spark.sql.shuffle.partitions')}")

# ============================================================================
# PARTE 5: INFORMAÇÕES DO CLUSTER
# ============================================================================

# Informações do cluster Spark
sc = spark.sparkContext
print(f"\nSpark Application ID: {sc.applicationId}")
print(f"Spark Application Name: {sc.appName}")
print(f"Spark Master: {sc.master}")
print(f"Default Parallelism: {sc.defaultParallelism}")

# ============================================================================
# PONTOS-CHAVE PARA O EXAME DP-700
# ============================================================================

"""
✅ MEMORIZE:

1. SPARK ENVIRONMENT vs SPARK POOL:
   - Environment: Define runtime e bibliotecas (permanente)
   - Pool: Define recursos de compute (nodes, cores, memory)

2. CONFIGURAÇÃO DE BIBLIOTECAS:
   - Via Environment: Permanente para todo workspace
   - Via %pip install: Temporário (apenas sessão atual)
   - Via requirements.txt: Upload para Environment

3. CONFIGURAÇÕES IMPORTANTES:
   - spark.sql.parquet.vorder.enabled: V-Order (padrão: true no Fabric)
   - spark.sql.adaptive.enabled: AQE (padrão: true)
   - spark.sql.shuffle.partitions: Número de partições (padrão: 200)

4. QUANDO USAR ENVIRONMENT:
   - Bibliotecas específicas necessárias em todos os notebooks
   - Versões específicas de bibliotecas
   - Configurações de runtime customizadas

5. NODE FAMILIES:
   - Memory Optimized: ETL, large datasets
   - Compute Optimized: CPU-intensive workloads
"""

# ============================================================================
# TROUBLESHOOTING COMUM
# ============================================================================

"""
PROBLEMA: ModuleNotFoundError: No module named 'pandas'
SOLUÇÃO: 
1. Adicionar biblioteca ao Spark Environment
2. Ou usar %pip install pandas (temporário)

PROBLEMA: Biblioteca instalada mas não funciona
SOLUÇÃO:
1. Reiniciar sessão do Spark
2. Verificar versão compatível com Spark runtime

PROBLEMA: Configuração não persiste entre sessões
SOLUÇÃO:
1. Configurações via spark.conf.set() são temporárias
2. Para permanente: configurar no Spark Environment
"""

print("\n✅ Exemplo completo! Configurações demonstradas com sucesso.")
