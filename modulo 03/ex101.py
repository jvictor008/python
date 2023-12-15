def ficha(nome="", gols=0):
    print("-"*20)
    print(f"Nome: {nome}\nGols marcados: {gols}")
    print("-"*20)
jogador= input("Digite o nome: ")
g = int(input("Digite o número de gols marcados: "))
ficha(jogador, g)