# Importa biblioteca para conexão com SQLite
import sqlite3


# Caminho do banco original
CAMINHO_BANCO = "data/raw/Northwind_small.sqlite"



def mapear_chaves():

    # Abre conexão com o banco
    conn = sqlite3.connect(CAMINHO_BANCO)

    # Cria cursor para executar SQL
    cursor = conn.cursor()


    # Busca todas as tabelas do banco
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table';
    """)


    tabelas = [
        tabela[0]
        for tabela in cursor.fetchall()
    ]


    print("🔗 Possíveis relacionamentos encontrados:\n")


    # Guarda todas as colunas de cada tabela
    estrutura = {}


    for tabela in tabelas:

        cursor.execute(
            f"PRAGMA table_info('{tabela}')"
        )

        colunas = cursor.fetchall()


        estrutura[tabela] = [
            coluna[1]
            for coluna in colunas
        ]


    # Compara colunas entre tabelas
    for tabela_origem, colunas_origem in estrutura.items():

        for coluna in colunas_origem:

            if coluna.lower().endswith("id"):

                for tabela_destino, colunas_destino in estrutura.items():

                    if tabela_origem != tabela_destino:

                        if coluna.lower() in [
                            c.lower()
                            for c in colunas_destino
                        ]:

                            if coluna.lower() != "id":

                                print(
                                    f"🔗 {tabela_origem}.{coluna} "
                                    f"→ {tabela_destino}.{coluna}"
                                )


    conn.close()



if __name__ == "__main__":
    mapear_chaves()