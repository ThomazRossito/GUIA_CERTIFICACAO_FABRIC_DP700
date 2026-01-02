-- ============================================================================
-- Exemplo 4: Implementação de Dynamic Data Masking (DDM)
-- Tópico: Segurança e Governança
-- Seção do Exame: 1 (Implementar e Gerenciar)
-- Complexidade: Básico
-- Objetivo: Ofuscar dados sensíveis sem impedir o acesso à coluna
-- ============================================================================

-- CENÁRIO:
-- Call Center precisa confirmar os últimos 4 dígitos do Cartão de Crédito e validar E-mail.
-- Atendentes NÃO devem ver o número completo do cartão nem o e-mail completo.
-- Administradores devem ver os dados reais.

-- 1. Criação da Tabela com Máscaras
CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    
    -- MÁSCARA 1: E-mail (mostra primeira letra + @ + domínio)
    EmailAddress VARCHAR(100) MASKED WITH (FUNCTION = 'email()'),
    
    -- MÁSCARA 2: Customizada (X para tudo, exceto últimos 4 dígitos)
    CreditCard VARCHAR(20) MASKED WITH (FUNCTION = 'partial(0, "XXXX-XXXX-XXXX-", 4)'),
    
    -- MÁSCARA 3: Default (ofusca totalmente conforme tipo de dados)
    Phone VARCHAR(20) MASKED WITH (FUNCTION = 'default()') 
);

-- 2. Inserindo dados (os dados são gravados INTEGRAIS no disco)
INSERT INTO Customers (FirstName, LastName, EmailAddress, CreditCard, Phone)
VALUES 
('Roberto', 'Silva', 'roberto@empresa.com', '1234-5678-9012-3456', '11-99999-0000'),
('Ana', 'Costa', 'ana@gmail.com', '9876-5432-1098-7654', '21-88888-1111');

-- ============================================================================
-- 3. TESTANDO O COMPORTAMENTO
-- ============================================================================

-- Passo A: Criar usuário com permissões de leitura
CREATE USER ServiceAgent WITHOUT LOGIN;
GRANT SELECT ON Customers TO ServiceAgent;

-- Passo B: Executar como ServiceAgent (verá mascarado)
EXECUTE AS USER = 'ServiceAgent';
SELECT * FROM Customers;
REVERT;

/*
RESULTADO PARA O USUÁRIO MASCARADO:
EmailAddress: rXXX@XXXX.com
CreditCard:   XXXX-XXXX-XXXX-3456
Phone:        xxxx (default para string)
*/

-- ============================================================================
-- 4. PERMITINDO VISUALIZAÇÃO DOS DADOS REAIS (UNMASK)
-- ============================================================================

-- Para permitir que um supervisor veja os dados reais, usamos a permissão UNMASK.

CREATE USER Supervisor WITHOUT LOGIN;
GRANT SELECT ON Customers TO Supervisor;
GRANT UNMASK TO Supervisor; -- Habilita ver dados reais

EXECUTE AS USER = 'Supervisor';
SELECT * FROM Customers; -- Verá dados originais
REVERT;

-- ============================================================================
-- PONTOS-CHAVE PARA O EXAME DP-700
-- ============================================================================

/*
✅ MEMORIZE:

1. NÃO É SÓ VISUALIZAÇÃO:
   - DDM altera como os dados são retornados na query.
   - O dado no disco (storage) NÃO é alterado.
   
2. FUNÇÕES DE MÁSCARA::
   - `default()`: XXXX (string), 0 (numérico), 01.01.1900 (data).
   - `email()`: aXXX@XXXX.com
   - `partial(prefix, padding, suffix)`: Mostra N char no início, substitui meio por padding, mostra N char no fim.
   - `random(min, max)`: Retorna valor numérico aleatório no range.

3. LIMITAÇÃO DE SEGURANÇA:
   - DDM é uma medida de OFUSCAÇÃO, não de segurança forte.
   - Usuário malicioso pode inferir dados via cláusula WHERE.
     Ex: `SELECT ID FROM Customers WHERE Phone = '11-99999-0000'`
     Se retornar uma linha, o usuário sabe o telefone, mesmo vendo 'xxxx'.

4. PERMISSÃO CHAVE:
   - `GRANT UNMASK TO User`: Permite ver dados reais.
   - `REVOKE UNMASK`: Volta a ver mascarado.
*/
