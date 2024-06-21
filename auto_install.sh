#!/bin/bash

# Muda para a pasta do aquivo
cd /home/master/Development/home/Contas

# Cria a maquina virtual
python -m venv .venv
source .venv/bin/activate

# Instala as dependencias
pip install pysqlite3

# Cria o banco de dados
python src/create_database/create_database.py
