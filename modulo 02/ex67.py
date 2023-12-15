from random import randrange
pc= randrange(1,1000)
num= 0
escolha= input("Escolha par ou impar: ").lower()
if escolha == "par":
    while True:
        num= int(input("Digite um número: "))
        if (num + pc) % 2 != 0:
            break
        print("Você venceu")
else:
    while True:
        num= int(input("Digite um número: "))
        if (num + pc) % 2 == 0:
            break
        print("Você venceu")
print(f"Você perdeu\nSeu número: {num}\nO número do PC: {pc}")
