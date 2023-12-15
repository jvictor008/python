l=[]
i= 0
while i <= 5:
    num= int(input("Digite um número: "))
    l.append(num)
    i += 1
tamanho= len(l)
inverso= l[:]
inverso.sort(reverse= True)
f= l.count(5)
if f == -1:
    f=0
print(f"A lista {l}\nO tamanho da lista {tamanho}")
l.reverse()
f= l.count(5)
if f == -1:
    f=0
print(f"O inverso da lista {l}\nO número cinco aparece {f} vezes")