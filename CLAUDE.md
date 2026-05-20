# Instruções para o Claude — code-challenge

Este repositório guarda exercícios de programação resolvidos pelo Gustavo em entrevistas técnicas e treinos. Use este arquivo como referência rápida para manter a organização consistente quando adicionar, mover ou renomear arquivos.

## Estrutura de pastas

A organização principal é **por linguagem**:

```
code-challenge/
├── javascript/   # *.js  — Node, browser, Angular, Express
├── typescript/   # *.ts
├── python/       # *.py  (+ *.md de documentação relacionada)
├── java/         # *.java (+ specs *.txt quando aplicável)
├── react-jsx/    # *.jsx — componentes e hooks React
└── sql/          # *.sql
```

Não existe sub-pasta por plataforma — a plataforma de origem é indicada no **nome do arquivo** e no índice do `README.md`.

## Convenções de nomenclatura

Padrão: `<plataforma>_<descricao_breve>.<ext>`

Exemplos canônicos:

- `coderbyte_BracketMatcher.js`
- `codility_n_bucket_problem.py`
- `hacker_hank_atm.py`
- `leet_code_merge_two_strings.py`

Diretrizes:

1. **Prefixo de plataforma** em snake_case minúsculo: `coderbyte`, `codesignal`, `codility`, `hacker_hank`, `leet_code`, `micro1`, `turing`, `coderpad`, `andela`, `ark`, `xometry`, `test_gorilla`, `pridelogic`.
2. **Separador**: prefira `_` (snake_case). Arquivos legados usam `.` ou `-` — não renomeie só por estilo; mantenha o nome para preservar o histórico do git, a menos que o usuário peça uma normalização explícita.
3. **Sem espaços** nem caracteres acentuados.
4. **Documentação acompanha o código**: se um `.py` tem um `.md` de notas, salve os dois na mesma pasta com o mesmo prefixo.
5. **Especificações de exercício** (enunciados em `.txt` etc.) vão na pasta da linguagem da solução esperada.

## Ao adicionar um novo arquivo

1. **Identificar a linguagem** pela extensão e mover para a pasta correspondente.
2. **Adicionar uma linha na tabela apropriada do `README.md`** com colunas `Arquivo | Plataforma | Descrição`. Mantenha a descrição em uma frase curta no infinitivo ou descritivo curto, em português.
3. **Atualizar este `CLAUDE.md`** apenas se for introduzir uma nova convenção ou uma nova linguagem/pasta.
4. **Usar `git mv`** para movimentações dentro do repositório (preserva histórico). Se ocorrer um lock `.git/index.lock`, espere o git anterior terminar antes de seguir — não execute múltiplos `git mv` em paralelo.

## Linguagem das interações

O dono do repositório (Gustavo) prefere conversa em **português brasileiro**. Mantenha esse idioma em mensagens, comentários novos no `README.md` e neste arquivo. Não traduza comentários já existentes dentro dos códigos de exercício — eles refletem como o problema foi resolvido na hora.

## O que **não** fazer

- Não criar sub-pastas por plataforma dentro de cada linguagem (ex.: `javascript/coderbyte/...`). A plataforma fica no nome do arquivo.
- Não renomear arquivos existentes só para padronizar separadores — o usuário valoriza preservar o histórico de commits.
- Não apagar arquivos sem confirmação explícita.
- Não comitar `.DS_Store`, `node_modules`, ambientes virtuais Python (`venv/`, `.venv/`) ou modelos treinados (`*.pt`, `*.pth`). Se aparecerem na working tree, sugira adicioná-los ao `.gitignore`.

## Lista de plataformas conhecidas

Para coerência, use exatamente estes nomes (em português ou inglês conforme o nome original) na coluna "Plataforma" do `README.md`:

Coderbyte · CodeSignal · Codility · HackerRank · LeetCode · CoderPad · Andela · Ark · micro1 · Turing · TestGorilla · Xometry · Pridelogic · Express · Algoritmos (uso genérico para arquivos sem plataforma) · Programação Dinâmica · Math · Matrizes · API

## Verificações de qualidade após mudanças

Sempre que reorganizar, terminar com:

```bash
git status        # confirmar renames detectados
ls -1 */          # conferir distribuição por pasta
```

E garantir que toda referência cruzada em `README.md` ainda esteja correta (sem caminhos antigos da raiz).
