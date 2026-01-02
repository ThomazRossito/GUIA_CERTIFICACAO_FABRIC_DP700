# Respostas e Explicações - Simulado Seção 1

**Questão 1: B) Um Ambiente do Spark associado ao workspace.**
- **Explicação:** O Ambiente do Spark é onde você define a versão do runtime e as bibliotecas que serão usadas pelos notebooks e jobs, garantindo consistência. O Pool do Spark define o hardware (recursos de computação).

**Questão 2: C) Domain**
- **Explicação:** Domínios são usados para agrupar workspaces por área de negócio (como Finanças, RH, etc.), facilitando a governança e a descoberta de dados em uma arquitetura de Data Mesh.

**Questão 3: C) Contributor**
- **Explicação:** A função de Contribuidor permite criar e editar conteúdo, mas não gerenciar permissões ou compartilhar conteúdo, o que corresponde exatamente ao requisito.

**Questão 4: B) Permitir o controle de versão dos itens do Fabric e facilitar a colaboração da equipe.**
- **Explicação:** A integração com o Git serve para versionar o código-fonte dos itens do Fabric, permitindo que as equipes colaborem, rastreiem alterações e revertam para versões anteriores.

**Questão 5: C) Configurando Regras de Implantação (Deployment Rules) para o Data Warehouse.**
- **Explicação:** As Regras de Implantação são projetadas especificamente para gerenciar as diferenças de configuração (como strings de conexão e parâmetros) entre os ambientes de um pipeline de implantação.

**Questão 6: C) Segurança em Nível de Linha (RLS)**
- **Explicação:** A RLS é o mecanismo ideal para filtrar os dados que um usuário pode ver com base em seus atributos, como a região de vendas. Ela filtra as linhas da tabela em tempo de consulta.

**Questão 7: B) Máscara Dinâmica de Dados (DDM)**
- **Explicação:** A DDM foi projetada para mascarar dados em colunas específicas para usuários não autorizados, sem alterar os dados subjacentes. A permissão UNMASK pode ser concedida a usuários privilegiados.

**Questão 8: B) Atribuir o endosso "Certificado" (Certified).**
- **Explicação:** O endosso "Certificado" é o nível mais alto de validação, indicando que um item atende aos padrões de qualidade da organização e é uma fonte de dados confiável e autoritativa.

**Questão 9: C) Pipeline**
- **Explicação:** Um Pipeline é a ferramenta de orquestração do Fabric, projetada para sequenciar e executar diferentes tipos de atividades, como copiar dados e executar notebooks, em um único fluxo de trabalho.

**Questão 10: B) Um gatilho baseado em evento (event-driven trigger).**
- **Explicação:** Os gatilhos de evento no Fabric podem reagir a eventos do OneLake, como a criação de um arquivo, permitindo a execução automática de um pipeline em resposta a esse evento.

**Questão 11: B) Autoscale gerencia o número de nós (máquinas) no pool, enquanto Dynamic Allocation gerencia o número de executores (trabalhadores) para um job específico.**
- **Explicação:** Autoscale ajusta a infraestrutura (nós do pool), enquanto a Alocação Dinâmica otimiza o uso desses recursos alocando executores para os jobs conforme a necessidade.

**Questão 12: C) Adicionar uma nova linha para o cliente com as informações atualizadas e marcar a linha antiga como não mais atual.**
- **Explicação:** Esta é a definição clássica de SCD Tipo 2, que preserva o histórico completo das alterações criando um novo registro para cada mudança.

**Questão 13: B) Executar um "Sync" (Sincronizar) a partir do painel de controle do código-fonte do workspace.**
- **Explicação:** A ação de "Sync" (ou "Update") no workspace busca as alterações mais recentes do branch do Git conectado e as aplica ao workspace do Fabric.

**Questão 14: B) Para tratar o esquema do seu Data Warehouse ou Lakehouse como código (Schema-as-Code) e versioná-lo no Git.**
- **Explicação:** Os Projetos de Banco de Dados permitem que as definições de tabelas, views, etc., sejam salvas como scripts SQL, integrando o desenvolvimento de banco de dados ao ciclo de vida de CI/CD.

**Questão 15: C) Build**
- **Explicação:** A permissão de "Build" em um modelo semântico (ou no Lakehouse/Warehouse subjacente) permite que um usuário crie conteúdo (como relatórios) com base nesses dados, sem conceder permissão para ler os dados brutos diretamente.

**Questão 16: B) Configurando as dependências de "conclusão" (on completion) nas setas que conectam as atividades.**
- **Explicação:** Em um pipeline do Fabric, você pode conectar atividades e configurar a seta de conexão para ser executada em caso de "Sucesso", "Falha", "Conclusão" ou "Ignorado", permitindo a criação de fluxos de trabalho condicionais.

**Questão 17: B) Evita a duplicação de dados e garante que você esteja sempre acessando os dados da fonte original.**
- **Explicação:** Atalhos são ponteiros para os dados originais. Eles não copiam os dados, o que economiza armazenamento e garante que as consultas sempre usem os dados mais recentes da fonte.

