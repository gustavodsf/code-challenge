# code-challenge

Coletânea pessoal de exercícios de programação resolvidos em entrevistas técnicas e treinos de algoritmos em diversas plataformas (Coderbyte, CodeSignal, Codility, HackerRank, LeetCode, micro1, Turing, CoderPad, entre outras).

Os arquivos estão organizados por linguagem.

## Estrutura

```
code-challenge/
├── javascript/   # Soluções em JavaScript (Node/Browser/Angular/Express)
├── typescript/   # Soluções em TypeScript
├── python/       # Soluções em Python (+ documentação de projetos)
├── java/         # Soluções em Java (+ specs de exercícios)
├── react-jsx/    # Componentes e hooks React (JSX)
├── sql/          # Consultas SQL
├── CLAUDE.md     # Convenções e instruções para manutenção
├── README.md     # Este arquivo
└── LICENSE
```

## JavaScript (`javascript/`)

| Arquivo | Plataforma | Descrição |
|---|---|---|
| `andela_file_tree_reader.js` | Andela | Constrói uma árvore de diretórios com profundidade limitada e tamanhos acumulados. |
| `binary_search_dumb.js` | Algoritmos | Busca binária ingênua que varre do ponto médio em direção ao alvo. |
| `binary_search_smart.js` | Algoritmos | Variante otimizada da busca binária com ponto médio. |
| `code_signal_angular_books.js` | CodeSignal / Angular | Componente reativo para adicionar e remover livros de uma lista. |
| `coderbyte-node-websocket.js` | Coderbyte | Parser de eventos JSON via WebSocket com mensagens formatadas por ação. |
| `coderbyte.string.challenge.js` | Coderbyte | Matcher de wildcards customizado com tokens `+`, `*` e `*{n}`. |
| `coderbyte_BracketMatcher.js` | Coderbyte | Validação de parênteses balanceados via contador simples. |
| `codesignal.matrix.move.js` | CodeSignal | Simulação de gravidade que assenta células preenchidas até encontrar obstáculo. |
| `codesignal_increment_digit.js` | CodeSignal | Incrementa um array de dígitos in-place, tratando carry e overflow. |
| `codility_mismatch_problem.js` | Codility | Conta parênteses não casados após remover pares válidos. |
| `express-rate-limit.js` | Express / HackerRank | App Express com middleware de rate limit por IP, com headers e respostas 429. |
| `micro1_sort_packages.js` | micro1 | Tabela pacotes em faixas de CEP definidas por estações de triagem. |
| `pridelogic.js` | Pridelogic | Log com atraso, bubble sort e inserção em array. |
| `quick-sort.js` | Algoritmos | Deduplica array ordenado e aplica quicksort in-place. |
| `target.sum.js` | Algoritmos | Três abordagens (brute force, hash, two-pointer) para soma de dois números. |

## TypeScript (`typescript/`)

| Arquivo | Plataforma | Descrição |
|---|---|---|
| `coderbyte.sort.manipulate.ts` | Coderbyte | Baixa dados de API, remove duplicatas, poda campos vazios e ordena chaves. |
| `count_battleships.ts` | Matrizes | Conta navios distintos identificando células do canto superior esquerdo. |
| `hacker.hank.dynamic.array.ts` | HackerRank | Processador de queries em array dinâmico com `lastAnswer` rotativo. |

## Python (`python/`)

