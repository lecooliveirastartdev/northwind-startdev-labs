# Importa biblioteca para conexão com SQLite
import sqlite3


# Caminho do banco original
CAMINHO_BANCO = "data/raw/Northwind_small.sqlite"


def analisar_estrutura():

    # Abre conexão com o banco
    conn = sqlite3.connect(CAMINHO_BANCO)

    # Cria cursor para executar SQL
    cursor = conn.cursor()


    # Busca todas as tabelas existentes
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table';
    """)

    tabelas = cursor.fetchall()


    print("📌 Estrutura das tabelas\n")


    # Percorre cada tabela encontrada
    for tabela in tabelas:

        nome_tabela = tabela[0]

        print(f"\n🔹 Tabela: {nome_tabela}")


        # PRAGMA é um comando especial do SQLite
        # usado para consultar informações internas
        # da estrutura das tabelas
        cursor.execute(
            f"PRAGMA table_info('{nome_tabela}')"
        )


        colunas = cursor.fetchall()


        for coluna in colunas:

            nome_coluna = coluna[1]
            tipo = coluna[2]
            chave = coluna[5]


            marcador = "🔑 PK" if chave else ""


            print(
                f"   - {nome_coluna} | {tipo} {marcador}"
            )


    conn.close()



if __name__ == "__main__":
    analisar_estrutura()