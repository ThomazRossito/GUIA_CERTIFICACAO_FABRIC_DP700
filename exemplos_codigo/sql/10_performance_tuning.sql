-- ============================================================================
-- Exemplo 10: Performance Tuning no Data Warehouse
-- Tópico: Monitorar e Otimizar
-- Seção do Exame: 3 (Monitorar e Otimizar)
-- Complexidade: Avançado
-- Objetivo: Estatísticas, Views Materializadas e Gerenciamento de Carga
-- ============================================================================

-- ============================================================================
-- 1. ESTATÍSTICAS (STATISTICS)
-- ============================================================================
-- O Otimizador de Consultas (Query Optimizer) precisa de estatísticas para escolher o melhor plano.
-- No Fabric DW, estatísticas são criadas automaticamente, mas podem ser mantidas manualmente.

-- Criar estatísticas manualmente para uma coluna crítica de filtro/join
CREATE STATISTICS Stats_Sales_Date ON dbo.Sales (TransactionDate);

-- Atualizar estatísticas (se os dados mudaram drasticamente e o auto-update ainda não rodou)
UPDATE STATISTICS dbo.Sales Stats_Sales_Date;

-- Ver estatísticas
DBCC SHOW_STATISTICS ('dbo.Sales', 'Stats_Sales_Date');

-- ============================================================================
-- 2. VIEWS MATERIALIZADAS (MATERIALIZED VIEWS)
-- ============================================================================
-- Armazenam o RESULTADO pré-computado da query no disco.
-- Excelente para agregações pesadas em grandes volumes de dados.
-- O Query Optimizer usa automaticamente a view mesmo se você consultar a tabela base (Query Rewrite).

CREATE MATERIALIZED VIEW mv_SalesByRegion
WITH (DISTRIBUTION = HASH(Region)) -- Distribuir os dados da view
AS
SELECT 
    Region,
    SUM(Amount) as TotalSales,
    COUNT(*) as TransactionCount
FROM dbo.Sales
GROUP BY Region;

-- Para usar, basta rodar a query original:
-- SELECT Region, SUM(Amount) FROM dbo.Sales GROUP BY Region
-- O engine vai redirecionar para 'mv_SalesByRegion' transparentemente.

-- Rebuild (se necessário para manutenção)
ALTER MATERIALIZED VIEW mv_SalesByRegion REBUILD;

-- ============================================================================
-- 3. RESULT SET CACHING
-- ============================================================================
-- Cacheia o resultado da query na memória do driver.
-- Bom para dashboards repetitivos. Habilitado por nível de banco.

-- Verificar se está habilitado
SELECT name, is_result_set_caching_on 
FROM sys.databases;

-- Habilitar (exemplo genérico T-SQL - no Fabric é via Portal ou settings)
-- ALTER DATABASE CURRENT SET RESULT_SET_CACHING = ON;

-- ============================================================================
-- 4. ORDER BY NA CRIAÇÃO DE TABELA (CTAS)
-- ============================================================================
-- Melhora a compressão Columnstore e performance de segment elimination.

CREATE TABLE dbo.Sales_Ordered
WITH (
    DISTRIBUTION = HASH(CustomerID),
    CLUSTERED COLUMNSTORE INDEX
)
AS
SELECT * FROM dbo.Sales_Staging
ORDER BY TransactionDate; -- Ordena fisicamente os dados iniciais

-- ============================================================================
-- PONTOS-CHAVE PARA O EXAME DP-700
-- ============================================================================

/*
✅ MEMORIZE:

1. STATISTICS:
   - Essencial para 'Cardinality Estimation'.
   - Se a query está lenta e o plano parece "burro" (ex: Nested Loop em tabela grande),
     verifique se as estatísticas estão atualizadas.

2. MATERIALIZED VIEWS:
   - Diferente de VIEW normal (que é apenas lógica salva).
   - Ocupa espaço no disco.
   - Tem maintenance overhead (atualiza quando a tabela base muda).
   - O 'Query Rewrite' é a killer feature: você não precisa mudar o código do dashboard.

3. INDEXES:
   - No Fabric DW, Clustered Columnstore Index (CCI) é o padrão e é sempre criado.
   - Não suporta Rowstore Indexes (Non-clustered B-Tree) da mesma forma que SQL Server on-prem.
   - O foco é em ordenação (ORDER BY no CTAS) e Estatísticas.

4. DISTRIBUTION:
   - HASH: Para tabelas grandes (> 2GB). Escolha uma coluna com alta cardinalidade e sem skew.
   - REPLICATE: Para tabelas pequenas (Dimensões). Copia para todos os nós.
   - ROUND_ROBIN: Padrão para Staging. Distribui aleatoriamente.
*/
