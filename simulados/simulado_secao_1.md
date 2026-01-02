# Simulado - Seção 1: Implementar e Gerenciar uma Solução de Análise

**Instruções:** Responda às seguintes questões para testar seu conhecimento sobre a implementação e o gerenciamento de soluções de análise no Microsoft Fabric. As respostas e explicações estão no final.

---

**Questão 1:**

Você está configurando um novo workspace no Microsoft Fabric para uma equipe de engenharia de dados. A equipe precisa de um ambiente com uma versão específica do Spark e um conjunto de bibliotecas Python pré-instaladas para todos os notebooks e jobs. Qual componente do Fabric você deve criar e configurar para atender a esse requisito?

A) Um Pool do Spark com a família de nós apropriada.
B) Um Ambiente do Spark associado ao workspace.
C) Um Pipeline de implantação com variáveis de ambiente.
D) Um Atalho (Shortcut) para um repositório de bibliotecas.

**Questão 2:**

Sua organização está adotando uma arquitetura de Data Mesh. Você precisa agrupar logicamente vários workspaces que pertencem ao departamento de Finanças para aplicar políticas de governança e facilitar a descoberta de dados. Qual recurso do Fabric permite essa organização?

A) Capacity
B) Deployment Pipeline
C) Domain
D) Workspace Roles

**Questão 3:**

Um engenheiro de dados precisa de permissão para criar, editar e executar notebooks e pipelines em um workspace, mas não deve ser capaz de gerenciar as permissões de outros usuários ou as configurações do workspace. Qual é a função (role) mínima que você deve atribuir a ele no workspace?

A) Admin
B) Member
C) Contributor
D) Viewer

**Questão 4:**

Você está implementando o gerenciamento do ciclo de vida (ALM) para sua solução no Fabric. Você conectou seu workspace a um repositório Git no Azure DevOps. Qual é o principal benefício de usar essa integração?

A) Aumentar a capacidade de computação do Spark.
B) Permitir o controle de versão dos itens do Fabric e facilitar a colaboração da equipe.
C) Criptografar automaticamente todos os dados no OneLake.
D) Reduzir os custos de armazenamento do OneLake.

**Questão 5:**

Sua equipe usa o recurso de Pipelines de Implantação (Deployment Pipelines) para mover conteúdo entre os ambientes de Desenvolvimento, Teste e Produção. A string de conexão do Data Warehouse é diferente em cada ambiente. Como você pode gerenciar essa alteração de forma automática durante a implantação?

A) Modificando manualmente cada item após a implantação.
B) Usando o Git para mesclar diferentes branches de configuração.
C) Configurando Regras de Implantação (Deployment Rules) para o Data Warehouse.
D) Usando um Ambiente do Spark diferente para cada estágio.

**Questão 6:**

Você precisa garantir que apenas os gerentes de vendas de cada região possam ver os dados de vendas correspondentes à sua própria região em um relatório do Power BI conectado a um Data Warehouse do Fabric. Qual mecanismo de segurança você deve implementar?

A) Máscara Dinâmica de Dados (DDM)
B) Segurança em Nível de Coluna (CLS)
C) Segurança em Nível de Linha (RLS)
D) Rótulos de Confidencialidade (Sensitivity Labels)

**Questão 7:**

Em uma tabela de funcionários no seu Data Warehouse, a coluna que armazena o número do CPF deve ser visível apenas para os usuários do departamento de RH. Para todos os outros usuários, a coluna deve aparecer com os valores mascarados (ex: XXX.XXX.XXX-XX). Qual recurso de segurança é o mais apropriado para este cenário?

A) Segurança em Nível de Objeto (OLS)
B) Máscara Dinâmica de Dados (DDM)
C) Endosso (Endorsement)
D) Segurança em Nível de Linha (RLS)

**Questão 8:**

Você publicou um modelo semântico que foi validado pela equipe de governança de dados e é considerado a fonte oficial e confiável para os relatórios de vendas da empresa. Qual recurso de governança você deve usar para sinalizar este item como autoritativo e de alta qualidade?

A) Aplicar um rótulo de confidencialidade "Público".
B) Atribuir o endosso "Certificado" (Certified).
C) Atribuir o endosso "Promovido" (Promoted).
D) Habilitar o log do workspace.

**Questão 9:**

Você precisa orquestrar um processo que primeiro copia um arquivo CSV de uma conta de armazenamento externa para o seu Lakehouse e, em seguida, executa um notebook PySpark para transformar esses dados. Qual item do Fabric é o mais adequado para desenhar e executar este fluxo de trabalho de ponta a ponta?

