print("Programa comparação de números")
n1= float(input("Digite um número: "))
n2= float(input("Digite outro número: "))
if n1 > n2:
    print("O {} é maior que o {}".format(n1, n2))
elif n1 < n2:
    print("o {} é mairo que o {}".format(n2, n1))
else:
    print("Os números são iguais")