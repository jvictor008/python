d= {"nome": "", "sexo": "", "idade": ""}
mulher= []
s= i= 0
l= []
while True:
    d["nome"]= input("Digite teu nome: ")
    u= input("Digite o sexo{F/M}: ").lower()
    d["sexo"]= u
    if "f" == u:
        mulher.append(u)
    o= int(input("Digite sua idade: "))
    d["idade"]= o
    l.append(o)
    i += 1
    escolha= input("Você quer adicionar outra pessoa?(S/N) ").lower()
    if escolha == "n":
        break
m= z= s= 0
acima= []
while True:
    s= s + l[z]
    z +=1
    if z == len(l):
        m= s/i
        for y in l:
            if y > m:
                acima.append(y)
        break
print(f"Foram cadastradas {i} pessoas\nA media de idade foi de {int(m)}\nAs idades acimas da média {acima}\nAs mulheres cadastradas {len(mulher)}")
