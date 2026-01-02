# Simulado - Seção 2: Ingerir e Transformar Dados

**Instruções:** Responda às seguintes questões para testar seu conhecimento sobre a ingestão e transformação de dados no Microsoft Fabric. As respostas e explicações estão no final.

---

**Questão 36:**

Você precisa ingerir uma tabela de 100 GB de um banco de dados SQL Server para o seu Lakehouse todas as noites. A tabela de origem possui uma coluna `LastModifiedDate`. Qual é o padrão de carregamento de dados mais eficiente para este cenário?

A) Carga Completa (Full Load)
B) Carga Incremental (Incremental Load) usando a coluna `LastModifiedDate` como marca d'água (watermark).
C) Usar o Espelhamento (Mirroring) do Fabric.
D) Exportar os dados para CSV e usar um Dataflow Gen2.

**Questão 37:**

Ao projetar um modelo dimensional, qual é o principal propósito de uma tabela de dimensão?

A) Armazenar as medições numéricas e as métricas do negócio.
B) Conter os atributos descritivos e contextuais (como nome do cliente, categoria do produto) que são usados para filtrar e agrupar os dados de fato.
C) Servir como uma área de preparação (staging) para os dados brutos.
D) Armazenar dados de log e telemetria.

**Questão 38:**

Você está ingerindo dados de um sistema de vendas onde os endereços dos clientes podem mudar ao longo do tempo. Você precisa manter um histórico completo de todas as alterações de endereço. Qual tipo de Slowly Changing Dimension (SCD) você deve implementar para a sua tabela de dimensão de clientes?

A) SCD Tipo 0
B) SCD Tipo 1
C) SCD Tipo 2
D) SCD Tipo 3

**Questão 39:**

Qual é a principal vantagem de usar o formato de tabela Delta Lake no seu Lakehouse?

A) É o formato mais rápido para ingestão de dados de streaming.
B) Fornece transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade), o que permite operações confiáveis de `MERGE`, `UPDATE` e `DELETE` em um data lake.
C) É um formato somente leitura otimizado para relatórios.
D) É o único formato que pode ser lido pelo Power BI.

**Questão 40:**

Você precisa processar um fluxo de eventos de cliques de um site em tempo real para identificar quais páginas são mais populares a cada minuto. Qual combinação de ferramentas do Fabric é a mais adequada para este cenário de análise em tempo real?

A) Pipeline e Data Warehouse
B) Dataflow Gen2 e Lakehouse
C) Eventstream e KQL Database
D) Notebook Spark e Espelhamento (Mirroring)

**Questão 41:**

Você tem dados armazenados em uma conta do Amazon S3 e precisa analisá-los no Fabric sem copiá-los. Qual recurso do OneLake permite que você acesse esses dados como se estivessem em seu Lakehouse?

A) Espelhamento (Mirroring)
B) Atalho (Shortcut)
C) Atividade de Cópia (Copy Activity)
D) Dataflow Gen2

**Questão 42:**

Qual é a principal função do recurso de Espelhamento (Mirroring) no Microsoft Fabric?

A) Criar uma cópia de backup do seu Lakehouse.
B) Criar uma réplica somente leitura e continuamente sincronizada de um banco de dados operacional (como Azure SQL DB ou Snowflake) no OneLake.
C) Versionar o código dos seus notebooks no Git.
D) Distribuir a carga de trabalho do Spark entre vários clusters.

**Questão 43:**

Em um notebook PySpark, você lê uma tabela grande em um DataFrame e precisa aplicar três transformações diferentes a ele. Para evitar que o Spark releia e recalcule o DataFrame da fonte a cada transformação, qual é a melhor otimização a ser aplicada após a leitura?

A) `.repartition(100)`
B) `.cache()`
C) `.collect()`
D) `.write.mode("overwrite")`

**Questão 44:**

