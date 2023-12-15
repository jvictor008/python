num= int(input("Diga um número: "))
pr= int(input("Diga a razão da progressão aritmética: "))
soma= 0
i= 0
while i < 10:
    i= i + 1
    num= num + pr
    print("{} + {} = {}".format(num - pr, pr, num))
  