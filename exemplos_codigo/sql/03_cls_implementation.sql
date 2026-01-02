-- ============================================================================
-- Exemplo 3: Implementação de Column-Level Security (CLS)
-- Tópico: Segurança e Governança
-- Seção do Exame: 1 (Implementar e Gerenciar)
-- Complexidade: Básico
-- Objetivo: Restringir acesso a colunas sensíveis (ex: Salário, CPF)
-- ============================================================================

-- CENÁRIO:
-- Tabela de Funcionários contém dados sensíveis como 'Salary' e 'SSN'.
-- A maioria dos usuários deve ver Nome e Departamento, mas NÃO o Salário.
-- Apenas o RH (HumanResources) deve ver o Salário.

-- 1. Criação da Tabela
CREATE TABLE Employees (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2), -- Coluna Sensível
    SSN VARCHAR(11)        -- Coluna Sensível
);

-- 2. Inserindo dados
INSERT INTO Employees VALUES (1, 'John', 'Doe', 'IT', 80000.00, '12345678901');
INSERT INTO Employees VALUES (2, 'Jane', 'Smith', 'HR', 90000.00, '98765432100');

-- ============================================================================
-- 3. IMPLEMENTAÇÃO USANDO PERMISSÕES GRANULARES (GRANT/DENY)
-- ============================================================================
-- No SQL Server/Fabric, CLS é implementado controlando permissões de SELECT em colunas específicas.

-- Passo A: Criar Roles
CREATE ROLE DataAnalyst; -- Usuários comuns
CREATE ROLE HR_Manager;  -- Usuários privilegiados

-- Passo B: Conceder acesso a colunas NÃO sensíveis para Analistas
GRANT SELECT ON Employees(EmployeeID, FirstName, LastName, Department) TO DataAnalyst;

-- NOTA: Se o usuário tentar fazer 'SELECT * FROM Employees', falhará com erro.
-- Eles DEVEM especificar apenas as colunas permitidas: 'SELECT FirstName, Department FROM Employees'.

-- Passo C: Conceder acesso TOTAL (todas as colunas) para RH
GRANT SELECT ON Employees TO HR_Manager;

-- ============================================================================
-- 4. ALTERNATIVA: USANDO DENY (Menos Recomendado, mas possível)
-- ============================================================================

-- Se o usuário já tem SELECT na tabela (ex: via role 'public' ou outra role),
-- você pode bloquear explicitamente a coluna.

-- DENY SELECT ON Employees(Salary, SSN) TO DataAnalyst;

-- CUIDADO: DENY sempre vence GRANT. Se um usuário estiver em ambas as roles (Analyst e HR),
-- o DENY vai bloquear o acesso, mesmo que ele seja HR!

-- ============================================================================
-- PONTOS-CHAVE PARA O EXAME DP-700
-- ============================================================================

/*
✅ MEMORIZE:

1. MECANISMO T-SQL:
   - Não existe um comando "CREATE COLUMN POLICY".
   - CLS é feito via `GRANT SELECT ON Table(Column) TO Role`.

2. COMPORTAMENTO 'SELECT *':
   - Se um usuário tem acesso apenas a algumas colunas, 'SELECT *' FALHARÁ.
   - Isso pode quebrar relatórios existentes se eles usarem 'SELECT *'.
   - Melhor prática: Sempre listar colunas explicitamente em Views ou Queries.

3. USO COM VIEWS (Abordagem Alternativa e Comum):
   - Criar uma View que exclui as colunas sensíveis.
   - `CREATE VIEW vw_EmployeesPublic AS SELECT EmployeeID, Name, Dept FROM Employees`
   - Dar acesso à View para todos, e acesso à Tabela Base apenas para RH.
   - Isso evita erros de 'SELECT *' na aplicação final.

4. SEGURANÇA NO POWER BI:
   - Se usar DirectLake/DirectQuery, as permissões do SQL são respeitadas.
   - Se importar (Import Mode), os dados sensíveis serão trazidos para o modelo se o usuário que atualiza o dataset tiver acesso.
*/
