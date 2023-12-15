d= {
    "nome":input("Digite seu nome: "),
    "ano nascimento": int(input("Digite o ano que você nasceu: ")),
    "carteira de trabalho": int(input("Carteira de trabalho: ")) 
    }
if d["carteira de trabalho"] != 0:
    d["ano de contratação"]= int(input("Em que ano você foi contratado? "))
    d["salário"]= float(input("Qual seu salário: "))
    idade = 2023 - d["ano nascimento"]
    d["aposentadoria"]= idade + (d["ano de contratação"] + 35)- 2023
print(d)