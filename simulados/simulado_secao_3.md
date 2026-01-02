# Simulado - Seção 3: Monitorar e Otimizar uma Solução de Análise

**Instruções:** Responda às seguintes questões para testar seu conhecimento sobre o monitoramento e a otimização de soluções de análise no Microsoft Fabric. As respostas e explicações estão no final.

---

**Questão 71:**

Você precisa verificar o status de todas as execuções de pipelines e dataflows que ocorreram nas últimas 24 horas em seu workspace. Qual é o local centralizado no Microsoft Fabric para encontrar essa informação?

A) O portal do Microsoft Purview.
B) O Hub de Monitoramento (Monitoring Hub).
C) A página de configurações do Capacity.
D) Os logs de diagnóstico do OneLake.

**Questão 72:**

Um pipeline que executa um notebook falhou. No Hub de Monitoramento, você clica na execução do pipeline com falha. Onde você encontraria a mensagem de erro específica e o stack trace do notebook?

A) Na aba de "Saída" (Output) da atividade de cópia.
B) Clicando no ícone de detalhes da atividade do notebook para visualizar seus logs de execução.
C) Nas configurações do Pool do Spark.
D) Nos logs de auditoria do Microsoft 365.

**Questão 73:**

Você quer ser notificado por e-mail sempre que a atualização agendada de um modelo semântico falhar. Onde você pode configurar este tipo de alerta?

A) No Hub de Monitoramento.
B) Nas configurações do modelo semântico, na seção de atualização agendada.
C) Criando uma regra de alerta no Azure Monitor.
D) Usando o Data Activator para monitorar o status da atualização.

**Questão 74:**

Você está investigando por que as consultas em uma tabela Delta no seu Lakehouse estão lentas. Ao listar os arquivos da tabela, você percebe que ela é composta por dezenas de milhares de arquivos pequenos. Qual ação de otimização teria o maior impacto na melhoria do desempenho da leitura?

A) Executar o comando `VACUUM` na tabela.
B) Executar o comando `OPTIMIZE` para compactar os arquivos pequenos em arquivos maiores.
C) Aumentar o número de nós no Pool do Spark.
D) Habilitar o V-Order na tabela.

**Questão 75:**

O que a técnica de otimização Z-Ordering faz em uma tabela Delta Lake?

A) Criptografa os dados para maior segurança.
B) Colocaliza fisicamente os dados relacionados nos mesmos arquivos, permitindo uma eliminação de arquivos (data skipping) mais eficiente durante as consultas.
C) Converte a tabela para o formato Parquet.
D) Remove permanentemente os dados antigos da tabela.

**Questão 76:**

Você tem um relatório do Power BI que consulta um Lakehouse. Para obter o melhor desempenho de consulta possível, combinando a velocidade do modo de Importação com a atualização em tempo real do DirectQuery, qual modo de conectividade do modelo semântico você deve usar?

A) Import
B) DirectQuery
C) Live Connection
D) DirectLake

**Questão 77:**

Um trabalho do Spark está falhando com um erro de "Out of Memory" (OOM). Qual das seguintes ações é uma solução válida para este problema?

A) Diminuir o número de partições do DataFrame.
B) Aumentar o tamanho da memória dos nós (usando uma família de nós maior) ou aumentar o número de nós no Pool do Spark.
C) Usar o comando `VACUUM` na tabela de origem.
D) Mudar a linguagem do notebook de PySpark para Scala.

**Questão 78:**

Você precisa ser alertado sempre que o número de transações fraudulentas detectadas em um fluxo de dados em tempo real exceder 10 por minuto. Qual item do Fabric é projetado especificamente para criar esse tipo de alerta acionável com base em dados?

A) Hub de Monitoramento
B) Pipeline
C) Data Activator
D) Log de Atividades do Workspace

**Questão 79:**

Qual é o propósito de criar estatísticas (`CREATE STATISTICS`) em colunas de um Data Warehouse do Fabric?

A) Para impor a unicidade dos valores na coluna.
B) Para fornecer ao otimizador de consultas informações sobre a distribuição dos dados, ajudando-o a criar planos de execução de consulta mais eficientes.
C) Para mascarar os dados na coluna.
D) Para auditar o acesso à coluna.

**Questão 80:**

Um pipeline que copia dados de um sistema de origem local para o Fabric está lento. O gateway de dados local está sobrecarregado. Qual das seguintes opções pode ajudar a otimizar o desempenho da ingestão?

A) Diminuir o número de cópias paralelas na atividade de cópia.
B) Escalar horizontalmente o gateway de dados, instalando-o em vários computadores.
C) Compactar os dados antes de enviá-los pelo gateway.
D) Todas as anteriores.

