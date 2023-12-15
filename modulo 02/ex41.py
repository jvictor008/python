l1= float(input("Digite o lado 1: "))
l2= float(input("Digite o lado 2: "))
l3= float(input("Digite o lado 3: "))
if l1 == l2 and l2 == l3:
    print("Triangulo equilátero")
elif (l1 == l2 and l3 != l2) or (l2 == l3 and l1 != l2):
    print("Triangulo isosceles")
else:
    print("Triangulo escaleno")