-- ============================================================================
-- Exemplo 2: Implementação de Row-Level Security (RLS)
-- Tópico: Segurança e Governança
-- Seção do Exame: 1 (Implementar e Gerenciar)
-- Complexidade: Intermediário
-- Objetivo: Restringir acesso a linhas de dados com base no usuário logado
-- ============================================================================

-- CENÁRIO:
-- Uma tabela de Vendas (Sales) contém dados de todas as regiões.
-- Gerentes de vendas devem ver apenas dados de suas próprias regiões.
-- A tabela 'SalesTerritory' mapeia usuários para regiões.

-- 1. Criação das Tabelas de Exemplo
CREATE TABLE Sales (
    OrderID INT,
    Product VARCHAR(50),
    Region VARCHAR(50),
    Amount DECIMAL(10, 2)
);

CREATE TABLE Security.UserRegion (
    UserName VARCHAR(100),
    Region VARCHAR(50)
);

-- Inserindo dados de exemplo
INSERT INTO Sales VALUES (1, 'Laptop', 'North', 1000.00);
INSERT INTO Sales VALUES (2, 'Mouse', 'South', 20.00);
INSERT INTO Sales VALUES (3, 'Keyboard', 'North', 50.00);

-- Mapeando usuários (UserName deve corresponder ao login do Azure AD/Entra ID)
INSERT INTO Security.UserRegion VALUES ('manager_north@contoso.com', 'North');
INSERT INTO Security.UserRegion VALUES ('manager_south@contoso.com', 'South');

-- ============================================================================
-- 2. CRIAÇÃO DA FUNÇÃO DE PREDICADO (PREDICATE FUNCTION)
-- ============================================================================
-- Esta função retorna 1 se o usuário tiver acesso, 0 caso contrário.

CREATE SCHEMA Security;
GO

CREATE FUNCTION Security.fn_securitypredicate(@Region AS sysname)
    RETURNS TABLE
WITH SCHEMABINDING
AS
    RETURN SELECT 1 AS fn_securitypredicate_result
    FROM Security.UserRegion AS ur
    WHERE (
        -- Condição 1: Usuário corresponde à região da linha
        ur.UserName = USER_NAME() 
        AND ur.Region = @Region
    ) 
    OR 
    (
        -- Condição 2: Usuário é Admin (exemplo: 'admin@contoso.com') e vê tudo
        USER_NAME() = 'admin@contoso.com'
    );
GO

-- ============================================================================
-- 3. CRIAÇÃO DA POLÍTICA DE SEGURANÇA (SECURITY POLICY)
-- ============================================================================
-- Aplica a função de predicado à tabela Sales, filtrando automaticamente as linhas.

CREATE SECURITY POLICY Security.SalesFilter
    ADD FILTER PREDICATE Security.fn_securitypredicate(Region)
    ON dbo.Sales
    WITH (STATE = ON); -- Habilita a política imediatamente
GO

-- ============================================================================
-- 4. TESTANDO A SEGURANÇA
-- ============================================================================

-- Para testar, você usaria 'EXECUTE AS USER', mas no Fabric (SQL Analytics Endpoint)
-- a autenticação é via Entra ID, então o teste ideal é logar com os usuários diferentes.

-- O que 'manager_north@contoso.com' veria:
-- | OrderID | Product  | Region | Amount |
-- |---------|----------|--------|--------|
-- | 1       | Laptop   | North  | 1000.00|
-- | 3       | Keyboard | North  | 50.00  |

-- O que 'manager_south@contoso.com' veria:
-- | OrderID | Product | Region | Amount |
-- |---------|---------|--------|--------|
-- | 2       | Mouse   | South  | 20.00  |

-- ============================================================================
-- PONTOS-CHAVE PARA O EXAME DP-700
-- ============================================================================

/*
✅ MEMORIZE:

1. COMPONENTES DO RLS:
   - Predicate Function: Lógica de filtragem (Table-Valued Function).
   - Security Policy: Vincula a função à tabela.
   - Filter Predicate: Filtra linhas para SELECT, UPDATE, DELETE.
   - Block Predicate: Bloqueia inserção/update que viole a regra (opcional).

2. FUNÇÕES DE SISTEMA:
   - USER_NAME(): Retorna o nome do usuário atual (contexto do banco).
   - IS_MEMBER('RoleName'): Verifica se usuário pertence a uma role de banco.

3. LIMITAÇÕES NO FABRIC:
   - RLS funciona no SQL Analytics Endpoint e Warehouse.
   - DirectLake no Power BI RESPEITA o RLS do Warehouse (Single Sign-On).
   - Se o usuário acessar via Spark diretamente nos arquivos (OneLake), o RLS do SQL NÃO se aplica!
     (Para proteger arquivos, precisa usar OneLake Security ou ACLs, não SQL RLS).

4. PERMISSÕES:
   - Usuários com permissão 'db_owner' ou 'sysadmin' geralmente ignoram RLS.
   - É melhor usar roles customizadas com permissões mínimas (Least Privilege).
*/
