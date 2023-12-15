lista= []
par= []
impar= []
i =0
while i <= 7:
    num= int(input("Digite um número: "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    i+=1
lista= [par, impar]
par.sort()
impar.sort()
print(f"Lista completa: {lista}\nLista dos pares: {par}\nLista dos impares: {impar}")