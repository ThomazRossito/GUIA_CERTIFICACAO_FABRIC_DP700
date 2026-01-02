"""
Exemplo 6: Implementação de SCD Tipo 2 (Slowly Changing Dimensions)
Tópico: Transformação de Dados
Seção do Exame: 2 (Ingerir e Transformar)
Complexidade: Avançado
Objetivo: Manter histórico completo de alterações em uma dimensão
"""

from delta.tables import *
from pyspark.sql.functions import *

# ============================================================================
# 1. CONCEITO: SCD TIPO 2
# ============================================================================
# - SCD Tipo 1: Sobrescreve (sem histórico).
# - SCD Tipo 2: Cria nova linha para mudanças, mantendo a antiga válida.
#
# Colunas essenciais no Tipo 2:
# - SurrogateKey (Chave única gerada)
# - BusinessKey (Chave original do negócio, ex: CustomerID)
# - ValidFrom (Início da validade)
# - ValidTo (Fim da validade - NULL ou Data Futura para o atual)
# - IsCurrent (Flag boleana - True para o registro atual)

# ============================================================================
# 2. CONFIGURAÇÃO (TABELAS)
# ============================================================================

# Dados de Chegada (Updates)
updates_data = [
    (1, "Alice Smith", "New York", "2024-02-01"), # Mudou de endereço
    (3, "Charlie", "London", "2024-02-01")        # Novo cliente
]
updates_df = spark.createDataFrame(updates_data, ["CustomerID", "Name", "City", "UpdateDate"])

# Tabela Dimensão Existente
# Se não existir, crie.
table_name = "DimCustomer_SCD2"
# (Código de criação omitido, assumindo que tabela já existe ou será criada vazia)

# ============================================================================
# 3. IMPLEMENTAÇÃO COM PYSPARK E DELTA MERGE
# ============================================================================
# Implementar SCD2 puro com MERGE pode ser complexo.
# Uma abordagem comum (e recomendada para o exame) é:
# 1. Identificar registros que mudaram.
# 2. UNION ALL:
#    a) Novos registros (Insert).
#    b) Versões ANTIGAS fechadas (Update ValidTo).
#    c) Versões NOVAS abertas (Insert new version).
# 3. Gravar na tabela.

from pyspark.sql.window import Window

def merge_scd2(updates_df, target_table_name):
    target_table = DeltaTable.forName(spark, target_table_name)
    target_df = target_table.toDF()
    
    # Passo A: Join para encontrar correspondências
    # Join na BusinessKey (CustomerID) E apenas nos registros ATUAIS (IsCurrent=True)
    joined_df = updates_df.alias("updates").join(
        target_df.alias("target"),
        (col("updates.CustomerID") == col("target.CustomerID")) & (col("target.IsCurrent") == True),
        "left_outer"
    )
    
    # Passo B: Determinar Ação
    # - Novo registro (Target.ID is Null)
    # - Mudança (Target.City != Updates.City)
    # - Sem mudança
    
    # Passo C: Construir Logica de Merge
    # Esta é a sintaxe avançada do Delta MERGE para SCD2
    # Note: Em cenários complexos, às vezes fazemos em duas etapas (Update antigos, depois Insert novos)
    # Mas o Delta suporta lógica complexa num único MERGE se bem estruturado.
    
    # Para o exame, é crucial saber a LÓGICA CONCEITUAL:
    # "Fechar o registro antigo atualizando ValidTo e IsCurrent=False"
    # "Inserir novo registro com ValidFrom=Agora, ValidTo=Null, IsCurrent=True"
    
    pass # (Implementação completa requereria muitas linhas, mantendo foco no conceito)

# ============================================================================
# 4. EXEMPLO SIMPLIFICADO (CONCEITUALMENTE RELEVANTE)
# ============================================================================
# Como faríamos com SQL (Muitas vezes mais legível para SCD2 que PySpark puro):

"""
-- 1. Inserir novos registros (que não existem)
INSERT INTO DimCustomer
SELECT *, '2024-02-01', NULL, 1 FROM Staging S
WHERE NOT EXISTS (SELECT 1 FROM DimCustomer D WHERE D.CustomerID = S.CustomerID);

-- 2. Atualizar registros antigos (SCD2 Logic) - Fechar validade
UPDATE DimCustomer
SET ValidTo = '2024-01-31', IsCurrent = 0
WHERE CustomerID IN (SELECT CustomerID FROM Staging)
  AND IsCurrent = 1;

-- 3. Inserir novas versões dos registros atualizados
INSERT INTO DimCustomer
SELECT *, '2024-02-01', NULL, 1 FROM Staging S
WHERE EXISTS (SELECT 1 FROM DimCustomer D WHERE D.CustomerID = S.CustomerID);
"""

# ============================================================================
# PONTOS-CHAVE PARA O EXAME DP-700
# ============================================================================

"""
✅ MEMORIZE:

1. COLUNAS OBRIGATÓRIAS SCD TIPO 2:
   - Surrogate Key (PK da tabela dimensão).
   - ValidFrom / StartDate.
   - ValidTo / EndDate.
   - IsActive / IsCurrent.

2. HASH DIFFERENCE:
   - Para detectar mudanças em tabelas largas (muitas colunas), use hashes.
   - MD5(concat_ws(col1, col2, col3)) ou SHA2.
   - Compare HashOrigem vs HashDestino em vez de comparar coluna por coluna.

3. DELTA LAKE MERGE:
   - O comando MERGE suporta WHEN MATCHED UPDATE, WHEN NOT MATCHED INSERT.
   - Para SCD2 num único comando MERGE, é necessário usar técnicas avançadas (como fazer cross join com UNION de NULLs),
     mas o exame foca mais no conceito e na estrutura da tabela do que na query MERGE de 50 linhas.
     
4. SURROGATE KEYS:
   - No Spark distribuído, gerar IDs sequenciais (1, 2, 3...) é caro (monotonically_increasing_id não é perfeito).
   - Use UUIDs ou hashing para surrogate keys se possível, ou `row_number()` no final.
"""
