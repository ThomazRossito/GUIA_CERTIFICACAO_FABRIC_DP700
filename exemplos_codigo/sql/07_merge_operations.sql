-- ============================================================================
-- Exemplo 7: Operações MERGE (Upsert)
-- Tópico: Ingestão e Transformação
-- Seção do Exame: 2 (Ingerir e Transformar)
-- Complexidade: Intermediário
-- Objetivo: Sincronizar dados entre Staging e Tabela Final (Dimensão)
-- ============================================================================

-- CENÁRIO:
-- Você tem uma tabela 'Staging.Customers' com dados novos e atualizados.
-- Você precisa atualizar a tabela 'dbo.DimCustomer' com base no CustomerID.
-- Se existir: Atualiza (UPDATE).
-- Se não existir: Insere (INSERT).
-- Se existir no destino mas não na origem: Opcionalmente deleta (DELETE).

-- 1. Estrutura das Tabelas
/*
CREATE TABLE dbo.DimCustomer (
    CustomerID INT,
    Name VARCHAR(100),
    Email VARCHAR(100),
    LastUpdated DATETIME2
);

CREATE TABLE Staging.Customers (
    CustomerID INT,
    Name VARCHAR(100),
    Email VARCHAR(100)
);
*/

-- ============================================================================
-- 2. COMANDO MERGE (T-SQL)
-- ============================================================================

MERGE INTO dbo.DimCustomer AS Target
USING Staging.Customers AS Source
ON (Target.CustomerID = Source.CustomerID)

-- Quando o ID existe em ambos (Match) -> Atualiza
WHEN MATCHED THEN
    UPDATE SET
        Target.Name = Source.Name,
        Target.Email = Source.Email,
        Target.LastUpdated = SYSDATETIME()

-- Quando o ID existe na Origem mas não no Destino (No Match) -> Insere
WHEN NOT MATCHED BY TARGET THEN
    INSERT (CustomerID, Name, Email, LastUpdated)
    VALUES (Source.CustomerID, Source.Name, Source.Email, SYSDATETIME())

-- (Opcional) Quando existe no Destino mas não na Origem
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
    
-- ============================================================================
-- 3. VARIAÇÃO: MERGE COM FILTRO EXTRA
-- ============================================================================
-- Atualizar APENAS se os dados forem diferentes (Performance Optimization)

MERGE INTO dbo.DimCustomer AS Target
USING Staging.Customers AS Source
ON (Target.CustomerID = Source.CustomerID)

-- Otimização: Só update se algo mudou
WHEN MATCHED AND (Target.Name <> Source.Name OR Target.Email <> Source.Email) THEN
    UPDATE SET
        Target.Name = Source.Name,
        Target.Email = Source.Email,
        Target.LastUpdated = SYSDATETIME()

WHEN NOT MATCHED BY TARGET THEN
    INSERT (CustomerID, Name, Email, LastUpdated)
    VALUES (Source.CustomerID, Source.Name, Source.Email, SYSDATETIME());

-- ============================================================================
-- PONTOS-CHAVE PARA O EXAME DP-700
-- ============================================================================

/*
✅ MEMORIZE:

1. COMPONENTES DO MERGE:
   - Target (foco da alteração).
   - Source (fonte dos dados).
   - ON (join condition).
   - WHEN MATCHED (Update/Delete).
   - WHEN NOT MATCHED [BY TARGET] (Insert).
   - WHEN NOT MATCHED BY SOURCE (Delete/Update).

2. TRANSAÇÃO:
   - O MERGE é executado como uma única transação atômica.
   - Tudo falha ou tudo passa.

3. DELTA LAKE MERGE vs T-SQL MERGE:
   - A sintaxe é muito similar.
   - Delta Lake (PySpark/SQL Analytics Endpoint) suporta MERGE.
   - Warehouse (T-SQL) suporta MERGE padrão ANSI.

4. LIMITAÇÕES:
   - Uma linha do Target não pode ser atualizada mais de uma vez na mesma transação MERGE.
   - Se a Source tiver duplicatas para o mesmo ID do Target, o MERGE falhará com erro.
*/
