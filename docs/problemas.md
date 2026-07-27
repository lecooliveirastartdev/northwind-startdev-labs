# Problemas e descobertas

## 2026-07-26 - Descoberta de relacionamentos no banco Northwind

### Contexto

Durante a etapa de exploração do banco SQLite Northwind, foi realizada uma tentativa de identificar automaticamente os relacionamentos entre tabelas.

O banco não possui Foreign Keys declaradas, portanto foi necessário criar uma estratégia de inferência baseada nos nomes das colunas.

---

## Primeira estratégia: comparação por nome de coluna

Foi criado um mapeador inicial procurando padrões como:

- ID
- Id
- id

A lógica buscava colunas com nomes semelhantes entre tabelas.

Exemplo:
Order.EmployeeId
↓
EmployeeTerritory.EmployeeId

---

## Problema encontrado

O algoritmo encontrou relacionamentos incorretos.

Motivo:

O nome da coluna sozinho não garante um relacionamento válido.

Exemplo:
EmployeeId

pode existir em várias tabelas, porém isso não significa que todas são tabelas pai.

---

## Aprendizado

Em Engenharia de Dados:

Nome de coluna igual ≠ relacionamento correto.

A validação precisa considerar:

- Primary Keys;
- Foreign Keys;
- regras de negócio;
- contexto das entidades.

---

## Próxima evolução

Criar uma versão mais inteligente do mapeador considerando:

- identificação das Primary Keys;
- comparação apenas com chaves principais;
- direção do relacionamento:

Exemplo esperado:
Order.EmployeeId
↓
Employee.EmployeeId

---

## Status

✅ Exploração das tabelas concluída  
✅ Estrutura das tabelas analisada  
✅ Primeira tentativa de descoberta automática realizada  
⬜ Modelo relacional documentado  
⬜ Extração RAW iniciada


