pessoa= []
galera= []
pesos= []
i= 0
u= 1

while True:
    nome= input("Digite o nome da pessoa: ")
    peso= float(input("Digite o peso da pessoa: "))
    pessoa.append(nome)
    pessoa.append(peso)
    escolha= input("Você quer adicionar outra pessoa?(S/N) ")
    i+=1
    if escolha == "s":
         galera.append(pessoa)
    if escolha == "n":
        break
while True:
    if u > len(galera[0]):
        break
    if u % 2!= 0:
         pesos.append(galera[0][u])
    u+=1
pesos.sort()
print(f"A lista: {pessoa}\nA quantidade de pessoas na lista: {i}\nLista do mais leve para o mais pesado: {pesos}")    


