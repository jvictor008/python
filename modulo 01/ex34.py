l1= float(input("Digite o valor do lado: "))
l2= float(input("Digite o valor do lado: "))
l3= float(input("Digite o valor do lado: "))
if (abs(l2 - l3) < l1 < l2 + l3) or (abs(l1 - l3) < l2 < l3 + l1) or (abs(l1 - l2) < l3 < l1 + l2):
    print("Os lados podem formar um triângulo")
else:
    print("Os lados não podem formar um triângulo")
    
    