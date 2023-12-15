valorCasa= float(input("O valor da casa: "))
salario= float(input("O seu salario: "))
anos= int(input("Quantidade de anos: "))
pretacao= valorCasa / (anos * 12)
if pretacao >= (salario * 30/100):
    print("Emprestimo negado")
else:
    print("Emprestimo aceito")