jogador={
    "nome": input("Digite o seu nome: "),
    "partidas": int(input("Quantidade de partidades jogadas: ")),
    "golsPar": ""
}
i= s= 0

while True:
    i += 1
    gols= int(input(f"Digite a quantiade de gols na partida {i}: "))
    s= s + gols
    if jogador["partidas"] == i:
        break
jogador["golsPar"]= s
print(f"Nome: {jogador['nome']}\nQuantidade de partidas: {jogador['partidas']}\nQuantidade total de gols: {jogador['golsPar']}")