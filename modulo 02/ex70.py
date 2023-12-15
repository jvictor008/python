num= int(input("Diga o valor a ser sacado: "))
c= v= d= u= 0
if num > 50:
    while True:
        if num % 50 == 0:
            c +=1
            num = num - 50
            if 50 - num == 50:
                break
        if num % 50 != 0:
            c +=1
            num = num -50
            if num < 50:
                break
if num > 20:
    while True:
        if num % 20 == 0:
            v +=1
            num = num - 20
            if 20 - num == 20:
                break
        if num % 20 != 0:
            v +=1
            num = num -20
            if num  < 20:
                break
if num > 10:           
    while True:
        if num % 10 == 0:
            d +=1
            num = num - 10
            if 10 - num == 10:
                break
        if num % 10 != 0:
            d +=1
            num = num - 10
            if num - 10 < 10 :
                break
while num > 0:
     u += 1
     num = num - 1      
          
   
print(f"Celulas de 50: {c}\nCelulas de 20: {v}\nCelulas de 10: {d}\nCelulas de 1: {u}")