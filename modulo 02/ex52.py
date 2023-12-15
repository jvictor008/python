string= input("Digite uma frase: ")
total= len(string)
sInversa= string[:: -1]
frase= string.replace(" ", "")
inversa= sInversa.replace(" ", "")
for i in range(0, total+ 1):
    if inversa[i] == frase[i]:
        print("Essa frase é um Palíndromo")
        break
    if inversa[i] != frase[i]: 
        print("Essa frase não é um palíndromo")
        break
