# Respostas e Explicações - Simulado Seção 2

**Questão 36: B) Carga Incremental (Incremental Load) usando a coluna `LastModifiedDate` como marca d'água (watermark).**
- **Explicação:** Para grandes volumes de dados, a carga incremental é muito mais eficiente do que a carga completa, pois processa apenas os dados novos ou alterados. A coluna `LastModifiedDate` é a candidata perfeita para ser usada como marca d'água.

**Questão 37: B) Conter os atributos descritivos e contextuais (como nome do cliente, categoria do produto) que são usados para filtrar e agrupar os dados de fato.**
- **Explicação:** As tabelas de dimensão fornecem o "quem, o quê, onde, quando, por quê" dos dados. Elas contêm os atributos pelos quais as métricas nas tabelas de fato são analisadas.

**Questão 38: C) SCD Tipo 2**
- **Explicação:** O SCD Tipo 2 (Slowly Changing Dimension Tipo 2) é projetado especificamente para manter um histórico completo das alterações, criando uma nova linha para cada mudança em um atributo rastreado.

**Questão 39: B) Fornece transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade), o que permite operações confiáveis de `MERGE`, `UPDATE` e `DELETE` em um data lake.**
- **Explicação:** A principal vantagem do Delta Lake sobre formatos como o Parquet puro é a adição de um log de transações que traz confiabilidade e operações de nível de banco de dados para o data lake.

**Questão 40: C) Eventstream e KQL Database**
- **Explicação:** O Eventstream é a ferramenta de ingestão e processamento de streaming low-code do Fabric, e o KQL Database é o banco de dados otimizado para análise interativa de dados de telemetria e séries temporais em tempo real.

**Questão 41: B) Atalho (Shortcut)**
- **Explicação:** Atalhos são ponteiros virtuais que permitem acessar dados em fontes externas (como S3, ADLS Gen2, ou outros workspaces) sem movê-los, tratando-os como se fossem locais.

**Questão 42: B) Criar uma réplica somente leitura e continuamente sincronizada de um banco de dados operacional (como Azure SQL DB ou Snowflake) no OneLake.**
- **Explicação:** O Espelhamento (Mirroring) replica dados de bancos de dados operacionais para o OneLake em tempo quase real, disponibilizando-os para análise no Fabric sem a necessidade de ETL e sem impactar a fonte.

**Questão 43: B) `.cache()`**
- **Explicação:** O método `.cache()` (ou `.persist()`) armazena o DataFrame na memória dos executores do Spark. Quando o DataFrame é usado novamente, o Spark o lê da memória em vez de recalculá-lo, economizando tempo de processamento.

**Questão 44: B) Janela Saltitante (Hopping Window)**
- **Explicação:** Uma janela saltitante é definida por seu tamanho (10 minutos) e seu intervalo de avanço (5 minutos), o que causa sobreposição. É exatamente o que o cenário descreve.

**Questão 45: A) Substituir Valores (Replace Values)**
- **Explicação:** A transformação "Substituir Valores" no Power Query permite encontrar um valor (neste caso, `null`) e substituí-lo por outro (neste caso, `0`). A transformação "Preencher" é usada para copiar valores para cima ou para baixo para preencher nulos.

**Questão 46: C) `MERGE`**
- **Explicação:** A instrução `MERGE` é um padrão SQL poderoso projetado para sincronizar duas tabelas, executando `INSERT` para linhas novas, `UPDATE` para linhas correspondentes e, opcionalmente, `DELETE` para linhas que não existem mais na origem.

**Questão 47: A) Janela Deslizante (Tumbling Window)**
- **Explicação:** Janelas deslizantes são de tamanho fixo e não se sobrepõem, o que corresponde à necessidade de agregar dados em intervalos de tempo distintos e contíguos.

**Questão 48: B) `OPTIMIZE`**
- **Explicação:** O comando `OPTIMIZE` no Delta Lake executa a compactação de arquivos (compaction), que combina arquivos pequenos em arquivos maiores para melhorar o desempenho da leitura.

**Questão 49: C) `join` ou `lookup`**
- **Explicação:** O operador `join` (no Eventstream ou Spark) ou `lookup` (em KQL) é usado para enriquecer um conjunto de dados, adicionando colunas de outro conjunto de dados com base em uma chave comum.

**Questão 50: B) O Lakehouse usa o motor Spark e armazena dados em formato Delta (arquivos), sendo ideal para engenharia de dados e IA, enquanto o Data Warehouse usa um motor T-SQL e um formato de coluna proprietário, sendo otimizado para análise de BI e SQL.**
- **Explicação:** Esta é a distinção fundamental. O Lakehouse abraça o paradigma de "data lake aberto" com Spark, enquanto o Data Warehouse oferece uma experiência de banco de dados relacional MPP tradicional com T-SQL.

**Questão 51: A) `.withWatermark("eventTime", "10 minutes")`**
- **Explicação:** A marca d'água (`withWatermark`) informa ao Spark Structured Streaming o quão atrasados os dados podem chegar. Isso permite que o motor descarte com segurança o estado de agregações antigas, evitando que o estado cresça indefinidamente.

**Questão 52: C) M**
- **Explicação:** A linguagem M é a linguagem de fórmulas por trás do Power Query. Cada etapa na interface gráfica gera uma expressão M correspondente.

**Questão 53: B) Armazenar dados limpos, conformados e enriquecidos, onde os tipos de dados foram corrigidos e regras de validação foram aplicadas.**
- **Explicação:** A camada Prata pega os dados brutos da Bronze e os transforma em um ativo de dados confiável e consultável, resolvendo problemas de qualidade e padronizando esquemas.

