num= int(input("Digite um número: "))
i= 0
soma= 0
resultado= 0
n1= 1
n2= 1
while i <= num:
    soma = n1 + n2
    n1 = n2
    n2 = soma
    i += 1
    print(soma)