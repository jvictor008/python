s= 0
for i in range(0, 7):
    num=int(input("Digite um número: "))
    if num % 2 == 0:
        s += num
print("A soma dos pares é de {}".format(s))