**Questão 54: B) Espelhamento (Mirroring) para Cosmos DB.**
- **Explicação:** O Espelhamento é a solução ideal para este caso, pois replica os dados do Cosmos DB para o OneLake em tempo quase real e sem a necessidade de ETL, tornando os dados imediatamente disponíveis para análise.

**Questão 55: C) Colocaliza os dados com valores semelhantes na `colunaA` nos mesmos arquivos, melhorando a eliminação de arquivos (data skipping) em consultas que filtram por essa coluna.**
- **Explicação:** Z-Ordering é uma técnica de layout de dados que organiza os dados de forma multidimensional. Isso permite que o Spark pule um número muito maior de arquivos quando uma consulta filtra pelas colunas usadas no Z-Order.

**Questão 56: C) Janela de Sessão (Session Window)**
- **Explicação:** Janelas de sessão são projetadas especificamente para agrupar eventos com base em períodos de atividade, separados por uma lacuna de inatividade (timeout).

**Questão 57: B) É uma chave única, geralmente um número inteiro, gerada pelo processo de ETL para identificar unicamente cada linha na tabela de dimensão, o que é crucial para implementar SCD Tipo 2.**
- **Explicação:** A chave substituta desacopla o data warehouse dos sistemas de origem e permite o rastreamento de histórico, pois a chave de negócio pode não ser mais única quando se implementa o SCD Tipo 2.

**Questão 58: D) Ambas A e B estão corretas.**
- **Explicação:** Em PySpark, `distinct()` é um alias para `drop_duplicates()`. Ambos os métodos retornam um novo DataFrame com as linhas duplicadas removidas.

**Questão 59: C) Agrupar linhas que têm os mesmos valores em uma ou mais colunas e calcular agregações (como `count()`, `avg()`) sobre cada grupo.**
- **Explicação:** `summarize` é o principal operador de agregação em KQL, análogo ao `GROUP BY` em SQL.

**Questão 60: C) Ela é traduzida e executada como um trabalho Spark no cluster de computação do Fabric.**
- **Explicação:** Uma das principais melhorias do Dataflow Gen2 é que ele usa o poder de computação do Fabric (Spark) para executar as transformações, permitindo um desempenho muito maior do que a geração anterior.

**Questão 61: B) DirectQuery envia consultas SQL para a fonte de dados a cada interação, enquanto DirectLake lê os arquivos Delta/Parquet diretamente do OneLake sem a necessidade de traduzir para SQL, oferecendo um desempenho muito superior.**
- **Explicação:** DirectLake é uma inovação fundamental. Ele combina a atualização em tempo real do DirectQuery com o desempenho do modo de Importação, lendo diretamente o formato Delta nativo do Lakehouse.

**Questão 62: B) Usando o valor máximo (MAX) do ID da última carga como a marca d'água (watermark) para a próxima carga.**
- **Explicação:** Qualquer coluna que aumente monotonicamente (como uma coluna de ID sequencial) pode ser usada como uma marca d'água para cargas incrementais.

**Questão 63: C) Usando o leitor de formato `sql` nativo do Spark para Fabric: `spark.read.table("MeuWarehouse.dbo.MinhaTabela")`.**
- **Explicação:** O Fabric fornece uma integração nativa e otimizada entre o Spark e o Data Warehouse, permitindo a leitura e escrita de tabelas diretamente usando a sintaxe `spark.read.table()` e `df.write.saveAsTable()`.

**Questão 64: B) Adicionando dois destinos diferentes (KQL Database e Lakehouse) ao mesmo Eventstream.**
- **Explicação:** O Eventstream foi projetado para ser um roteador de eventos, permitindo que um único fluxo de entrada seja enviado para múltiplos destinos simultaneamente.

**Questão 65: B) Fornece uma estrutura lógica que melhora progressivamente a qualidade e a estrutura dos dados, suportando uma variedade de casos de uso, desde a exploração de dados brutos até o BI corporativo.**
- **Explicação:** A arquitetura Medalhão organiza o data lake em zonas de qualidade crescente, o que traz ordem, governança e suporta diferentes tipos de consumidores de dados.

**Questão 66: C) `where message has "error"`**
- **Explicação:** Em KQL, o operador `has` é otimizado para pesquisar por um termo completo de forma insensível a maiúsculas e minúsculas. `contains` procura por uma substring e é mais lento.

**Questão 67: C) Notebook**
- **Explicação:** Notebooks oferecem um ambiente de desenvolvimento "code-first" com o poder e a flexibilidade do PySpark, tornando-os a ferramenta ideal para transformações de dados complexas e em larga escala.

**Questão 68: C) Remove permanentemente os arquivos de dados que não são mais referenciados pela tabela e que são mais antigos que o período de retenção, limpando o lixo e economizando custos.**
- **Explicação:** `VACUUM` é o comando de limpeza do Delta Lake. Ele remove arquivos órfãos que não fazem mais parte de nenhuma versão da tabela, ajudando a gerenciar os custos de armazenamento.

**Questão 69: C) Uma marca d'água (watermark) para permitir que o Spark descarte estados antigos.**
- **Explicação:** Em agregações de streaming, uma marca d'água é essencial para limitar a quantidade de estado que o Spark precisa manter, permitindo que ele descarte com segurança os dados de janelas que são muito antigas para receber dados atrasados.

**Questão 70: C) Fornecer dados prontos para o consumo, altamente refinados e agregados, geralmente organizados em modelos dimensionais para atender a projetos de BI e análise específicos.**
- **Explicação:** A camada Ouro é a camada de consumo. Ela pega os dados limpos da Prata e os modela para casos de uso de negócios específicos, garantindo o melhor desempenho e facilidade de uso para os analistas._
