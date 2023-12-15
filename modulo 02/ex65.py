num = soma = i = 0
while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    soma += num
    i += 1
print(f"A quantidade de números é de {i} e a soma deles é de {soma} ")