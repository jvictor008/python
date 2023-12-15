tup=("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "once", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
num= int(input("Diga um número de 1-20: "))
if num > 20 or num < 1:
    print("não")
print(tup[num]) 
