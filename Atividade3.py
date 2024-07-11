# nome da fabrica
print("Bem vindo à Fábrica de Camisetas do Allan Martins Castilho Ferreira")

# funcao escolha do modelo
def escolha_modelo():
    print("Entre com o modelo desejado")
    print("MCS - Manga Curta Simples")
    print("MCE - Manga Curta Com Estampa")
    print("MLS - Manga Longa Simples")
    print("MLE - Manga Longa Com Estampa")
    
    while True:
        modelo = input(">>").upper()
        if modelo in ['MCS', 'MCE', 'MLS', 'MLE']:
            return modelo
        else:
            print("Escolha inválida, entre com o modelo novamente")


# funcao escolha do frete
def GetFrete(): # USEI GetFrete() POR CAUSA DA VAR frete!!!
    print("Escolha o tipo de frete:")
    print("1 - Frete por transportadora - R$ 100.00")
    print("2 - Frete por Sedex - R$ 200.00")
    print("0 - Retirar na fábrica - R$ 0.00")
    
    while True:
        try:
            frete = int(input(">>"))
            if frete in [0, 1, 2]:
                return frete
            else:
                print("Opção de frete inválida. Tente novamente.")
        except ValueError: # uso do ValueError caso der false 
            print(">>")

# funcao calculo do desconto
def CalcularDesconto(num_camisetas, preco_unitario):
    if num_camisetas < 20:
        return num_camisetas * preco_unitario
    elif num_camisetas >= 20 and num_camisetas < 200:
        return num_camisetas * preco_unitario * 0.95 # 5%
    elif num_camisetas >= 200 and num_camisetas < 2000:
        return num_camisetas * preco_unitario * 0.93 # 7%
    elif num_camisetas >= 2000 and num_camisetas <= 20000:
        return num_camisetas * preco_unitario * 0.88 # 12%

# funcao pegar numero de camisetas 
def num_camisetas():
    while True:
        try:
            numCamisetas = int(input("Entre com o número de camisetas: "))
            if numCamisetas > 20000:
                raise ValueError("Não aceitamos tantas camisetas de uma vez.\n") # uso do raise para caso de false apareca a primeira mensagem 
            return numCamisetas
        except ValueError as e:
            print(f"{e}Por favor, entre com o número de camisetas novamente.") # em seguida segunda mensagem

# programa principal
def Main():

    modelo = escolha_modelo()
    
    if modelo == 'MCS':
        precoUnitario = 1.80
    elif modelo == 'MCE':
        precoUnitario = 2.80
    elif modelo == 'MLS':
        precoUnitario = 3.30
    elif modelo == 'MLE':
        precoUnitario = 4.20

    numCamisetas = num_camisetas()
    totalSemFrete = CalcularDesconto(numCamisetas, precoUnitario)
    
    frete = GetFrete()
    
    if frete == 1:
        custoFrete = 100.00
    elif frete == 2:
        custoFrete = 200.00
    else:
        custoFrete = 0.00

    total = totalSemFrete + custoFrete
    print(f"Total: R$ {total:.2f} (Modelo: {precoUnitario:.2f} * Quantidade(com desconto): {totalSemFrete/precoUnitario:.0f} + frete: {custoFrete:.2f})")

# iniciar o programa
if __name__ == "__main__":
    Main()
