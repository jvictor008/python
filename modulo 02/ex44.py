from random import randint
print("Jogo jokenpô\n[1] Papel\n[2] Tesoura\n[3] Pedra")
opc= int(input("Faça sua jogada: "))
opcPc= randint(1, 3)
if (opc == 1 and opcPc == 3) or (opc == 2 and opcPc == 1) and (opc == 3 and opcPc == 2):
    resul="Você venceu"
elif (opc == 3 and opcPc == 1) or (opc == 1 and opcPc == 2) and (opc == 2 and opcPc == 3):
    resul="Você perdeu"
elif opcPc == opc:
    resul="Empate"
print("{}\nSua escolha {}\nA escolha do PC {}".format(resul, opc, opcPc))