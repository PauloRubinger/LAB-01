# LAB-01 — Análise de Repositórios Populares no GitHub

## Visão geral

Este projeto reúne a coleta, o processamento e a análise de dados de repositórios populares do GitHub, com foco em identificar padrões relacionados à maturidade, manutenção ativa, contribuição da comunidade e qualidade de gestão de issues.

A amostra foi composta pelos 1.000 repositórios com maior número de estrelas, e a análise foi conduzida com base em métricas quantitativas extraídas por meio da API do GitHub.

O trabalho foi documentado em detalhes no relatório final em [reports/final.md](reports/final.md), e os principais resultados também estão disponíveis em gráficos e tabelas na pasta [reports/figures](reports/figures).

---

## Objetivo do estudo

Analisar características dos repositórios mais populares do GitHub para verificar se existe uma relação entre popularidade e fatores como:

- maturidade e idade do projeto;
- atividade de contribuição externa;
- frequência de releases;
- frequência de atualização;
- linguagem principal;
- percentual de issues fechadas.

---

## Questões de pesquisa

### RQ01 — Sistemas populares são maduros ou antigos?
Métrica: idade do repositório.

### RQ02 — Sistemas populares recebem muita contribuição externa?
Métrica: número de pull requests aceitas.

### RQ03 — Sistemas populares lançam releases com frequência?
Métrica: número total de releases.

### RQ04 — Sistemas populares são atualizados com frequência?
Métrica: tempo desde a última atualização.

### RQ05 — Sistemas populares são escritos nas linguagens mais populares?
Métrica: linguagem principal do repositório.

### RQ06 — Sistemas populares possuem um alto percentual de issues fechadas?
Métrica: razão entre issues fechadas e total de issues.

---

## Hipóteses

Antes da análise dos dados, foram formuladas as seguintes hipóteses:

- repositórios populares tendem a ser mais antigos;
- projetos populares recebem mais contribuições externas;
- projetos populares publicam releases com regularidade;
- projetos populares são atualizados com frequência;
- projetos populares usam linguagens amplamente adotadas;
- projetos populares têm gestão eficiente de issues.

---

## Metodologia

### Coleta de dados

A coleta foi realizada usando a API GraphQL do GitHub, consultando repositórios ordenados por número de estrelas.

### Estrutura do conjunto de dados

Os dados foram armazenados em CSV e incluem:

- proprietário e nome do repositório;
- número de estrelas;
- data de criação e última atualização;
- linguagem principal;
- número de pull requests mergeados;
- número de releases;
- total de issues;
- número de issues fechadas.

### Métricas derivadas

Além dos campos originais, foram calculadas métricas derivadas como:

- idade do repositório em anos;
- tempo desde a última atualização em horas;
- razão de issues fechadas em relação ao total de issues.

### Técnica estatística

A mediana foi escolhida como medida de tendência central porque é menos sensível a valores extremos do que a média.

---

## Estrutura do repositório

- [src/main.py](src/main.py) — ponto de entrada do processo de coleta.
- [src/github_api/client.py](src/github_api/client.py) — cliente HTTP para a API do GitHub.
- [src/github_api/query.py](src/github_api/query.py) — definição da query GraphQL para buscar repositórios.
- [src/github_api/pagination.py](src/github_api/pagination.py) — lógica de paginação da busca.
- [src/processing/metrics.py](src/processing/metrics.py) — cálculo das métricas e geração dos gráficos.
- [src/analysis/analyze.py](src/analysis/analyze.py) — análise exploratória e geração de visualizações.
- [data/raw/repos_1000.csv](data/raw/repos_1000.csv) — dados brutos dos repositórios coletados.
- [data/processed/medians.csv](data/processed/medians.csv) — medianas das métricas principais.
- [reports/final.md](reports/final.md) — relatório final completo do trabalho.
- [reports/draft.md](reports/draft.md) — rascunho e versões preliminares da análise.
- [reports/figures](reports/figures) — gráficos produzidos na análise.

---

## Resultados principais

Os dados coletados indicam que os repositórios populares tendem a:

- ser relativamente antigos; a mediana da idade foi de aproximadamente 8,34 anos;
- receber contribuições externas relevantes; a mediana de pull requests aceitas foi de 738;
- manter ciclos de releases; a mediana foi de 40 releases;
- apresentar manutenção frequente; a mediana do tempo desde a última atualização foi de 1,03 horas;
- possuir elevado índice de resolução de issues; a mediana da razão de issues fechadas foi de 0,88.

### Medianas observadas

| Métrica | Mediana |
|---|---:|
| Idade do repositório | 8,34 anos |
| Pull requests aceitas | 738 |
| Releases | 40 |
| Tempo desde última atualização | 1,03 horas |
| Razão de issues fechadas | 0,88 |

---

## Como executar

1. Configure a variável de ambiente `GITHUB_TOKEN` com um token válido do GitHub.
2. Instale as dependências do projeto:

   pip install -r requirements.txt

3. Execute a coleta de dados:

   python src/main.py

4. Gere os gráficos e a análise estatística:

   python src/analysis/analyze.py

> O projeto já inclui os dados coletados e os artefatos gerados em [data](data) e [reports](reports), então a etapa de coleta pode ser reutilizada conforme necessário.

---

## Observações finais

A conclusão do estudo sugere que a popularidade em repositórios do GitHub está fortemente associada a maturidade, manutenção ativa, presença de comunidade contribuindo e boa organização do projeto. O relatório completo detalha esses achados e aporta interpretações quantitativas e visuais dos dados analisados.

Para detalhes completos do experimento, veja [reports/final.md](reports/final.md).
