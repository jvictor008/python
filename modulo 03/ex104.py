def ajuda(h):
    print(help(h))
escolha= "s"
a= ""
while escolha == "s":
    a= input("Digite um comando: ").lower()
    if a == "fim":
        b= "Fim do Programa"
        break
    if a != "fim":
        ajuda(a)
    escolha= input("Você outra ajuda?(S/N) ").lower()
print(b)