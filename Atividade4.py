# nome da empresa
print("Bem vindo a empresa do Allan Martins Castilho Ferreira")

# lista e id global
lista_funcionarios = []
id_global = 4739255  # RU

# cadastro do funcionario
def cadastrar_funcionario(id):
    nome = input("Por favor entre com o nome do funcionário: ")
    setor = input("Por favor entre com o setor do funcionário: ")
    salario = float(input("Por favor entre com o salário do funcionário: "))
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    return funcionario

# adicionar o funcionario
def adicionar_funcionario():
    global id_global
    funcionario = cadastrar_funcionario(id_global)
    lista_funcionarios.append(funcionario)
    id_global += 1

# consulta de todos os funcionarios
def consultar_funcionarios():
    print("\n--------- CONSULTA TODOS OS FUNCIONÁRIOS ---------")
    for funcionario in lista_funcionarios:
        print(f"id: {funcionario['id']}")
        print(f"nome: {funcionario['nome']}")
        print(f"setor: {funcionario['setor']}")
        print(f"salário: {funcionario['salario']}\n")

# consultar por id os funcionarios
def consultar_por_id(id):
    for funcionario in lista_funcionarios:
        if funcionario['id'] == id:
            print(f"\nid: {funcionario['id']}")
            print(f"nome: {funcionario['nome']}")
            print(f"setor: {funcionario['setor']}")
            print(f"salário: {funcionario['salario']}\n")
            return
    print("Funcionário não encontrado.")

# consultar por setor os funcionarios
def consultar_por_setor(setor):
    print(f"\n--------- CONSULTA POR SETOR: {setor} ---------")
    for funcionario in lista_funcionarios:
        if funcionario['setor'] == setor:
            print(f"id: {funcionario['id']}")
            print(f"nome: {funcionario['nome']}")
            print(f"salário: {funcionario['salario']}\n")

# remover funcionario por id
def remover_funcionario(id):
    global lista_funcionarios
    lista_funcionarios = [funcionario for funcionario in lista_funcionarios if funcionario['id'] != id]

# programa principal
def Main():
    while True:
        print("\n--------- MENU PRINCIPAL ---------")
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Funcionário")
        print("2 - Consultar Funcionário(s)")
        print("3 - Remover Funcionário")
        print("4 - Sair")
        opcao = input(">> ")

        if opcao == '1':
            print("\n--------- MENU CADASTRAR FUNCIONÁRIO ---------")
            print(f"Id do Funcionário: {id_global}")
            adicionar_funcionario()
        elif opcao == '2':
            while True:
                print("\n--------- MENU CONSULTAR FUNCIONÁRIO ---------")
                print("Escolha a opção desejada:")
                print("1 - Consultar Todos os Funcionários")
                print("2 - Consultar Funcionário por id")
                print("3 - Consultar Funcionário(s) por setor")
                print("4 - Retornar")
                sub_opcao = input(">> ")

                if sub_opcao == '1':
                    consultar_funcionarios()
                elif sub_opcao == '2':
                    id = int(input("Digite o ID do funcionário: "))
                    consultar_por_id(id)
                elif sub_opcao == '3':
                    setor = input("Digite o setor: ")
                    consultar_por_setor(setor)
                elif sub_opcao == '4':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao == '3':
            id = int(input("Digite o ID do funcionário: "))
            remover_funcionario(id)
        elif opcao == '4':
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# iniciar o programa
if __name__ == "__main__":
    Main()
