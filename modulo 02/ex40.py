from datetime import date
anoNas= int(input("Digite o seu ano de nascimeto: "))
idade= date.today().year - anoNas
if idade <= 9 and idade > 0:
    print("Mirim")
elif idade <= 14 and idade > 0:
    print("Infantil")
elif idade <= 19 and idade > 0:
    print("Junior")
elif idade <= 25 and idade > 0:
    print("Sênior")
elif idade > 25:
    print("Master")
else:
    print("Você ainda não nasceu")