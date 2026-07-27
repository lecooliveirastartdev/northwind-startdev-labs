# Importa biblioteca para conexão com SQLite
import sqlite3


# Caminho do banco original
CAMINHO_BANCO = "data/raw/Northwind_small.sqlite"


def analisar_relacionamentos():

    # Conecta ao banco SQLite
    conn = sqlite3.connect(CAMINHO_BANCO)

    # Cria cursor para executar comandos SQL
    cursor = conn.cursor()


    # Busca todas as tabelas do banco
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table';
    """)

    tabelas = cursor.fetchall()


    print("🔗 Relacionamentos encontrados:\n")


    for tabela in tabelas:

        nome_tabela = tabela[0]


        # Consulta as chaves estrangeiras da tabela
        cursor.execute(
            f"PRAGMA foreign_key_list('{nome_tabela}')"
        )


        relacionamentos = cursor.fetchall()


        for relacao in relacionamentos:

            tabela_destino = relacao[2]
            coluna_origem = relacao[3]
            coluna_destino = relacao[4]


            print(
                f"{nome_tabela}.{coluna_origem} "
                f"→ {tabela_destino}.{coluna_destino}"
            )


    conn.close()



if __name__ == "__main__":
    analisar_relacionamentos()