**Questão 81:**

O que o comando `VACUUM` faz em uma tabela Delta Lake?

A) Compacta arquivos pequenos em arquivos maiores.
B) Remove permanentemente arquivos de dados antigos que não são mais referenciados pela tabela, ajudando a economizar custos de armazenamento.
C) Reordena os dados dentro dos arquivos.
D) Analisa a tabela para coletar estatísticas.

**Questão 82:**

Você está monitorando a execução de um notebook e vê que uma célula específica está demorando muito para ser executada. Onde você pode ver os detalhes dos trabalhos e estágios do Spark associados a essa célula para um diagnóstico mais aprofundado?

A) No Hub de Monitoramento.
B) Na interface de usuário do Spark (Spark UI) associada à sessão do notebook.
C) Nos logs de auditoria do Fabric.
D) Nas configurações do Ambiente do Spark.

**Questão 83:**

Qual é a principal vantagem do V-Order, a otimização de escrita do Fabric para arquivos Parquet?

A) Melhora a compressão e a velocidade de leitura, reorganizando os dados dentro dos arquivos.
B) Garante a conformidade com o GDPR.
C) Permite transações ACID em arquivos Parquet.
D) Converte arquivos CSV para Parquet automaticamente.

**Questão 84:**

Um Dataflow Gen2 está falhando. A mensagem de erro no histórico de atualização diz "Não foi possível encontrar a tabela 'Vendas2024'". Qual é a causa mais provável do erro?

A) O Pool do Spark do workspace está parado.
B) A fonte de dados foi alterada e a tabela 'Vendas2024' foi renomeada ou excluída.
C) As credenciais para a fonte de dados expiraram.
D) O gateway de dados está offline.

**Questão 85:**

Você precisa otimizar um pipeline que executa várias atividades de notebook que não dependem umas das outras. Qual é a melhor maneira de acelerar a execução geral do pipeline?

A) Executar todas as atividades em sequência.
B) Aumentar o tempo de timeout de cada atividade.
C) Executar as atividades de notebook em paralelo, não as conectando sequencialmente.
D) Colocar todas as atividades em um único notebook.

**Questão 86:**

O que significa "predicate pushdown" no contexto da otimização de consultas?

A) A capacidade do motor de consulta de empurrar as operações de filtro (predicados) para o mais próximo possível da fonte de dados, reduzindo a quantidade de dados que precisam ser lidos e processados.
B) A capacidade de converter consultas DAX em consultas SQL.
C) A prática de mover a lógica de transformação do Power Query para o SQL.
D) A habilidade de executar consultas em paralelo.

**Questão 87:**

Um usuário reclama que um relatório do Power BI está lento. O relatório usa o modo DirectQuery para um Data Warehouse do Fabric. Qual é o primeiro passo para diagnosticar o problema?

A) Usar o Analisador de Desempenho (Performance Analyzer) no Power BI Desktop para capturar e analisar as consultas DAX e SQL geradas pelos visuais.
B) Reiniciar o Capacity do Fabric.
C) Verificar o Hub de Monitoramento do Fabric.
D) Executar o comando `OPTIMIZE` no Data Warehouse.

**Questão 88:**

Você tem uma tabela Delta com 10 anos de dados, particionada por ano. Uma consulta que filtra apenas os dados do último mês está lenta. Você suspeita que o Spark está lendo mais arquivos do que o necessário. Qual otimização ajudaria o Spark a pular (skip) os arquivos de anos anteriores de forma mais eficiente?

A) Usar o comando `VACUUM`.
B) Particionar a tabela por mês em vez de ano.
C) Usar `Z-ORDER BY` na coluna de data completa.
D) Ambas B e C podem ajudar significativamente.

**Questão 89:**

Você configurou um alerta no Data Activator para ser notificado via Teams quando o número de erros de ingestão exceder 5 em uma hora. O que você precisa configurar no Data Activator para que ele saiba como verificar essa condição?

A) Um Pipeline
B) Um Gatilho (Trigger) que define a condição e a frequência da verificação.
C) Um Eventstream
D) Um Atalho (Shortcut)

**Questão 90:**

Qual é uma boa prática ao usar o cache (`.cache()`) em um notebook Spark?

A) Usar o cache em todos os DataFrames que você criar.
B) Usar o cache em DataFrames pequenos que são usados apenas uma vez.
C) Usar o cache em DataFrames que são grandes e/ou caros de computar e que são reutilizados várias vezes no notebook.
D) Evitar o uso de cache, pois ele sempre degrada o desempenho.

**Questão 91:**

Um atalho (shortcut) para uma pasta no ADLS Gen2 para de funcionar. Qual das seguintes opções é uma causa provável?

