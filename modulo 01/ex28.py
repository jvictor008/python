vel= float(input("Digite a velocidade: "))
if vel <= 80:
    print("Velocidade normal")
else:
    velMais= vel - 80
    multa= 7 * velMais
    print("Acima que o permitido, multa de {} R$".format(multa))