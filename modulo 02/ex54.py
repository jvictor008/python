from datetime import date
s= 0
for i in range(0, 7):
    ano= float(input("Digite o ano de nascimento: ")) 
    idade=  date.today().year - ano
    if idade < 18 :
        s= s + 1
        print("{} pessoa não é maior de idade".format(s))