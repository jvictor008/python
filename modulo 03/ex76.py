palavras= ("ana", "lula", "cachorro", "primo")
i= u=  0
s= v= ""
while True:
    s = palavras[u]
    while True:
        letra= s[i]
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            v= v + letra + " "
        i += 1
        if i > len(letra):
            break
    print(f"A palavra {s} possui-- {v}--como vogais")
    u +=1
    if u == len(palavras):
        break