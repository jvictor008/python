print("Digitador de números\nDigite quantos números quiser\nPara sair do programa ==> 999")
i = 1
num= int(input("Digite um número: "))
if num == 999:
    print("Fim do programa")
else:
    while num != 999:
        num= int(input("Digite um número: "))
