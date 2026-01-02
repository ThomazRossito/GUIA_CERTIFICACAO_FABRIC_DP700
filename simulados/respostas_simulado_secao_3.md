# Respostas e Explicações - Simulado Seção 3

**Questão 71: B) O Hub de Monitoramento (Monitoring Hub).**
- **Explicação:** O Hub de Monitoramento é a ferramenta centralizada no Fabric para visualizar o histórico de execuções e o status de itens como pipelines, dataflows e notebooks.

**Questão 72: B) Clicando no ícone de detalhes da atividade do notebook para visualizar seus logs de execução.**
- **Explicação:** Dentro da visualização de execução do pipeline no Hub de Monitoramento, cada atividade tem um link para seus detalhes. Para uma atividade de notebook, isso leva aos logs completos do Spark, incluindo a mensagem de erro e o stack trace.

**Questão 73: B) Nas configurações do modelo semântico, na seção de atualização agendada.**
- **Explicação:** O serviço do Power BI (integrado ao Fabric) tem uma opção nativa nas configurações de atualização agendada para enviar notificações por e-mail aos proprietários do modelo semântico em caso de falha.

**Questão 74: B) Executar o comando `OPTIMIZE` para compactar os arquivos pequenos em arquivos maiores.**
- **Explicação:** O problema de "arquivos pequenos" é um gargalo de desempenho clássico em data lakes. O comando `OPTIMIZE` resolve isso executando a compactação (compaction), o que reduz a sobrecarga de metadados e melhora a velocidade de leitura.

**Questão 75: B) Colocaliza fisicamente os dados relacionados nos mesmos arquivos, permitindo uma eliminação de arquivos (data skipping) mais eficiente durante as consultas.**
- **Explicação:** Z-Ordering é uma técnica de layout de dados que organiza os dados de forma multidimensional. Quando você filtra por uma coluna que faz parte do Z-Order, o Spark pode pular um grande número de arquivos que não contêm os dados relevantes.

**Questão 76: D) DirectLake**
- **Explicação:** O modo DirectLake é uma inovação do Fabric que permite ao motor do Power BI ler os dados diretamente do formato Delta no OneLake, evitando a necessidade de importação ou de tradução de consultas (como no DirectQuery), alcançando assim o melhor dos dois mundos: desempenho e atualização em tempo real.

**Questão 77: B) Aumentar o tamanho da memória dos nós (usando uma família de nós maior) ou aumentar o número de nós no Pool do Spark.**
- **Explicação:** Um erro de "Out of Memory" indica que o trabalho não tem recursos de memória suficientes. A solução direta é fornecer mais memória, seja usando nós maiores (mais RAM por nó) ou mais nós (distribuindo a carga).

**Questão 78: C) Data Activator**
- **Explicação:** O Data Activator é o componente do Fabric projetado para agir com base nos seus dados. Ele monitora os dados (de modelos semânticos ou eventstreams) e dispara ações (como alertas) quando condições específicas são atendidas.

**Questão 79: B) Para fornecer ao otimizador de consultas informações sobre a distribuição dos dados, ajudando-o a criar planos de execução de consulta mais eficientes.**
- **Explicação:** O otimizador de consultas usa estatísticas (como histogramas de valores, número de valores distintos, etc.) para tomar decisões inteligentes sobre como executar uma consulta (ex: qual tipo de junção usar, a ordem das tabelas).

**Questão 80: D) Todas as anteriores.**
- **Explicação:** Escalar o gateway (B) aumenta a capacidade de processamento. Compactar os dados (C) reduz a quantidade de dados a serem transferidos. Diminuir as cópias paralelas (A) pode ajudar se o sistema de origem estiver sobrecarregado, mas em geral, aumentar o paralelismo otimiza a velocidade.

**Questão 81: B) Remove permanentemente arquivos de dados antigos que não são mais referenciados pela tabela, ajudando a economizar custos de armazenamento.**
- **Explicação:** `VACUUM` é o comando de limpeza do Delta Lake. Ele remove arquivos órfãos que resultam de operações de `OPTIMIZE`, `MERGE`, etc., e que já passaram do período de retenção.

**Questão 82: B) Na interface de usuário do Spark (Spark UI) associada à sessão do notebook.**
- **Explicação:** A Spark UI fornece uma visão extremamente detalhada da execução de um trabalho Spark, mostrando os jobs, estágios, tarefas, o plano de execução e onde o tempo está sendo gasto. Ela pode ser acessada a partir da visualização de execução do notebook.

**Questão 83: A) Melhora a compressão e a velocidade de leitura, reorganizando os dados dentro dos arquivos.**
- **Explicação:** V-Order é uma otimização de escrita que aplica uma ordenação especial e outras técnicas aos arquivos Parquet, resultando em arquivos menores e leituras mais rápidas pelo motor do Fabric.

**Questão 84: B) A fonte de dados foi alterada e a tabela ´Vendas2024´ foi renomeada ou excluída.**
- **Explicação:** Este erro indica que o Dataflow não conseguiu encontrar o objeto de origem que ele esperava. A causa mais comum é uma alteração no esquema da fonte de dados.

**Questão 85: C) Executar as atividades de notebook em paralelo, não as conectando sequencialmente.**
- **Explicação:** Se as atividades não têm dependência entre si, executá-las em paralelo é a maneira mais eficaz de reduzir o tempo total de execução do pipeline.

