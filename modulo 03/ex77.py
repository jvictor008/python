lista = []
maior = 0
menor= 0
i= 0
while i < 5:
    num= int(input("Digite um número: "))
    lista.append(num)
    if i == 0:
        maior = menor= num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    i +=1
print(f"{lista}\nMaior: {maior}\nMenor: {menor}")