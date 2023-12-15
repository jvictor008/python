quilometros= float(input("Digite a quantidade de KM rodados: "))
dias=int(input("Digite a quantidade de dias com o veiculo: "))
valorKM= quilometros * 0.15
valorD= dias * 60
print("Quantidade de dias: {}\nQuantidade de KM rodados: {}\nValor total a pagar: {}".format(dias, quilometros, valorD + valorKM))