A) Dataflow Gen2
B) Notebook
C) Pipeline
D) KQL Queryset

**Questão 10:**

Você quer que seu pipeline de ingestão de dados seja executado automaticamente sempre que um novo arquivo for carregado na pasta `bronze/novos_pedidos/` do seu Lakehouse. Que tipo de configuração de automação você deve usar?

A) Um agendamento (schedule) para ser executado a cada minuto.
B) Um gatilho baseado em evento (event-driven trigger).
C) Uma atividade de "Wait" no pipeline.
D) Um alerta do Data Activator.

**Questão 11:**

Ao configurar um Pool do Spark, você se depara com as opções de "Autoscale" e "Dynamic Allocation". Qual a principal diferença entre elas no contexto do Fabric?

A) Autoscale gerencia o número de executores por job, enquanto Dynamic Allocation gerencia o número de nós no pool.
B) Autoscale gerencia o número de nós (máquinas) no pool, enquanto Dynamic Allocation gerencia o número de executores (trabalhadores) para um job específico.
C) Ambas são a mesma coisa, apenas com nomes diferentes.
D) Autoscale é para Dataflows e Dynamic Allocation é para Notebooks.

**Questão 12:**

Você precisa implementar a lógica de SCD Tipo 2 para uma dimensão de Clientes em seu Data Warehouse. Qual das seguintes ações é característica do SCD Tipo 2?

A) Sobrescrever o registro existente com as novas informações.
B) Adicionar novas colunas à tabela para armazenar o valor anterior.
C) Adicionar uma nova linha para o cliente com as informações atualizadas e marcar a linha antiga como não mais atual.
D) Mover o registro antigo para uma tabela de histórico separada.

**Questão 13:**

Você está usando a integração do Git com seu workspace. Um colega de equipe fez commit de uma alteração em um notebook no repositório Git. O que você precisa fazer para que essa alteração apareça no seu workspace do Fabric?

A) Executar um "Commit" do seu workspace.
B) Executar um "Sync" (Sincronizar) a partir do painel de controle do código-fonte do workspace.
C) Criar um novo Pipeline de Implantação.
D) Reiniciar o Pool do Spark.

**Questão 14:**

Qual a principal finalidade de se usar "Projetos de Banco de Dados" (Database Projects) em conjunto com o Fabric?

A) Para executar consultas T-SQL diretamente no OneLake.
B) Para tratar o esquema do seu Data Warehouse ou Lakehouse como código (Schema-as-Code) e versioná-lo no Git.
C) Para criar modelos semânticos do Power BI.
D) Para gerenciar as permissões de acesso dos usuários ao banco de dados.

**Questão 15:**

Você precisa dar a um analista de BI a capacidade de criar relatórios do Power BI com base em um modelo semântico, mas ele não deve ser capaz de ler os dados subjacentes no Lakehouse ou no Data Warehouse. Qual permissão você deve conceder no item (Lakehouse/Warehouse)?

A) Read
B) ReadAll
C) Build
D) Write

**Questão 16:**

Você precisa orquestrar um processo complexo com várias dependências: a Atividade B só pode começar após a Atividade A ser concluída com sucesso, e a Atividade C deve ser executada se a Atividade A falhar. Como você configura isso em um Pipeline do Fabric?

A) Usando gatilhos de evento para cada atividade.
B) Configurando as dependências de "conclusão" (on completion) nas setas que conectam as atividades.
C) Escrevendo um script PySpark para gerenciar o fluxo.
D) Configurando regras de implantação.

**Questão 17:**

Qual é a principal vantagem de usar um "Atalho" (Shortcut) no OneLake em vez de copiar os dados?

A) Melhora a compressão dos dados.
B) Evita a duplicação de dados e garante que você esteja sempre acessando os dados da fonte original.
C) Permite a edição dos dados na fonte diretamente do Fabric.
D) Converte automaticamente os dados para o formato Delta Lake.

**Questão 18:**

Você precisa implementar uma política de segurança que impeça a visualização de todas as colunas que contenham informações de identificação pessoal (PII), como `Email` e `Telefone`, para todos os usuários, exceto um grupo de segurança de auditores. Qual é a abordagem mais eficiente?

A) Criar uma view segura para cada tabela que omita as colunas PII.
B) Implementar Segurança em Nível de Coluna (CLS) usando `GRANT` e `DENY` nas colunas PII.
C) Implementar Máscara Dinâmica de Dados (DDM) nas colunas PII e conceder a permissão `UNMASK` ao grupo de auditores.
D) Usar Segurança em Nível de Linha (RLS) para filtrar as colunas.