Você está usando o Spark Structured Streaming para processar dados de um Azure Event Hub. Você precisa contar o número de eventos que chegam a cada 10 minutos, com as janelas começando a cada 5 minutos (ex: 00:00-00:10, 00:05-00:15, etc.). Que tipo de função de janela (windowing) você deve usar?

A) Janela Deslizante (Tumbling Window)
B) Janela Saltitante (Hopping Window)
C) Janela de Sessão (Session Window)
D) Janela Deslizante Contínua (Sliding Window)

**Questão 45:**

Você está usando um Dataflow Gen2 para limpar dados. A coluna `PrecoUnitario` tem alguns valores ausentes (nulos). Você precisa preencher esses valores nulos com o valor `0`. Qual transformação no editor do Power Query você usaria?

A) Substituir Valores (Replace Values)
B) Preencher (Fill)
C) Remover Erros (Remove Errors)
D) Dinamizar Coluna (Pivot Column)

**Questão 46:**

Qual instrução T-SQL é usada para combinar dados de uma tabela de origem (staging) em uma tabela de destino, realizando operações de `INSERT`, `UPDATE` e `DELETE` em uma única transação atômica?

A) `JOIN`
B) `UNION`
C) `MERGE`
D) `APPLY`

**Questão 47:**

Você está processando um fluxo de dados de telemetria de sensores. Você quer agrupar os eventos por `SensorId` e calcular a média da temperatura em janelas de tempo fixas e não sobrepostas de 15 minutos. Que tipo de janela é essa?

A) Janela Deslizante (Tumbling Window)
B) Janela Saltitante (Hopping Window)
C) Janela de Sessão (Session Window)
D) Janela de Agregação (Aggregate Window)

**Questão 48:**

Ao trabalhar com dados no Lakehouse, você nota que uma tabela Delta tem milhares de arquivos pequenos, o que está degradando o desempenho da leitura. Qual comando você deve executar para resolver esse problema?

A) `VACUUM`
B) `OPTIMIZE`
C) `ANALYZE TABLE`
D) `REFRESH TABLE`

**Questão 49:**

Você precisa enriquecer um fluxo de dados de vendas em tempo real com informações de categoria de produto que estão em uma tabela de dimensão no seu KQL Database. Qual operador no Eventstream ou KQL você usaria para realizar esse enriquecimento?

A) `filter`
B) `aggregate`
C) `join` ou `lookup`
D) `summarize`

**Questão 50:**

Qual é a principal diferença entre um Lakehouse e um Data Warehouse no Microsoft Fabric?

A) O Lakehouse é para dados estruturados e o Data Warehouse é para dados não estruturados.
B) O Lakehouse usa o motor Spark e armazena dados em formato Delta (arquivos), sendo ideal para engenharia de dados e IA, enquanto o Data Warehouse usa um motor T-SQL e um formato de coluna proprietário, sendo otimizado para análise de BI e SQL.
C) O Lakehouse não suporta transações ACID, enquanto o Data Warehouse sim.
D) O Lakehouse é um recurso do Power BI, enquanto o Data Warehouse é um recurso do Synapse.

**Questão 51:**

Você está usando o Spark Structured Streaming e precisa lidar com dados que podem chegar com atraso. Qual recurso você usaria para especificar por quanto tempo o estado de uma agregação deve ser mantido para aguardar por dados atrasados?

A) `.withWatermark("eventTime", "10 minutes")`
B) `.withTimeout("10 minutes")`
C) `.withLateArrival("10 minutes")`
D) `.withDelay("10 minutes")`

**Questão 52:**

Você está criando um Dataflow Gen2. Qual linguagem de expressão está por trás da interface gráfica do Power Query?

A) Python
B) SQL
C) M
D) DAX

**Questão 53:**

Em uma arquitetura Medalhão, qual é o propósito da camada (ou zona) Prata (Silver)?

A) Armazenar os dados brutos, exatamente como vieram da fonte.
B) Armazenar dados limpos, conformados e enriquecidos, onde os tipos de dados foram corrigidos e regras de validação foram aplicadas.
C) Armazenar dados agregados e modelados para projetos de BI específicos.
D) Armazenar os logs e metadados do processo de ETL.