**Questão 86: A) A capacidade do motor de consulta de empurrar as operações de filtro (predicados) para o mais próximo possível da fonte de dados, reduzindo a quantidade de dados que precisam ser lidos e processados.**
- **Explicação:** Este é um conceito fundamental de otimização de banco de dados. Filtrar cedo significa processar menos dados nas etapas subsequentes, o que economiza I/O, CPU e memória.

**Questão 87: A) Usar o Analisador de Desempenho (Performance Analyzer) no Power BI Desktop para capturar e analisar as consultas DAX e SQL geradas pelos visuais.**
- **Explicação:** O Analisador de Desempenho é a principal ferramenta de diagnóstico para problemas de desempenho em relatórios do Power BI. Ele mostra a duração de cada visual e a consulta subjacente, permitindo identificar o gargalo.

**Questão 88: D) Ambas B e C podem ajudar significativamente.**
- **Explicação:** Particionar por mês (B) criaria partições mais granulares, permitindo que o Spark ignorasse todos os meses, exceto o último. Z-Ordering na coluna de data (C) ajudaria a pular arquivos dentro da partição do último mês. A combinação de ambos é uma estratégia de otimização poderosa.

**Questão 89: B) Um Gatilho (Trigger) que define a condição e a frequência da verificação.**
- **Explicação:** No Data Activator, um gatilho (trigger) é o objeto que contém a lógica: a condição a ser verificada, o item a ser monitorado e a ação a ser tomada quando a condição for atendida.

**Questão 90: C) Usar o cache em DataFrames que são grandes e/ou caros de computar e que são reutilizados várias vezes no notebook.**
- **Explicação:** O cache é mais eficaz quando evita a recomputação de um trabalho caro. Armazenar em cache um DataFrame que é usado repetidamente é o caso de uso ideal.

**Questão 91: B) A pasta de destino no ADLS Gen2 foi renomeada ou excluída, ou as permissões na fonte foram revogadas.**
- **Explicação:** Um atalho é apenas um ponteiro. Se o alvo do ponteiro for movido, excluído ou se o acesso a ele for revogado, o atalho será quebrado.

**Questão 92: B) Nas configurações do Dataflow, na seção de conexões de fonte de dados.**
- **Explicação:** O Fabric gerencia as credenciais para as conexões de forma centralizada. Para um Dataflow, você editaria a conexão relevante em suas configurações para atualizar a senha ou o token.

**Questão 93: B) O aplicativo "Fabric Capacity Metrics".**
- **Explicação:** Este é um aplicativo de modelo do Power BI que pode ser instalado e que se conecta aos dados de telemetria do seu capacity, fornecendo relatórios detalhados sobre o consumo de CUs, throttling e desempenho.

**Questão 94: B) `OPTIMIZE` compacta arquivos pequenos, enquanto `VACUUM` remove arquivos antigos que não são mais referenciados pela tabela.**
- **Explicação:** `OPTIMIZE` é sobre o layout e o desempenho dos arquivos. `VACUUM` é sobre a limpeza e o gerenciamento do armazenamento.

**Questão 95: B) O esquema da fonte de dados não corresponde ao esquema da tabela de destino (por exemplo, tentar inserir uma string em uma coluna de inteiros).**
- **Explicação:** Este é um erro clássico de ETL. A atividade de cópia falha se não conseguir converter um valor do tipo de dados de origem para o tipo de dados de destino.

**Questão 96: C) Para relatórios do Power BI sobre um Lakehouse do Fabric.**
- **Explicação:** O modo DirectLake foi projetado especificamente para ler o formato Delta nativo dos Lakehouses do Fabric, proporcionando um desempenho sem precedentes para este cenário.

**Questão 97: A) O tempo que o pipeline ficou na fila esperando por recursos de computação para serem alocados.**
- **Explicação:** A duração total do pipeline inclui o tempo de enfileiramento (se houver) e a sobrecarga de orquestração, não apenas a soma da duração das atividades.

**Questão 98: B) Colocar o filtro de tempo o mais cedo possível na consulta para reduzir o volume de dados processado nas etapas seguintes.**
- **Explicação:** Assim como o predicate pushdown em SQL, filtrar por tempo primeiro em KQL é crucial, pois as tabelas de log são geralmente particionadas ou indexadas por tempo, e isso reduz drasticamente o escopo da pesquisa.

**Questão 99: C) O Spark irá adquirir e liberar executores para um trabalho conforme a necessidade, permitindo que vários trabalhos compartilhem os recursos do pool de forma mais eficiente.**
- **Explicação:** A alocação dinâmica permite um uso mais elástico e eficiente dos recursos do pool, especialmente em ambientes onde vários usuários e trabalhos estão competindo pelos mesmos recursos.

**Questão 100: B) `SELECT * FROM minha_tabela WHERE ID_Cliente = 123;`**
- **Explicação:** O Z-Ordering otimiza o layout dos dados com base nos valores da coluna especificada. Portanto, as consultas que filtram por um valor específico nessa coluna (`WHERE ID_Cliente = ...`) se beneficiarão mais, pois o Spark poderá pular um grande número de arquivos que não contêm esse `ID_Cliente`._
