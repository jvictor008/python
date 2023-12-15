def fatorial(numero, show):
    f= 1
    if show == "n":
        for i in range(numero, 0, -1):
            f= f * i
            print(i)
        return f
    if show == "s":
        for i in range(numero, 0, -1):
            print(f"{i} x {f}= {f*i}")
            f= f * i
        return f
fat= int(input("Digite um número: "))
escolha= input("Você quer ver os calculos?(S/N) ").lower()
resposta= fatorial(fat, escolha)
print(resposta)