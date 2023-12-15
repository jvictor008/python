import math
angulo= float(input("Digite o valor do angulo: "))
seno= math.trunc(math.degrees(math.sin(angulo)))
cosseno=math.trunc(math.degrees(math.cos(angulo)))
tangente=math.trunc(math.degrees(math.tan(angulo)))
print("O valor do angulo é de {}\nSeu seno é de {}\nSeu cosseno é de {}\nSua tangente é de {}\nOBS: valor em Graus".format(angulo, seno, cosseno, tangente))