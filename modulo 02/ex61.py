num=int(input("Digite um número: "))
pr=int(input("Digite a progressão aritmética: "))
qnt= int(input("Digite a quantidade da progressão: "))
i = 1
while i <= qnt:
    i = i + 1
    num = num + pr
    print("{} x {} = {}". format(num - pr, pr, num ))