A) O Pool do Spark do workspace foi pausado.
B) A pasta de destino no ADLS Gen2 foi renomeada ou excluída, ou as permissões na fonte foram revogadas.
C) O V-Order foi desabilitado no Lakehouse.
D) O Hub de Monitoramento está cheio.

**Questão 92:**

Você está tentando resolver um erro de "credenciais inválidas" em um Dataflow Gen2. Onde você deve ir para atualizar as credenciais usadas para se conectar à fonte de dados?

A) Nas configurações do workspace.
B) Nas configurações do Dataflow, na seção de conexões de fonte de dados.
C) No portal do Microsoft Entra ID (anteriormente Azure Active Directory).
D) No editor do Power Query, na consulta M.

**Questão 93:**

Você precisa monitorar o uso da capacidade (Capacity Units - CUs) do seu Fabric Capacity para identificar gargalos e otimizar os custos. Qual ferramenta fornece uma visão detalhada do consumo de CU por tipo de item e por usuário?

A) O Hub de Monitoramento.
B) O aplicativo "Fabric Capacity Metrics".
C) O log de atividades do workspace.
D) O portal do Azure.

**Questão 94:**

Ao otimizar uma tabela Delta, qual a diferença entre `OPTIMIZE` e `VACUUM`?

A) `OPTIMIZE` remove arquivos antigos, enquanto `VACUUM` compacta arquivos pequenos.
B) `OPTIMIZE` compacta arquivos pequenos, enquanto `VACUUM` remove arquivos antigos que não são mais referenciados pela tabela.
C) Ambos fazem a mesma coisa.
D) `OPTIMIZE` é para tabelas pequenas e `VACUUM` é para tabelas grandes.

**Questão 95:**

Um pipeline falha em uma atividade de cópia com um erro de "tipo de dados incompatível". O que isso geralmente significa?

A) O Pool do Spark não tem memória suficiente.
B) O esquema da fonte de dados não corresponde ao esquema da tabela de destino (por exemplo, tentar inserir uma string em uma coluna de inteiros).
C) As credenciais da fonte de dados expiraram.
D) O gateway de dados está offline.

**Questão 96:**

Para qual cenário o modo DirectLake é mais benéfico?

A) Para relatórios do Power BI sobre um banco de dados Oracle local.
B) Para relatórios do Power BI sobre um Data Warehouse do Fabric.
C) Para relatórios do Power BI sobre um Lakehouse do Fabric.
D) Para relatórios paginados.

**Questão 97:**

Você está analisando os logs de um pipeline no Hub de Monitoramento. Você vê que a duração total do pipeline foi de 10 minutos, mas a soma das durações de cada atividade individual é de apenas 6 minutos. O que poderia explicar os 4 minutos de diferença?

A) O tempo que o pipeline ficou na fila esperando por recursos de computação para serem alocados.
B) Um erro nos logs de monitoramento.
C) O tempo gasto para fazer o commit das alterações no Git.
D) O tempo de execução de gatilhos de evento.

**Questão 98:**

Você precisa otimizar uma consulta KQL que filtra uma grande tabela de logs por um intervalo de tempo. Qual é a melhor prática?

A) Colocar o filtro de tempo (`where Timestamp between (...)`) no final da consulta.
B) Colocar o filtro de tempo o mais cedo possível na consulta para reduzir o volume de dados processado nas etapas seguintes.
C) Evitar filtrar por tempo, pois é uma operação lenta.
D) Usar o operador `search` em vez de `where` para filtros de tempo.

**Questão 99:**

Seu Pool do Spark está configurado com alocação dinâmica de executores habilitada. O que isso significa para seus trabalhos do Spark?

A) O número de nós no pool aumentará e diminuirá automaticamente.
B) Cada trabalho do Spark usará todos os nós disponíveis no pool, o tempo todo.
C) O Spark irá adquirir e liberar executores para um trabalho conforme a necessidade, permitindo que vários trabalhos compartilhem os recursos do pool de forma mais eficiente.
D) A versão do Spark será atualizada dinamicamente.

**Questão 100:**

Você executou o comando `OPTIMIZE minha_tabela ZORDER BY (ID_Cliente)`. Qual tipo de consulta se beneficiará mais com essa otimização?

A) `SELECT * FROM minha_tabela;`
B) `SELECT * FROM minha_tabela WHERE ID_Cliente = 123;`
C) `SELECT * FROM minha_tabela ORDER BY Data_Venda;`
D) `SELECT COUNT(*) FROM minha_tabela;`

---

## Respostas e Explicações

(As respostas serão adicionadas em um arquivo separado ou no final para evitar spoilers)
_
