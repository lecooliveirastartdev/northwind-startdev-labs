import sqlite3

NOME_BANCO = "Northwind_small.sqlite"

try:
    # 1. Conecta ao banco com tempo de espera (timeout) configurado
    conn = sqlite3.connect(NOME_BANCO, timeout=10)
    cursor = conn.cursor()

    # Enable WAL mode (permite leitura e escrita concorrentes sem travar)
    cursor.execute("PRAGMA journal_mode=WAL;")

    print("Conexão realizada com sucesso!\n")

    # 2. Lista todas as tabelas reais do banco
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()
    
    print("--- Tabelas Encontradas ---")
    for t in tabelas:
        print(f"- {t[0]}")

    # 3. Consulta a estrutura da tabela Customer (dados reais)
    print("\n--- Estrutura da Tabela Customer (Colunas) ---")
    cursor.execute("PRAGMA table_info(Customer);")
    colunas = cursor.fetchall()

    for col in colunas:
        # col[1] é o nome da coluna, col[2] é o tipo de dado (VARCHAR, INT, etc)
        print(f"Coluna: {col[1]} | Tipo: {col[2]}")

    # 4. Consulta os primeiros 5 clientes reais da tabela
    print("\n--- Primeiros 5 Clientes Reais ---")
    cursor.execute("SELECT Id, CompanyName, ContactName, City, Country FROM Customer LIMIT 5;")
    clientes = cursor.fetchall()

    for cliente in clientes:
        print(f"ID: {cliente[0]} | Empresa: {cliente[1]} | Contato: {cliente[2]} ({cliente[3]} - {cliente[4]})")

except sqlite3.Error as e:
    print(f"Erro ao conectar ou consultar o SQLite: {e}")

finally:
    # Garante que a conexão seja FECHADA para não deixar o arquivo preso
    if 'conn' in locals():
        conn.close()
        print("\nConexão encerrada com segurança.")