# imprimir o nome da loja
print("Bem-vindo a Loja do Allan Martins Castilho Ferreira"); 

# escrever o valor do pedido e quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido: ")); 
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: ")); 


# pegar o valor do pedido e quantidade de parcelas
# se a quantidadeParcelas for menor que 4
if quantidadeParcelas < 4 : 
    valorDaParc = valorDoPedido * (1 + (0/100))/quantidadeParcelas # calculo do valor da parcela
    print(f"O valor das parcelas é de: R$ {valorDaParc:.2f}"); # imprimir "O valor das parcelas é de: R$ valorDaParc"

# se a quantidadeParcelas for maior que 4 e menor que 6 
elif quantidadeParcelas <= 5 :
    valorDaParc = valorDoPedido * (1 + (4/100))/quantidadeParcelas 
    print(f"O valor das parcelas é de: R$ {valorDaParc:.2f}"); #!  :.2f -> arredondamento

# se a quantidadeParcelas for maior que 6 e menor que 9
elif quantidadeParcelas <= 8 :  
    valorDaParc = valorDoPedido * (1 + (8/100))/quantidadeParcelas
    print(f"O valor das parcelas é de: R$ {valorDaParc:.2f}");

# se a quantidadeParcelas for maior que 9 e menor que 13 
elif quantidadeParcelas <= 12 :  
    valorDaParc = valorDoPedido * (1 + (16/100))/quantidadeParcelas 
    print(f"O valor das parcelas é de: R$ {valorDaParc:.2f}"); 

# entretanto 
else : 
    valorDaParc = valorDoPedido * (1 + (32/100))/quantidadeParcelas 
    print(f"O valor das parcelas é de: R$ {valorDaParc:.2f}");


 # calculo do valor total da parcela
valorTotalParc = valorDaParc * quantidadeParcelas
print(f"O valor Total Parcelado é de: R$ {valorTotalParc:.2f}")