**Questão 54:**

Você precisa ingerir dados de um banco de dados Cosmos DB que muda constantemente. Você quer que essas alterações estejam disponíveis para análise no Fabric com a menor latência possível e sem a necessidade de construir um pipeline de ETL. Qual recurso do Fabric é o mais indicado?

A) Atividade de Cópia agendada para cada minuto.
B) Espelhamento (Mirroring) para Cosmos DB.
C) Dataflow Gen2 com atualização incremental.
D) Atalho (Shortcut) para o Cosmos DB.

**Questão 55:**

Ao usar o comando `OPTIMIZE` em uma tabela Delta, você adiciona a cláusula `ZORDER BY (colunaA)`. O que isso faz?

A) Ordena fisicamente toda a tabela pela `colunaA`.
B) Cria um índice na `colunaA`.
C) Colocaliza os dados com valores semelhantes na `colunaA` nos mesmos arquivos, melhorando a eliminação de arquivos (data skipping) em consultas que filtram por essa coluna.
D) Compacta apenas os arquivos que contêm a `colunaA`.

**Questão 56:**

Você está processando um fluxo de eventos de login de usuários. Você quer agrupar todos os eventos de um usuário em uma única sessão, onde uma sessão é definida como uma sequência de eventos que não são interrompidos por mais de 30 minutos de inatividade. Que tipo de janela você usaria?

A) Janela Deslizante (Tumbling Window)
B) Janela Saltitante (Hopping Window)
C) Janela de Sessão (Session Window)
D) Janela de Inatividade (Idle Window)

**Questão 57:**

Qual é a principal função de uma chave substituta (surrogate key) em uma tabela de dimensão?

A) É a chave de negócio original da fonte de dados.
B) É uma chave única, geralmente um número inteiro, gerada pelo processo de ETL para identificar unicamente cada linha na tabela de dimensão, o que é crucial para implementar SCD Tipo 2.
C) É uma chave usada para criptografar os dados na tabela.
D) É uma chave estrangeira que se conecta à tabela de fatos.

**Questão 58:**

Você tem um DataFrame PySpark chamado `df_vendas` e precisa remover as linhas duplicadas com base em todas as colunas. Qual é o código correto para fazer isso?

A) `df_vendas.drop_duplicates()`
B) `df_vendas.distinct()`
C) `df_vendas.unique()`
D) Ambas A e B estão corretas.

**Questão 59:**

No KQL, qual é a função do operador `summarize`?

A) Ordenar os resultados da consulta.
B) Filtrar as linhas com base em uma condição.
C) Agrupar linhas que têm os mesmos valores em uma ou mais colunas e calcular agregações (como `count()`, `avg()`) sobre cada grupo.
D) Juntar duas tabelas.

**Questão 60:**

Você está usando um Dataflow Gen2 para carregar dados em um Lakehouse. Onde a lógica de transformação que você constrói no Power Query é executada?

A) No seu computador local.
B) Em um gateway de dados local.
C) Ela é traduzida e executada como um trabalho Spark no cluster de computação do Fabric.
D) No serviço do Power BI.

**Questão 61:**

Qual é a principal diferença entre o modo de conectividade DirectQuery e o modo DirectLake no Power BI?

A) DirectQuery se conecta a um Lakehouse, enquanto DirectLake se conecta a um Data Warehouse.
B) DirectQuery envia consultas SQL para a fonte de dados a cada interação, enquanto DirectLake lê os arquivos Delta/Parquet diretamente do OneLake sem a necessidade de traduzir para SQL, oferecendo um desempenho muito superior.
C) DirectLake importa os dados para a memória, enquanto DirectQuery não.
D) Não há diferença, são nomes diferentes para a mesma tecnologia.

**Questão 62:**

