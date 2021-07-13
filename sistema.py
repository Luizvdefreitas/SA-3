valor_total = float(input("Digite o valor total da compra: ")) # Valor total da compra
valor_recebido = float(input("Digite o valor recebido: ")) # Valor total recebido pelo cliente
operacao = True


if(valor_total > valor_recebido): # Se o valor total for maior que o valor recebido, o saldo é insuficiente.
    import sys 
    sys.exit("Saldo insuficiente!") # Encerra o programa
    
elif(valor_total == valor_recebido): # Se o valor total e o valor recebido forem iguais, troco igual a zero reais.
    import sys
    sys.exit("Troco: R$ 0,00")

else:
#calculo do troco
    troco = valor_recebido - valor_total 

    print("Troco total de: ", troco)

notas_100 = troco // 100 # troco dividido por 100 =
print(f'\nNotas de R$100,00 para o cliente: {int(notas_100)}') # Quantidade de notas de 100

notas_50 = (troco - (notas_100 * 100)) // 50
print(f'\nNotas de R$50,00 para o cliente: {int(notas_50)}') # Quantidade de notas de 50

notas_20 = (troco - (notas_100 * 100) - (notas_50 * 50)) // 20 
print(f'\nNotas de R$20,00 para o cliente: {int(notas_20)}') # Quantidade de notas de 20

notas_10 = (troco - (notas_100 * 100) - (notas_50 * 50) - (notas_20 * 20)) // 10
print(f'Notas de R$10,00 para o cliente: {int(notas_10)}') # Quantidade de notas de 10

notas_5 = (troco - (notas_100 * 100) - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10)) // 5 
print(f'Notas de R$5,00 para o cliente: {int(notas_5)}') # Quantidade de notas de 5 

notas_2 = (troco - (notas_100 * 100) - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (notas_5 * 5)) // 2 
print(f'Notas de R$2,00 para o cliente: {int(notas_2)}') # Quantidade de notas de 2 

moedas_1 = (troco - (notas_100 * 100) - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (notas_5 * 5) - (notas_2 * 2)) // 1
print(f'Moedas de R$1,00 para o cliente: {int(moedas_1)}') # Quantidade de moedas de 1

moedas_50 = (troco - (notas_100 * 100) - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (notas_5 * 5) - (notas_2 * 2) -
(moedas_1 * 1)) // 0.5
print(f'Moedas de R$0,50 para o cliente: {int(moedas_50)}') # Quantidade de moedas de 50

moedas_25 = (troco - (notas_100 * 100) - (notas_50 * 50) - (notas_20 * 20) - (notas_10 * 10) - (notas_5 * 5) - (notas_2 * 2) -
(moedas_1 * 1) - (moedas_50 * 0.5)) // 0.25
print(f'Moedas de R$0,25 para o cliente: {int(moedas_25)}') #Quantidade de moedas 25
