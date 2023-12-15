num=int(input("Digite um número: "))
i = num - 1
resposta= 1
calculo = 1
while i != 0:
    calculo= calculo * i 
    i= i - 1
    resposta= calculo * num
print("O fatorial de {} é {}".format(num, resposta))
