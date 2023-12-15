def notas(lnotas):
    classe={"Quantidade de notas": 0, "A maior nota": 0, "A menor nota": 0, "Média da turma": 0, "Situcão da turma": 0}
    n= []
    n.append(lnotas)
    maior= n[0][0]
    menor= n[0][0]
    tamanho= len(n[0])
    s= 0
    for i in n[0]:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        s = s + i
    media= s / tamanho
    if media >= 7:
        situacao= "Acima da média"
    else:
        situacao= "Abaixo da média"
    print(n[0])
    classe["Quantidade de notas"]= tamanho
    classe["A maior nota"]= maior
    classe["A menor nota"]= menor
    classe["Média da turma"]= media
    classe["Situcão da turma"]= situacao
    print(classe)
escolha= "s"
nota= 0
l=[]
while escolha == "s":
    nota= float(input("Digite a nota: "))
    l.append(nota)
    escolha= input("Você quer adicionar outra nota?(S/N) ").lower()
notas(l)
