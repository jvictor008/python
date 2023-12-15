s= 0
maior = 0 
menor = 0
for i in range(0, 5):
    s+= 1
    peso= float(input("Qual seu peso? "))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    print("{}° possui {} kg".format(s, peso))
print("Maior peso: {}\nMenor peso: {}".format(maior, menor))