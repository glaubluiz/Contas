# Cria o banco de dados zerado

# Objetivo
# Criar o banco de dados zerado a partir de todos os arquivos sql da pasta 
# database/create_database.

import os
import sqlite3

def make_database():
    # Verifica os arquivos salvos na pasta create_database
    try:
        file_list = os.listdir("database/create_database")
    except Exception as e:
        print(f"Erro em {__file__}: \nErro na verificação de arquivos sql \n{e}\n")
    
    # Cria e abre o banco de dados
    try:
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
    except Exception as e:
        print(f"Erro em {__file__}: \nErro ao criar/abrir banco de dados \n{e}\n")
    
    # Cria as tabelas do banco de dados
    for file in file_list:
        try:
            with open(f"database/create_database/{file}", "r") as file:
                sql_command = file.read()
                try:
                    cursor.execute(sql_command)
                except Exception as e:
                    print(f"Erro em {__file__}: \nErro ao criar tabela \n {e}\n")
        except Exception as e:
            print(f"Erro em {__file__}: \nErro em abrir arquivo \n{e}\n")


if __name__ == "__main__":
    make_database()
