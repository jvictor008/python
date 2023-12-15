aluno = {"nome": "", "media": 0, "situação": ""}
nome= input("Digite o nome do aluno: ")
media= float(input("Digite a média do aluno: "))
if media >= 6:
    situacao= "Aprovado"
else:
    situacao= "reprovado"
aluno["nome"]= nome
aluno["media"]= media
aluno["situação"]= situacao
print(aluno.values())