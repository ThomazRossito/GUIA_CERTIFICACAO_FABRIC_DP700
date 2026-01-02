-- Exemplo de Script SQL para Transformação de Dados no Microsoft Fabric Data Warehouse

-- Cenário: Atualizar uma tabela de dimensão de clientes (Dim_Cliente) com novos dados
-- de uma tabela de preparação (Staging_Cliente), implementando a lógica de SCD Tipo 2.

-- Etapa 1: Criar as tabelas de exemplo (se não existirem)
-- Em um cenário real, essas tabelas já existiriam no seu Warehouse.

CREATE TABLE IF NOT EXISTS Dim_Cliente (
    ClienteKey INT IDENTITY(1,1) PRIMARY KEY, -- Chave substituta (Surrogate Key)
    ClienteID INT,
    Nome VARCHAR(100),
    Estado VARCHAR(2),
    DataInicio DATETIME2,
    DataFim DATETIME2,
    IsCurrent BIT
);

CREATE TABLE IF NOT EXISTS Staging_Cliente (
    ClienteID INT,
    Nome VARCHAR(100),
    Estado VARCHAR(2)
);

-- Etapa 2: Inserir dados de exemplo
-- Inserir um cliente existente na dimensão
INSERT INTO Dim_Cliente (ClienteID, Nome, Estado, DataInicio, DataFim, IsCurrent)
VALUES (101, 'João Silva', 'SP', '2024-01-01', NULL, 1);

-- Inserir dados na tabela de preparação (staging)
-- Cliente 101 mudou de estado (SP -> RJ) - vai gerar uma atualização SCD2
-- Cliente 102 é um novo cliente - vai gerar uma nova inserção
TRUNCATE TABLE Staging_Cliente;
INSERT INTO Staging_Cliente (ClienteID, Nome, Estado)
VALUES (101, 'João Silva', 'RJ'), (102, 'Maria Souza', 'MG');


-- Etapa 3: Usar a instrução MERGE para implementar a lógica de Carga Incremental (SCD Tipo 2)

MERGE INTO Dim_Cliente AS Target
USING (
    -- Seleciona os clientes da staging e compara com a dimensão atual para encontrar alterações
    SELECT
        s.ClienteID,
        s.Nome,
        s.Estado,
        d.ClienteKey AS CurrentClienteKey,
        d.Estado AS CurrentEstado
    FROM Staging_Cliente s
    LEFT JOIN Dim_Cliente d ON s.ClienteID = d.ClienteID AND d.IsCurrent = 1
) AS Source
ON Target.ClienteKey = Source.CurrentClienteKey AND Target.IsCurrent = 1 AND Source.Estado <> Target.Estado

-- CASO 1: O cliente existe e seu estado mudou (UPDATE na linha antiga)
WHEN MATCHED THEN
    UPDATE SET
        Target.IsCurrent = 0,
        Target.DataFim = GETDATE()

-- CASO 2: O cliente é novo (INSERT da nova linha)
WHEN NOT MATCHED BY TARGET THEN
    INSERT (ClienteID, Nome, Estado, DataInicio, DataFim, IsCurrent)
    VALUES (Source.ClienteID, Source.Nome, Source.Estado, GETDATE(), NULL, 1);

-- Etapa 4: Inserir as novas versões das linhas que foram atualizadas (SCD Tipo 2)
-- Esta etapa é necessária porque o MERGE não pode inserir e atualizar a mesma linha na mesma operação.
INSERT INTO Dim_Cliente (ClienteID, Nome, Estado, DataInicio, DataFim, IsCurrent)
SELECT
    s.ClienteID,
    s.Nome,
    s.Estado,
    GETDATE(),
    NULL,
    1
FROM Staging_Cliente s
JOIN Dim_Cliente d ON s.ClienteID = d.ClienteID
WHERE d.DataFim IS NOT NULL -- A linha antiga foi fechada na etapa MERGE
  AND d.ClienteID = s.ClienteID
  AND d.IsCurrent = 0;


-- Etapa 5: Verificar o resultado
-- O cliente 101 deve ter duas entradas: uma antiga (IsCurrent=0) e uma nova (IsCurrent=1)
-- O cliente 102 deve ter uma nova entrada.
SELECT * FROM Dim_Cliente ORDER BY ClienteID, DataInicio;


-- Exemplo de uso de Função de Janela para remover duplicatas em uma tabela de staging

CREATE TABLE IF NOT EXISTS Staging_Vendas_Duplicadas (
    ID_Venda INT,
    Data_Venda DATE,
    Valor DECIMAL(10, 2)
);

INSERT INTO Staging_Vendas_Duplicadas VALUES (1, '2025-01-10', 100.00);
INSERT INTO Staging_Vendas_Duplicadas VALUES (1, '2025-01-10', 100.00); -- Duplicata
INSERT INTO Staging_Vendas_Duplicadas VALUES (2, '2025-01-11', 250.50);

WITH VendasComRN AS (
    SELECT
        ID_Venda,
        Data_Venda,
        Valor,
        ROW_NUMBER() OVER(PARTITION BY ID_Venda, Data_Venda, Valor ORDER BY ID_Venda) as rn
    FROM Staging_Vendas_Duplicadas
)
-- DELETE FROM VendasComRN WHERE rn > 1; -- Em muitos sistemas, DELETE em CTE não é direto.
-- A abordagem mais segura é selecionar os dados únicos para uma nova tabela ou deletar com subquery.
SELECT ID_Venda, Data_Venda, Valor
FROM VendasComRN
WHERE rn = 1;
