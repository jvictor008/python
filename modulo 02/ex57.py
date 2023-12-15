from random import uniform
print("Jogo de Adivinha\nAcabei de pensar em número entre 1 e 10, você consegue adivinhar ele?")
num= int(input("Faça um palpite: "))
certo= int(uniform(1, 10))
if num > 10 or num < 1:
    print("Jogue corretamente :/")
i= 0
while num != certo:
     i = i + 1
     num= int(input("Faça um palpite: "))
     if i == 9:
          num= int(input("Agora vai!: "))
print("Parabens você acertou\n {}".format(certo))