**Questão 19:**

Sua empresa tem workspaces para os departamentos de Vendas, Marketing e RH. Para facilitar a governança e a descoberta de dados, você quer que os ativos de dados de RH sejam claramente separados e gerenciados pelos líderes de RH. Qual é o primeiro passo para alcançar essa estrutura?

A) Criar um novo Capacity para o RH.
B) Criar um Domínio chamado "Recursos Humanos" e associar o workspace de RH a ele.
C) Criar um Pipeline de Implantação para o RH.
D) Dar a todos do RH a função de Admin no workspace.

**Questão 20:**

Você precisa executar um notebook que requer a biblioteca `scikit-learn` versão 1.2. Outro projeto no mesmo workspace requer a versão 0.24. Como você pode gerenciar essas dependências conflitantes de forma eficaz?

A) Instalar ambas as versões no Pool do Spark padrão.
B) Criar dois Ambientes do Spark separados, cada um com a versão necessária da biblioteca, e associar cada notebook ao seu respectivo ambiente.
C) Usar o comando `%pip install` no início de cada notebook, o que pode levar a inconsistências.
D) Criar dois Workspaces separados para cada projeto.

**Questão 21:**

Ao configurar um Pipeline de Implantação, você percebe que um parâmetro em um Dataflow precisa ter o valor "UAT" no ambiente de Teste e "PROD" no ambiente de Produção. Qual recurso dos Pipelines de Implantação permite essa configuração?

A) Variáveis de Pipeline
B) Regras de Implantação (Deployment Rules)
C) Integração com o Git
D) Endosso (Endorsement)

**Questão 22:**

Qual é a principal função da Segurança em Nível de Objeto (OLS)?

A) Mascarar os dados dentro de uma coluna.
B) Filtrar as linhas que um usuário pode ver em uma tabela.
C) Controlar a visibilidade de uma tabela ou view inteira para um usuário.
D) Classificar a sensibilidade de uma tabela.

**Questão 23:**

Você precisa registrar e auditar todas as atividades que ocorrem em um workspace, como quem acessou um relatório ou quem executou um pipeline. Onde você pode encontrar esses logs de auditoria?

A) No Hub de Monitoramento (Monitoring Hub).
B) Nos logs de diagnóstico do Capacity.
C) No portal do Microsoft Purview.
D) Nos logs de auditoria do Microsoft 365 e no log de atividades do workspace do Fabric.

**Questão 24:**

Você tem um processo de ETL que é executado diariamente. A primeira etapa é um Dataflow Gen2 que ingere e limpa os dados. A segunda etapa é um notebook que aplica regras de negócio complexas. Qual a melhor forma de orquestrar isso?

A) Agendar o Dataflow e o notebook para serem executados no mesmo horário, esperando que o Dataflow termine primeiro.
B) Criar um Pipeline, adicionar uma atividade para executar o Dataflow Gen2 e, em seguida, encadear uma atividade para executar o notebook após a conclusão bem-sucedida da primeira.
C) Chamar o notebook de dentro do Dataflow Gen2 usando Power Query.
D) Usar dois gatilhos de evento separados.

**Questão 25:**

Ao configurar a segurança de um Lakehouse, você quer permitir que um grupo de analistas de dados leia os arquivos Parquet diretamente do OneLake usando Spark, mas não quer que eles possam se conectar ao SQL Endpoint. Qual permissão de item você deve conceder?

A) Read
B) ReadAll
C) Build
D) ReadData

**Questão 26:**

Qual é a principal diferença entre as funções de workspace "Membro" (Member) e "Contribuidor" (Contributor)?

A) O Membro pode gerenciar permissões de workspace, enquanto o Contribuidor não pode.
B) O Membro pode publicar e compartilhar conteúdo (como aplicativos), enquanto o Contribuidor pode criar e editar, mas não compartilhar.
C) O Contribuidor tem acesso somente leitura, enquanto o Membro pode editar.
D) Não há diferença, são sinônimos.

**Questão 27:**

Você está projetando um pipeline de implantação. Qual é o fluxo de implantação recomendado para os estágios?

A) Produção -> Teste -> Desenvolvimento
B) Desenvolvimento -> Produção -> Teste
C) Teste -> Desenvolvimento -> Produção
D) Desenvolvimento -> Teste -> Produção

**Questão 28:**

