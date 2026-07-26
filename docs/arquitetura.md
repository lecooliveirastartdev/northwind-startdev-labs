# Arquitetura Planejada

# 🏗️ Arquitetura do Projeto Northwind

## Visão Geral

Este projeto tem como objetivo construir um pipeline de dados utilizando a base Northwind, simulando um cenário real de Engenharia de Dados.

A proposta é transformar dados transacionais em informações analíticas para apoiar decisões de negócio.

---

# Fonte de Dados

## Banco Original

Tecnologia:

- SQLite

Arquivo:


data/raw/Northwind_small.sqlite


Características:

- Base de dados simulando sistema comercial;
- Contém informações de clientes, produtos, pedidos e funcionários;
- Utilizada como camada inicial do pipeline.

---

# Arquitetura Planejada


Northwind SQLite
|
↓
Extração com Python
(Pandas / Polars)
|
↓
Data Lake
(Arquivos Parquet)
|
↓
DuckDB
(Data Warehouse Analítico)
|
↓
Modelagem SQL
(dbt)
|
↓
Dashboard BI
(Metabase)


---

# Tecnologias

## Linguagem

- Python

## Manipulação de Dados

- Pandas
- Polars

## Banco Analítico

- DuckDB

## Modelagem

- dbt

## Visualização

- Metabase

## Controle de Versão

- Git / GitHub

---

# Objetivo Técnico

Desenvolver uma solução completa envolvendo:

- Extração de dados;
- Tratamento e limpeza;
- Modelagem dimensional;
- Construção de métricas;
- Visualização dos indicadores;
- Documentação das decisões técnicas.
