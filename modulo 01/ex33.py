sal= float(input("Digite o salário: "))
if sal > 1250:
    aumento= (sal * (10/100)) + sal
else:
    aumento=(sal * (15/100)) + sal
print("O novo salario é {}".format(aumento))