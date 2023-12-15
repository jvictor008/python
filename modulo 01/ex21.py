import random
a1= input("Nome do primeiro aluno: ")
a2= input("Nome do segundo aluno: ")
a3= input("Nome do terceiro aluno: ")
a4= input("Nome do quarto aluno: ")
lista= [a1, a2, a3, a4]
ordem= random.sample(lista,4)
print("A ordem escolhida foi de {}".format(ordem))