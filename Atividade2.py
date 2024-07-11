
# Define os precos dos sabores
precos = {
    "BA": {"P": 16, "M": 18, "G": 22},
    "FF": {"P": 15, "M": 17, "G": 21}
}

# funcao para imprimir as boas vindas
def BoasVindas():
# desing - menu 
    mensagemVindas = """
-Bem-vindo à Loja de Marmitas do Allan Martins Castilho Ferreira--
-----------------------------Cardápio-----------------------------
----| Tamanho |  Bife Acebolado(BA) |    Filé de Frango(FF)  |----
----|    P    |      R$ 16.00       |        R$ 15.00        |---- 
----|    M    |      R$ 18.00       |        R$ 17.00        |----
----|    G    |      R$ 22.00       |        R$ 21.00        |----
------------------------------------------------------------------
    """

    print(mensagemVindas)

# funcao para pegar o item pedido
def GetItem():
    while True:
        item = input("Escolha o sabor (BA/FF): ").strip().upper() # nao precisa escrever em Capslock
        if item in precos:
            return item
        else:
            print("Sabor inválido. Tente novamente.")

# funcao para pegar o tamanho pedido
def GetTamanho():
    while True:
        tamanho = input("Escolha o tamanho (P/M/G): ").strip().upper()
        if tamanho in ["P", "M", "G"]:
            return tamanho
        else:
            print("Tamanho inválido. Tente novamente.")

# programa principal
def Main():
    BoasVindas()

    custoTotal = 0
    while True:
        item = GetItem()
        tamanho = GetTamanho()
        custo = precos[item][tamanho]
        custoTotal += custo
        print(f"O valor atual da sua compra é: R$ {custo:.2f}")
        
        outro = input("Deseja mais alguma coisa? (S/N): ").strip().upper()
        if outro == "N":
            break

    print(f"O valor total da sua compra é: R$ {custoTotal:.2f}")
    
# iniciar o programa
if __name__ == "__main__":
    Main()