Você precisa garantir que um relatório do Power BI seja classificado como "Altamente Confidencial" e que políticas de proteção de dados sejam aplicadas a ele, como impedir a exportação. Qual recurso de governança do Fabric você deve usar?

A) Endosso "Certificado"
B) Um Domínio
C) Um Rótulo de Confidencialidade (Sensitivity Label) do Microsoft Purview
D) Segurança em Nível de Coluna (CLS)

**Questão 29:**

Você precisa criar um pipeline que execute uma consulta SQL em um Data Warehouse do Azure, copie o resultado e, em seguida, execute um notebook do Fabric. Qual item do Fabric você usaria para conter essa lógica de fluxo de trabalho?

A) Um Dataflow Gen2
B) Um Pipeline
C) Um KQL Queryset
D) Um Ambiente do Spark

**Questão 30:**

Ao usar a integração do Git, o que acontece quando você faz "commit" das suas alterações no workspace?

A) As alterações são imediatamente implantadas na produção.
B) As alterações são salvas localmente no seu computador.
C) As definições dos seus itens do Fabric são salvas como arquivos no branch do Git conectado.
D) Um novo Pool do Spark é criado para validar as alterações.

**Questão 31:**

Qual das seguintes opções NÃO é uma função de workspace padrão no Microsoft Fabric?

A) Admin
B) Member
C) Executor
D) Contributor

**Questão 32:**

Você precisa passar um valor de data dinamicamente para um pipeline para que ele processe apenas os dados do dia anterior. Qual recurso de pipeline você usaria para construir essa data dinamicamente?

A) Parâmetros do Pipeline
B) Variáveis de Pipeline
C) Funções e Expressões do Sistema (ex: `@adddays(utcnow(), -1)`)
D) Regras de Implantação

**Questão 33:**

Qual é a principal limitação da Segurança em Nível de Linha (RLS) quando aplicada no SQL Endpoint de um Lakehouse?

A) Ela não funciona para consultas T-SQL.
B) Ela não se aplica a usuários que acessam os arquivos diretamente no OneLake via Spark.
C) Ela só pode filtrar com base no nome de usuário, não em funções.
D) Ela não permite o uso de tabelas de dimensão para as regras de segurança.

**Questão 34:**

Você promoveu um relatório a "Certificado". O que isso implica para os usuários da sua organização?

A) Que o relatório agora está protegido por senha.
B) Que o relatório é considerado um ativo de dados oficial, confiável e de alta qualidade, validado pela organização.
C) Que o relatório será automaticamente implantado em todos os workspaces.
D) Que o relatório agora usa o modo DirectLake.

**Questão 35:**

Você está configurando um Pool do Spark para trabalhos de ETL que consomem muita memória. Qual família de nós (Node Family) seria a mais indicada para este cenário?

A) Otimizada para Memória (Memory Optimized)
B) Otimizada para Computação (Compute Optimized)
C) Otimizada para GPU (GPU Optimized)
D) Otimizada para Armazenamento (Storage Optimized)

**Questão 36:**

Você está configurando um Spark Environment para seu workspace. A equipe precisa usar a biblioteca `pandas` versão 2.0.0 e `scikit-learn` versão 1.3.0. Qual é a melhor abordagem para garantir que todos os notebooks usem essas versões específicas?

A) Instalar as bibliotecas usando `%pip install` no início de cada notebook.
B) Criar um Spark Environment customizado com as bibliotecas especificadas e associá-lo ao workspace.
C) Modificar o código de cada notebook para verificar e instalar as versões corretas.
D) Usar um Pool do Spark diferente para cada versão de biblioteca.

**Questão 37:**

Sua equipe está usando Git Integration com Azure DevOps. Um desenvolvedor fez commit de mudanças em um notebook, mas depois percebeu que cometeu um erro. Como ele pode desfazer o último commit local antes de fazer sync com o repositório remoto?

A) Usar a opção "Undo" no Git panel do Fabric.
B) Deletar o notebook e recriar do zero.
C) Fazer um novo commit com as correções.
D) Usar "Source control" → "Undo last commit" no Fabric.

**Questão 38:**

Você está implementando uma estratégia de branching Git Flow para seu projeto Fabric. Qual branch deve ser usado para desenvolver novas features antes de mesclá-las na branch principal?

