frase= input("Digiite uma frase: ")
minusculo= frase.lower()
quantidade= minusculo.count("a")
primeiro=minusculo.find("a")
separado=minusculo.split()
inverso= separado[::-1]
junto= " ".join(inverso)
ultimo=junto.find("a")
print("Frase digitada: {}\nQuantidade de letra : {}\nPrimeira letra: {}\nUltima letra: {}".format(frase, quantidade, primeiro, ultimo))

