print("  1 2 3\n1 [][][]\n2 [][][]\n3 [][][]")
lista= []
linha= []
par= []
i= u= z= s= sp= maior=0
while True:
    while u <= 3:
        num= int(input(f"Digite um número para [{i + 1}][{u+ 1}]:"))
        if num % 2 == 0:
            par.append(num)
            sp= sp + num
        linha.append(num)
        if i == 1:
            if u == 0:
                maior= num
            if num > maior:
                maior = num 
        if u == 2:
            s= s + num
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
print(f"A soma dos valores pares: {sp}\nA soma dos valores da terceira coluna: {s}\nO maior valor da segunda linha: {maior} ")