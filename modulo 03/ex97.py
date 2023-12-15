def maior(num):
    print(num)
    m= num[0]  
    for i in num:
        if i > m:
            m = i  
    print(m)
numero= []
while True:
    n= float(input("Digite um número: "))
    numero.append(n)
    escolha= input("Quer adicionar outro número?(S/N) ").lower()
    if escolha == "n":
        break
maior(numero)