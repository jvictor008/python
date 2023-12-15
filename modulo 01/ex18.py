import math
cat1= float(input("Digite o valor do cateto adjacente: "))
cat2= float(input("Digite o valor do cateto oposto: "))
hip= math.sqrt(math.pow(cat1, 2) + math.pow(cat2, 2))
print("O valor do cateto adjacente é de {} e do oposto é de {}\nO valor da hipotenusa é de {}".format(cat1, cat2, hip))