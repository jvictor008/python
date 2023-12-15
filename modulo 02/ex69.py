nome= input("Diga o nome do produto: ")
preco= float(input("Digite o preço: "))
escolha= input("Deseja continuar? [S/N] ").lower()
soma= preco
i= 0
if preco >= 1000:
    i= 1
barato = nome
menor= preco
while escolha == "s": 
    nome= input("Diga o nome do produto: ")
    preco= float(input("Digite o preço: "))
    if preco >= 1000:
        i += 1
    if preco < menor:
        barato = nome
    soma += preco
    escolha= input("Deseja continuar? [S/N] ").lower()
    if escolha == "n":
        break
print(f"Soma total: {soma}\nQuantidade de produtos que custam mais que R$1000: {i}\nO produto mais barato: {barato}")
