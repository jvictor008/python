def voto(dataNas):
    idade= 2023- dataNas
    if idade < 16:
        return "não pode votar"
    if (idade >= 16 and idade < 18) or idade >= 60:
        return "facultativo"
    if  idade >= 18 and idade < 60:
        return "obrigatório"
pergunta= int(input("Digite o ano de nascimento: "))
resposta= voto(pergunta)
print(resposta)