Você precisa implementar uma carga incremental em um pipeline. A tabela de origem não tem uma coluna de data de modificação, mas tem uma coluna de ID inteira que sempre aumenta. Como você pode implementar a carga incremental?

A) Não é possível sem uma coluna de data.
B) Usando o valor máximo (MAX) do ID da última carga como a marca d'água (watermark) para a próxima carga.
C) Usando o Espelhamento (Mirroring).
D) Fazendo uma carga completa a cada vez.

**Questão 63:**

Em um notebook Spark, você precisa ler dados de uma tabela SQL em um Data Warehouse do Fabric. Qual é a maneira recomendada de fazer isso?

A) Usando o conector JDBC do Spark.
B) Exportando os dados para CSV e lendo o arquivo.
C) Usando o leitor de formato `sql` nativo do Spark para Fabric: `spark.read.table("MeuWarehouse.dbo.MinhaTabela")`.
D) Usando um atalho (shortcut).

**Questão 64:**

No Eventstream, você tem um fluxo de eventos e precisa enviar os dados simultaneamente para um KQL Database (para análise em tempo real) e para um Lakehouse (para armazenamento histórico). Como você consegue isso?

A) Criando dois Eventstreams separados.
B) Adicionando dois destinos diferentes (KQL Database e Lakehouse) ao mesmo Eventstream.
C) Usando um Pipeline para copiar os dados do KQL Database para o Lakehouse.
D) Não é possível ter múltiplos destinos.

**Questão 65:**

Qual das seguintes opções é um benefício do uso de uma arquitetura Medalhão (Bronze, Prata, Ouro)?

A) Reduz o número de ferramentas necessárias para o ETL.
B) Fornece uma estrutura lógica que melhora progressivamente a qualidade e a estrutura dos dados, suportando uma variedade de casos de uso, desde a exploração de dados brutos até o BI corporativo.
C) Garante que todos os dados sejam armazenados em formato CSV.
D) Elimina a necessidade de governança de dados.

**Questão 66:**

Você está escrevendo uma consulta KQL para analisar logs. Você quer encontrar todas as linhas que contêm a palavra "error", independentemente de maiúsculas ou minúsculas. Qual operador você usaria?

A) `where message == "error"`
B) `where message contains "error"`
C) `where message has "error"`
D) `where message matches regex "(?i)error"`

**Questão 67:**

Você precisa transformar um grande volume de dados usando PySpark. O processo envolve várias junções e agregações complexas. Qual item do Fabric é o mais adequado para desenvolver e executar essa lógica?

A) Dataflow Gen2
B) Pipeline
C) Notebook
D) KQL Queryset

**Questão 68:**

O que o comando `VACUUM` faz em uma tabela Delta Lake?

A) Compacta arquivos pequenos em arquivos maiores.
B) Reordena os dados dentro dos arquivos para melhorar a compressão.
C) Remove permanentemente os arquivos de dados que não são mais referenciados pela tabela e que são mais antigos que o período de retenção, limpando o lixo e economizando custos.
D) Cria estatísticas sobre a tabela para otimizar as consultas.

**Questão 69:**

Você está usando o Spark Structured Streaming e nota que o estado da sua agregação está crescendo indefinidamente, o que pode causar problemas de memória. O que você esqueceu de configurar?

A) O número de executores do Spark.
B) O formato de saída (output format).
C) Uma marca d'água (watermark) para permitir que o Spark descarte estados antigos.
D) O modo de saída (output mode).

**Questão 70:**

Qual é a principal finalidade da camada Ouro (Gold) em uma arquitetura Medalhão?

A) Armazenar dados brutos e imutáveis.
B) Armazenar dados limpos e conformados.
C) Fornecer dados prontos para o consumo, altamente refinados e agregados, geralmente organizados em modelos dimensionais para atender a projetos de BI e análise específicos.
D) Servir como uma sandbox para cientistas de dados.

---

## Respostas e Explicações

(As respostas serão adicionadas em um arquivo separado ou no final para evitar spoilers)
_
