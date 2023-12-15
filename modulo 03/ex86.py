from random import uniform
l= []
jogo= []
np=int(input("Quantidade de jogos: "))
i= u= 0
while i < np:
    while True:
        num= int(uniform(1, 60))
        jogo.append(num)
        u+=1
        if u == 6:
            l.append(jogo[:])
            break
    jogo.clear()
    u = 0
    i += 1
print(f"Jogo 1: {l[0]}\nJogo 2: {l[1]}\nJogo 3: {l[2]}")