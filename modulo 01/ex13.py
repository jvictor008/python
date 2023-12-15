preco= float(input("Digite o valor do produto: "))
print("O preco do produto é de {} sem o desconto de {}(5%)\nO valor final é de {}".format(preco, preco * (5/100), preco - (preco * (5/100))))