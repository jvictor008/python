num= i= 0
while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    while i <= 10:
        print(f"{num} x {i}= {i * num}")
        i+=1
print(f"Fim do programa")