**Questão 18: C) Implementar Máscara Dinâmica de Dados (DDM) nas colunas PII e conceder a permissão `UNMASK` ao grupo de auditores.**
- **Explicação:** DDM é a ferramenta perfeita para este cenário, pois mascara os dados para todos por padrão, enquanto permite que um grupo específico veja os dados não mascarados através da permissão `UNMASK`.

**Questão 19: B) Criar um Domínio chamado "Recursos Humanos" e associar o workspace de RH a ele.**
- **Explicação:** Domínios são a estrutura de governança de alto nível no Fabric para agrupar workspaces por área de negócio, que é exatamente o que o cenário descreve.

**Questão 20: B) Criar dois Ambientes do Spark separados, cada um com a versão necessária da biblioteca, e associar cada notebook ao seu respectivo ambiente.**
- **Explicação:** Ambientes do Spark são projetados para isolar dependências de software (bibliotecas e versões do Spark), permitindo que diferentes projetos coexistam sem conflitos.

**Questão 21: B) Regras de Implantação (Deployment Rules)**
- **Explicação:** As Regras de Implantação são usadas nos Pipelines de Implantação para definir como os valores de parâmetros e configurações de fontes de dados devem ser alterados ao mover conteúdo entre os estágios.

**Questão 22: C) Controlar a visibilidade de uma tabela ou view inteira para um usuário.**
- **Explicação:** OLS opera no nível do objeto. Se um usuário não tiver permissão `SELECT` em uma tabela, a tabela inteira será como se não existisse para ele.

**Questão 23: D) Nos logs de auditoria do Microsoft 365 e no log de atividades do workspace do Fabric.**
- **Explicação:** As atividades de alto nível do Fabric são integradas ao log de auditoria unificado do Microsoft 365, enquanto atividades mais detalhadas podem ser encontradas no log de atividades do workspace.

**Questão 24: B) Criar um Pipeline, adicionar uma atividade para executar o Dataflow Gen2 e, em seguida, encadear uma atividade para executar o notebook após a conclusão bem-sucedida da primeira.**
- **Explicação:** Esta é a função principal de um Pipeline: orquestrar e encadear diferentes tipos de atividades em um fluxo de trabalho controlado.

**Questão 25: B) ReadAll**
- **Explicação:** A permissão `ReadAll` concede acesso aos arquivos no OneLake via Spark, mas não concede acesso ao SQL Endpoint. A permissão `Read` concede acesso ao SQL Endpoint, mas não ao Spark.

**Questão 26: B) O Membro pode publicar e compartilhar conteúdo (como aplicativos), enquanto o Contribuidor pode criar e editar, mas não compartilhar.**
- **Explicação:** A principal distinção é a capacidade de compartilhar e publicar. Membros podem distribuir o conteúdo, enquanto Contribuidores estão limitados a criar e editar dentro do workspace.

**Questão 27: D) Desenvolvimento -> Teste -> Produção**
- **Explicação:** Este é o fluxo padrão e lógico do ALM, onde o conteúdo é criado em Dev, validado em Teste e, finalmente, promovido para consumo em Produção.

**Questão 28: C) Um Rótulo de Confidencialidade (Sensitivity Label) do Microsoft Purview**
- **Explicação:** Rótulos de Confidencialidade são a ferramenta de governança para classificar a sensibilidade dos dados e aplicar políticas de proteção, como impedir a exportação.

**Questão 29: B) Um Pipeline**
- **Explicação:** Um Pipeline é a ferramenta de orquestração que permite combinar atividades de diferentes tipos, como executar uma consulta SQL e, em seguida, executar um notebook.

**Questão 30: C) As definições dos seus itens do Fabric são salvas como arquivos no branch do Git conectado.**
- **Explicação:** O commit salva uma representação em texto (JSON, etc.) dos seus itens do Fabric no repositório Git, permitindo o controle de versão.

**Questão 31: C) Executor**
- **Explicação:** As funções padrão são Admin, Member, Contributor e Viewer. "Executor" não é uma função de workspace padrão no Fabric.

**Questão 32: C) Funções e Expressões do Sistema (ex: `@adddays(utcnow(), -1)`)**
- **Explicação:** O idioma de expressões do Fabric fornece funções de sistema, como `utcnow()`, que podem ser usadas para criar valores dinâmicos em tempo de execução.

**Questão 33: B) Ela não se aplica a usuários que acessam os arquivos diretamente no OneLake via Spark.**
- **Explicação:** A RLS definida no SQL Endpoint é aplicada apenas pelo motor T-SQL. Um usuário com permissões para o OneLake pode contornar a RLS acessando os arquivos Parquet diretamente com o Spark. Para uma segurança completa, é necessário implementar um controle de acesso também na camada do OneLake.

**Questão 34: B) Que o relatório é considerado um ativo de dados oficial, confiável e de alta qualidade, validado pela organização.**
- **Explicação:** A certificação é o mais alto nível de endosso, sinalizando aos usuários que o ativo é autoritativo e atende aos padrões de qualidade.

**Questão 35: A) Otimizada para Memória (Memory Optimized)**
- **Explicação:** Trabalhos de ETL (Extração, Transformação e Carga) no Spark, que envolvem muitas junções, shuffles e agregações, geralmente são intensivos em memória. A família de nós otimizada para memória fornece mais RAM por vCPU, o que é ideal para esses cenários._
