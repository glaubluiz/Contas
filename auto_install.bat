@echo off

REM Muda para a pasta do aquivo
cd /home/master/Development/home/Contas

REM Cria a maquina virtual
virtualenv .venv
call .venv\Scripts\activate

REM Instala as dependencias
pip install pysqlite3

REM Cria o banco de dados
python src\create_database\create_database.py