| Arquivo | Plataforma | Descrição |
|---|---|---|
| `asteroid-monitor.py` | HackerRank / API | Pagina busca de asteroides, filtra por ano de descoberta e flag PHA, retorna designações. |
| `asteroid-orbits-sorted.py` | HackerRank / API | Filtra asteroides por ano e classe de órbita, ordenando pelo período orbital. |
| `coderpad_ant_distance.py` | CoderPad | Distância euclidiana após movimentos diagonais da formiga codificados de 0 a 3. |
| `coderpad_version_comparation.py` | CoderPad | Compara versões semânticas pontuadas após normalizar segmentos. |
| `codility_n_bucket_problem.py` | Codility | Mínimo de trocas para alternar bolas em baldes ou retorna impossível. |
| `earning_dynamic_program.py` | Programação Dinâmica | House robber clássico maximizando ganhos não adjacentes. |
| `hacker_hank_atm.py` | HackerRank | ATM em máquina de estados finitos (login, saldo, depósito, saque). |
| `hacker_hank_face_mask_classifier.py` | HackerRank | Pipeline completo PyTorch para classificação de máscaras faciais. |
| `hacker_hank_face_mask_classifier.md` | (documentação) | Notas do projeto acima: dados, setup, treino e troubleshooting. |
| `hacker_hank_product_limit.py` | HackerRank | Limite global de instâncias com exceção `UserLimitExceeded`. |
| `leet_code_common_divisor_strings.py` | LeetCode | "Greatest Common Divisor of Strings" — encontra o maior padrão que gera ambas as strings. |
| `leet_code_merge_two_strings.py` | LeetCode | "Merge Strings Alternately" — intercala duas strings, com duas variações de implementação. |
| `odd_even_product.py` | Math | Soma dois números somente quando o produto deles é par. |
| `test_gorilla_most_commont_item.py` | TestGorilla | Item que gera maior receita em texto de transações estilo CSV. |
| `turing_frog_eat_fly.py` | Turing | Quantas moscas cada sapo alcança dado o comprimento da língua. |
| `turing_three_houses_problem.py` | Turing | Conta triplas pitagóricas com catetos ≤ n ("três casas"). |
| `xometry_credit_card.py` | Xometry | Classifica número de cartão por bandeira e inclui checagem de Luhn. |

## Java (`java/`)

| Arquivo | Plataforma | Descrição |
|---|---|---|
| `code_siginal_list_of_products_json.java` | CodeSignal | Faz fetch de JSON de produtos via HTTP e imprime nome/preço/fabricante. |
| `code_siginal_product_sum.java` | CodeSignal | Produto dos dígitos menos soma dos dígitos de um inteiro. |
| `codility_visitor_count.java` | Codility | Agrega contagens de visitas com Streams filtrando chaves e valores inválidos. |
| `ark_java_test.txt` | Ark (spec) | Requisitos para serviço Spring de empréstimos com limites de crédito. |

## React / JSX (`react-jsx/`)

| Arquivo | Plataforma | Descrição |
|---|---|---|
| `coderbyte.context.api.jsx` | Coderbyte | Uso de Context para alternar a linguagem de programação favorita. |
| `codility_react_component_click.jsx` | Codility | Contador como class component, inicializa em 42 com botão estilizado. |
| `micro1_custom_hook.jsx` | micro1 | Hook `useFetch` customizado alimentando tabela de produtos com loading states. |

## SQL (`sql/`)

| Arquivo | Plataforma | Descrição |
|---|---|---|
| `sql_daily_wages.sql` | SQL | Calcula salários devidos por trabalhador somando horas e saldos anteriores. |

## Como rodar

Cada arquivo é tipicamente um snippet autossuficiente, sem dependências de build. Para rodar:

- **JavaScript**: `node javascript/<arquivo>.js` (o `express-rate-limit.js` requer `npm install express`)
- **TypeScript**: `npx ts-node typescript/<arquivo>.ts` (ou compilar com `tsc`)
- **Python**: `python3 python/<arquivo>.py` (alguns scripts exigem dependências: `torch`/`torchvision`/`PIL` para o classificador de máscaras; `requests` para os asteroid-*)
- **Java**: `javac java/<arquivo>.java && java <NomeDaClasse>`
- **React/JSX**: snippets de referência — copie para um projeto React com Babel/Vite para executar
- **SQL**: execute o conteúdo em qualquer engine SQL compatível

## Licença

Veja [LICENSE](LICENSE).
