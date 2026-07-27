# Importa a biblioteca nativa do Python para trabalhar com bancos SQLite
import sqlite3


# Caminho do arquivo do banco de dados original (camada raw)
CAMINHO_BANCO = "data/raw/Northwind_small.sqlite"


# Função responsável por explorar a estrutura do banco
def explorar_banco():

    # Cria uma conexão entre o Python e o banco SQLite
    conn = sqlite3.connect(CAMINHO_BANCO)

    # Cria um cursor para executar comandos SQL dentro do banco
    cursor = conn.cursor()


    # Consulta a tabela interna do SQLite que guarda informações
    # sobre a estrutura do banco (tabelas, índices, etc.)
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table';
    """)


    # Recupera todas as tabelas encontradas pela consulta
    tabelas = cursor.fetchall()


    # Exibe um título para o resultado da exploração
    print("📌 Inventário do Banco:\n")


    # Percorre cada tabela encontrada
    for tabela in tabelas:

        # Como o retorno vem como tupla, pegamos apenas o nome
        nome_tabela = tabela[0]


        # Executa uma consulta para contar quantos registros
        # existem dentro de cada tabela
        cursor.execute(
            f"SELECT COUNT(*) FROM '{nome_tabela}'"
        )


        # Recupera o número retornado pelo COUNT(*)
        quantidade = cursor.fetchone()[0]


        # Mostra o nome da tabela e sua quantidade de registros
        print(f"- {nome_tabela}: {quantidade} registros")


    # Fecha a conexão com o banco para liberar recursos
    conn.close()



# Garante que a função será executada somente quando
# este arquivo for chamado diretamente
if __name__ == "__main__":

    # Executa a exploração do banco
    explorar_banco()