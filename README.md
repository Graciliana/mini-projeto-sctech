# Mini-Projeto Avaliativo - Machine Learning e Visão Computacional

## Descrição do Projeto

Este projeto foi desenvolvido como parte do Mini-Projeto Avaliativo do módulo de Machine Learning e Visão Computacional.

O desafio consiste em criar um pipeline de sanitização de dados utilizando apenas bibliotecas nativas do Python, sem o uso da biblioteca Pandas. Foram utilizados os datasets da Olist contendo informações sobre produtos e pedidos.

O objetivo é identificar e corrigir inconsistências nos dados, garantindo que eles possam ser utilizados posteriormente em análises de Business Intelligence e modelos de Machine Learning.

---

## Objetivos

O pipeline desenvolvido realiza:

* Leitura de arquivos CSV utilizando `csv.DictReader`
* Tratamento de valores ausentes
* Padronização de categorias de produtos
* Limpeza de strings utilizando Expressões Regulares (Regex)
* Conversão de datas utilizando o módulo `datetime`
* Aplicação de regras de negócio para validação de pedidos cancelados
* Geração de relatórios estatísticos
* Exportação dos dados tratados para novos arquivos CSV

---

## Estrutura do Projeto

```text
Mini-Projeto_Machine_Learning_Visao_Computacional/

├── data/
│   ├── raw/
│   │   ├── olist_products_dataset.csv
│   │   └── olist_orders_dataset.csv
│   │
│   └── processed/
│       ├── produtos_tratados.csv
│       └── orders_tratados.csv
│
├── src/
│   ├── functions.py
│   ├── products_processing.py
│   ├── orders_processing.py
│   └── main.py
│
├── README.md
└── requirements.txt
```

---

## Tecnologias Utilizadas

* Python 3
* csv
* re
* datetime

Bibliotecas utilizadas:

```python
csv
re
datetime
```

Todas fazem parte da biblioteca padrão do Python.

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acessar a pasta do projeto

```bash
cd Mini-Projeto_Machine_Learning_Visao_Computacional
```

### 3. Executar o pipeline

```bash
python src/main.py
```

### 4. Resultado

Após a execução serão gerados os arquivos:

```text
data/processed/produtos_tratados.csv
data/processed/pedidos_tratados.csv
```

Além disso, será exibido um relatório contendo:

* Quantidade de produtos processados
* Categorias corrigidas
* Dimensões corrigidas
* Quantidade de pedidos cancelados
* Inconsistências identificadas
* Datas convertidas

---

## Tratamentos Realizados

### Produtos

* Preenchimento de categorias vazias com "Sem Categoria"
* Conversão para letras minúsculas
* Remoção de espaços excedentes
* Limpeza de caracteres especiais utilizando Regex
* Tratamento de valores ausentes das dimensões físicas utilizando a média da coluna
* Criação da variável derivada `volume_cm3`

### Pedidos

* Conversão de datas para o formato brasileiro
* Verificação da relação entre pedidos cancelados e ausência de data de entrega
* Identificação de inconsistências na base

---

## Feature Engineering

Como melhoria adicional, foi criada a coluna:

```text
volume_cm3
```

Obtida através da fórmula:

Volume = Comprimento × Altura × Largura

Essa etapa representa uma técnica de Feature Engineering frequentemente utilizada em projetos de Machine Learning para enriquecer os dados e gerar novas variáveis relevantes para futuras análises.

---

## Reflexão Teórica sobre Machine Learning e Qualidade dos Dados

A qualidade dos dados é um dos fatores mais importantes para o sucesso de modelos de Machine Learning. Dados incompletos, inconsistentes ou incorretos podem levar a previsões equivocadas e comprometer a capacidade de generalização dos algoritmos.

O processo de limpeza e preparação dos dados reduz ruídos, inconsistências e valores ausentes, permitindo que os modelos aprendam padrões reais presentes na base de dados. Esse cuidado ajuda a minimizar problemas como overfitting, viés e baixa capacidade preditiva.

Além disso, técnicas de Feature Engineering, como a criação de novas variáveis derivadas, contribuem para aumentar a qualidade da informação disponível para os algoritmos, melhorando o desempenho dos modelos de Inteligência Artificial.

---

## Autora

Graciliana Kascher - <https://www.linkedin.com/in/gracilianakascher/>

Projeto desenvolvido para o Bootcamp de Machine Learning e Visão Computacional.
