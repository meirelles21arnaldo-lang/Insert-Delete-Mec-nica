import sqlite3 as sql

def conectar():
    conn = sql.connect("oficina.db")
    return conn

def criar_tabela_mecanico():
    conn = conectar()
    cursor = conn.cursor()

    cursor = cursor.execute("""
        CREATE TABLE IF NOT EXISTS mecanico (
        cpf PRIMARY KEY NOT NULL UNIQUE,
        nome TEXT NOT NULL)
""")

    conn.commit()
    conn.close()

def buscar_cpf(cpf: str):
    cpf.strip()
    conn = conectar()
    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * FROM mecanico WHERE cpf = ?" , (cpf,))

    if cursor.fetchone() is None:
        conn.close()
        return False

    else:
        conn.close()
        return True

def cadastar_mecanico(cpf: str , nome: str):

    if nome.strip() == "" or nome.isdigit():
        return "Insira um nome válido!"

    elif not (len(cpf) == 11 and cpf.isdigit()):
        return "CPF inválido!"

    elif buscar_cpf(cpf) == True:
        return "CPF já cadastrado!"

    else:

        conn = conectar()
        cursor = conn.cursor()

        cursor = conn.execute("INSERT INTO mecanico (cpf , nome) VALUES (? , ?)", (cpf.strip() , nome.strip()))

        conn.commit()
        conn.close()

        return "Cadastrado com Sucesso!"

def deletar_mecanico(cpf):

    if len(cpf) == 11 and cpf.isdigit() and buscar_cpf == True:
        conn = conectar()
        cursor = conn.cursor()

        cursor = cursor.execute("DELETE FROM mecanico WHERE cpf = ?", (cpf,))

        conn.commit()
        conn.close()

        return "Funcionário Deletado do Sistema!"

    else:
        return "Funcionário Inválido!"  
