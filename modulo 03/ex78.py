l= []
u= 0
i= 0
a= 0 
escolha = "s"
num= int(input("Digite um número: "))
l.append(num)
escolha = input("Deseja continuar?(s/n) ").lower()
while escolha == "s":
    num= int(input("Digite um número: "))
   
    i += 1
   
    escolha = input("Deseja continuar?(s/n) ").lower()
   
    if num not in l:
        l.append(num)
        
l.sort()
print(l)