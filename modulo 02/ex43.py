print("Super mercado super legal\nOpções de Pagamento\n[1] À vista dinheito/cheque: 10% de desconto\n[2] À vista cartão: 5% de desconto\n[3] Em até 2x no cartão: preço normal\n[4] 3x ou mais no cartão: 20% de juros ")
preco= float(input("Digite o preço do produto: "))
opção= int(input("Digite a opção de pagamento: "))
if opção == 1:
    valor= preco - (preco * 10/100)
    print("O valor total sera de {}".format(valor))
elif opção == 2:
    valor= preco - (preco * 5/100)
    print("o valor sera de {}".format(valor))
elif opção == 3:
    print("O valor sera de {}".format(preco))
elif opção == 4:
    valor= preco + (preco * 20/100)
    print("O valor sera de {}".format(valor))