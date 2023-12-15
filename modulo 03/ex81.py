l1= []
l2= []
l3= []
escolha= "s"
while escolha == "s":
    num = int(input("Digite um número: "))
    l1.append(num)
    if num % 2 == 0:
        l2.append(num)
    else:
        l3.append(num)
    escolha= input("Você ainda quer continuar?(s/n) ").lower()
print(f"Lista total {l1}\nListas dos números pares {l2}\nListas dos números impares {l3}")
    