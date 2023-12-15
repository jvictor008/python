from random import uniform
def sorteio(num):
    u= 0
    while u < 5:
        n = int(uniform(1, 999))
        num.append(n)
        u+=1
def somaPar(l):
    s= 0
    for i in l:
        if i % 2 == 0:
            s= s + i
            print(f"Par: {i}")
    print(f"Soma: {s}")
numero= []
sorteio(numero)
print(numero)
somaPar(numero)