A) main
B) develop
C) feature/*
D) hotfix/*

**Questão 39:**

Você criou um Database Project no Fabric para gerenciar o schema do seu Data Warehouse como código. Qual arquivo é gerado durante o build do projeto que contém a definição completa do schema?

A) .sql
B) .dacpac
C) .json
D) .yaml

**Questão 40:**

Você está configurando Row-Level Security (RLS) em uma tabela de vendas. A regra deve permitir que gerentes vejam apenas vendas de sua própria região. Qual função T-SQL você deve usar na função de predicado para obter o nome de usuário atual?

A) CURRENT_USER()
B) USER_NAME()
C) SYSTEM_USER
D) SESSION_USER

**Questão 41:**

Você implementou RLS em uma tabela, mas percebeu que usuários com a role `db_owner` conseguem ver todos os dados, ignorando a política de segurança. Isso é esperado?

A) Não, é um bug que deve ser reportado.
B) Sim, `db_owner` e `db_datareader` ignoram RLS por padrão.
C) Não, você deve ter configurado a política incorretamente.
D) Sim, mas apenas `db_owner` ignora RLS, não `db_datareader`.

**Questão 42:**

Você precisa implementar Column-Level Security (CLS) para ocultar a coluna `salary` da tabela `employees` para todos os usuários, exceto para a role `HR_Manager`. Qual comando T-SQL você deve usar?

A) `GRANT SELECT ON employees(salary) TO HR_Manager;`
B) `DENY SELECT ON employees(salary) TO PUBLIC; GRANT SELECT ON employees(salary) TO HR_Manager;`
C) `ALTER TABLE employees ALTER COLUMN salary ADD MASK;`
D) `CREATE SECURITY POLICY ON employees FOR salary;`

**Questão 43:**

Você está implementando Object-Level Security (OLS) para segregar dados de diferentes departamentos. Cada departamento deve ter seu próprio schema (ex: `Finance`, `HR`, `Sales`). Como você pode garantir que usuários do departamento Finance só acessem objetos no schema `Finance`?

A) Usar RLS em todas as tabelas.
B) Criar roles específicas por departamento e conceder permissões apenas no schema correspondente.
C) Usar DDM para mascarar dados de outros departamentos.
D) Criar workspaces separados para cada departamento.

**Questão 44:**

Você precisa mascarar a coluna `credit_card` em uma tabela para que usuários não privilegiados vejam apenas os últimos 4 dígitos. Qual função de Dynamic Data Masking (DDM) você deve usar?

A) `DEFAULT()`
B) `EMAIL()`
C) `PARTIAL(prefix, padding, suffix)`
D) `RANDOM()`

**Questão 45:**

Você aplicou uma Sensitivity Label "Confidential" em um lakehouse. O que acontece automaticamente com os dados?

A) Os dados são criptografados com uma chave gerenciada pela Microsoft.
B) A label é propagada para downstream items e aparece em ferramentas de governança como Microsoft Purview.
C) Os dados são movidos para um workspace seguro separado.
D) O acesso aos dados é automaticamente restrito apenas a Admins.

**Questão 46:**

Você criou um shortcut no seu Lakehouse apontando para um container ADLS Gen2. Usuários estão recebendo erro "Access Denied" ao tentar ler dados através do shortcut. Qual é a causa mais provável?

A) O shortcut está configurado incorretamente.
B) Os usuários não têm a role "Storage Blob Data Reader" no container ADLS Gen2.
C) O Lakehouse não suporta shortcuts para ADLS Gen2.
D) Os dados no ADLS Gen2 estão corrompidos.

**Questão 47:**

Você está configurando OneLake Data Access Roles para um lakehouse. Qual role permite que usuários leiam dados via Spark e SQL Endpoint, mas não permite gerenciar o lakehouse?

A) Admin
B) Member  
C) Contributor
D) ReadAll

**Questão 48:**

Você precisa configurar um Deployment Pipeline com 3 estágios: Development, Test e Production. Qual é a ordem correta de implantação?

A) Production → Test → Development
B) Development → Test → Production
C) Test → Development → Production
D) Development → Production → Test

**Questão 49:**

Você configurou Deployment Rules para um Data Warehouse no pipeline. A regra especifica que a connection string deve ser diferente em cada estágio. Quando a regra é aplicada?

A) Manualmente, quando você edita o item.
B) Automaticamente, durante a implantação de um estágio para outro.
C) Apenas na primeira implantação.
D) Apenas quando você faz rollback.

**Questão 50:**

Você está usando CI/CD com GitHub Actions para implantar itens do Fabric. Qual ferramenta da Microsoft você deve usar para automatizar a implantação via API?

A) Azure CLI
B) Fabric REST API
C) Power BI REST API
D) Azure DevOps CLI

---

## Respostas e Explicações

(As respostas serão adicionadas em um arquivo separado ou no final para evitar spoilers)
_
