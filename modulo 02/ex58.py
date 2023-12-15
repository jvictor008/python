print("Programa qualquer")
n1= int(input("Digite o primeiro número: "))
n2= int(input("Digite o segundo número: "))
e= int(input("Escolha uma das oções:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nEscolha: "))
while e != 5:
    if e == 1:
        print(n1 + n2)
    if e == 2:
        print(n1 * n2)
    if e == 3:
        if n1 > n2:
            print("O {} é maior que {}".format(n1, n2))
        if n1 < n2:
            print("O {} é maior que {}".format(n2, n1))
            
        else:
            print("Os números são os mesmos")
            
    if e == 4:
        e4= int(input("Escolha uma opção:\n[1] Substituir o primeiro número\n[2] Substituir o segundo número\n[3]Substituir os dois números\nEscolha: "))
        if e4 == 1:
            n1= int(input("Digite o primeiro número: "))
        if e4 == 2:
            n2= int(input("Digite o segundo número: "))
        if e4 == 3:
            n1= int(input("Digite o primeiro número: "))
            n2= int(input("Digite o segundo número: "))
    e= int(input("Escolha uma das oções:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\nEscolha: "))