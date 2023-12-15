nome= input("A cidade que você nasceu: ")
separado= nome.split()
junto= "!".join(separado)
primeiroNome= junto[:junto.find("!")]
santo=primeiroNome.find("Santo")
print(santo)