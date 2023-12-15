print("  1 2 3\n1 [][][]\n2 [][][]\n3 [][][]")
lista= []
linha= []
i= u= z= 0
while True:
    while u <= 3:
        num= int(input(f"Digite um número para [{i + 1}][{u+ 1}]:"))
        linha.append(num)
        u+= 1
        if u == 3:
            lista.append(linha[:])
            break
    i+=1
    u = 0
    z+=1
    linha.clear()
    if z == 3:
        break
    
print(f"   1  2  3\n1 [{lista[0][0]}][{lista[0][1]}][{lista[0][2]}]\n2 [{lista[1][0]}][{lista[1][1]}][{lista[1][2]}]\n3 [{lista[2][0]}][{lista[2][1]}][{lista[2][2]}]")