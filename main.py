import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('imc_db.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS imc (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            altura REAL,
            peso REAL,
            resultado_imc REAL,
            data_calculo TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

def calcular_imc(altura, peso):
    return peso / (altura ** 2)

def inserir_dados(nome, altura, peso, resultado_imc, data_calculo):
    conexao = sqlite3.connect('imc_db.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO imc (nome, altura, peso, resultado_imc, data_calculo)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, altura, peso, resultado_imc, data_calculo))

    conexao.commit()
    conexao.close()

def exibir_todos_os_registros():
    conexao = sqlite3.connect('imc_db.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM imc')
    registros = cursor.fetchall()

    for registro in registros:
        print(registro)

    conexao.close()

def main():
    criar_tabela()

    while True:
        print("\nMenu:")
        print("1. Calcular e armazenar novo IMC")
        print("2. Exibir todos os registros")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o seu nome: ")
            altura = float(input("Digite a sua altura (em metros): "))
            peso = float(input("Digite o seu peso (em quilogramas): "))
            resultado_imc = calcular_imc(altura, peso)
            inserir_dados(nome, altura, peso, resultado_imc, '2023-01-01')
            print(f"Seu IMC é: {resultado_imc:.2f}")
            print("Dados armazenados no banco de dados.")
        elif opcao == '2':
            exibir_todos_os_registros()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
