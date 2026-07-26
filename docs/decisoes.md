# 📌 Decisões Técnicas do Projeto Northwind

## Decisão 01 - Manter SQLite como fonte inicial

**Data:** 26/07/2026

### Contexto

A base Northwind foi disponibilizada inicialmente em formato SQLite.

### Decisão

Manter o SQLite como camada de origem dos dados.

### Motivo

- Preservar a fonte original;
- Evitar alterações nos dados brutos;
- Simular um cenário real de ingestão de dados.

### Impacto

O pipeline será construído a partir da extração dessa fonte, permitindo evolução futura para uma arquitetura analítica.