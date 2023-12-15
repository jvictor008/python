l= []
aluno= []
i= u= z=0
while True:
    nome= input("Digite o nome do aluno: ")
    n1= float(input("Digite a nota parcial: "))
    n2= float(input("Digite a nota parcial: "))
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    l.append(aluno[:])
    aluno.clear()
    escolha= input("Deseja continuar?(S/N) ").lower()
    if escolha == "n":
        break
while True:
    m= (l[u][1] + l[u][2]) / 2
    print(f"{i} {l[u][0]} {m}")
    i+=1
    u+= 1
    if i == len(l):
        break
while True:
    num= int(input("Digite o número que você quer ver as notas(-1 para o programa): "))
    if num == -1:
        print("Programa encerrado")
        break
    print(f"{l[num][1]} e {l[num][2]}")
    