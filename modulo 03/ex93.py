jogador={
    "nome": "",
    "jogos": 0
}
lTotal= []
lgol= []
gol= []
lNome= []
lJogos= []
u= z= i= s= y= 0
while True:
    jogador["nome"]= input("Digite o nome: ")
    jogador["jogos"]= int(input("Digite o número de jogos: "))
    while True: 
        u+=1
        gp= int(input(f"Digite o número de gols na partida {u}: "))
        gol.append(gp)
        s = s + gp
        jogador["golsPar"]= gol
        if u == jogador["jogos"]:
            print(f"Nome: {jogador['nome']}\nNumero de jogos {jogador['jogos']}\nGols feitos {jogador['golsPar']}\nNúmero total de gols: {s}")
            lTotal.append(s)
            lNome.append(jogador["nome"])
            lJogos.append(jogador["jogos"])
            lgol.append(gol[:])
            gol.clear()
            s=0
            break
    z += 1
    u= 0
    escolha=input("Você ainda quer adicionar outro jogador(S/N? ").lower()
    if escolha == "n":
        break
while True:
    print(f"{i} {lNome[i]} {lgol[i]} {lTotal[i]}")
    i+=1
    if i == len(lNome):
       break
while True:
    e= int(input("Escolha um jogador para ver os dados(999 para parar): "))
    for p in lgol[e]:
        print(f"Jogo {y} = {p}")
        y += 1
    
    if e == 999:
        break
            
        
