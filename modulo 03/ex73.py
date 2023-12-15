from random import randrange
num= (randrange(999), randrange(999),randrange(999))
maior= menor = num[0]
i= 0
while True:
    i+= 1
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]
    if i == 2:
        break
print(f"{num}\nMaior número : {maior}\nMenor número: {menor}")