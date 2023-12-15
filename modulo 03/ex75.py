nome= ("a", "b", "c", "d")
preco= ("1", "2", "3", "4")
i = 0
while True:
    print(f"{nome[i]}.....{preco[i]}")
    i += 1
    if i == len(nome):
        break