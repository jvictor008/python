def contador(ini, fim, pas):
    while ini <= fim:
        print(ini)
        ini= ini + pas
ini= float(input("de: "))
fim= float(input("Até: "))
pas= float(input("Passando: "))    
contador(ini, fim, pas)