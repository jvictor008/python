from datetime import date
print("Alistamento Militar")
anoNas= int(input("Seu ano de nascimeto: "))
idade= date.today().year - anoNas
if idade == 18:
    print("Hora de se alistar!!")
elif idade < 18:
    anoFal= 18 - idade
    print("Ainda não é possivel se alistar, ainda faltam {} anos!". format(anoFal))
else:
    print("O tempo de se alistar se encerrou")