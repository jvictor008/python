num= int(input("Digite um número: "))
escolha=input("Deseja continuar no programa[S/N]? ").upper()
if escolha == "N":
    print("Fim do programa")
if escolha == "S":
    i = 1
    soma = num
    m= 0
    maior = num
    menor = num
    while escolha == "S":
        num= int(input("Digite um número: "))
        print(num)
        soma = soma + num
        i += 1
        m = soma / i
        escolha=input("Deseja continuar no programa[S/N]? ").upper()
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print("Média: {}\nMaior= {}\nMenor= {}".format(m, maior, menor))
