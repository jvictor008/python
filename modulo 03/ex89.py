from random import randint
d= {
    "j1": randint(1, 6),
    "j2": randint(1, 6),
    "j3": randint(1, 6),
    "j4": randint(1, 6)
}
maior= d["j1"]
if d["j2"] > maior:
    maior= d["j2"]
if d["j3"] > maior:
    maior= d["j3"] 
if d["j4"] > maior:
    maior= d["j4"]
print(f"\Os números tirados: {d.values()}\nO maior número tirado foi {maior}") 
