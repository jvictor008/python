while True:
    sexo= input("Diga seu sexo: ").lower()
    idade= input("Diga sua idade: ")
    print(f"{sexo} e {idade}")
    escolha= input("Você deseja continuar? (S/N) ").lower()
    if escolha == "n":
        break
print("Fim do programa")