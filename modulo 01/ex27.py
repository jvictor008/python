import random
num=float(input("Digite um número(entre 0-5): "))
numCerto= random.randint(0,5)
if num == numCerto:
    print("Correto! Acertou o número!")
else:
    print("Infelizmente você errou o número\nO numero correto é {}".format(numCerto))