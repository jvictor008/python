def moeda(m):
   s= str(float(m))
   q= len(s) - 1
   return f"R${m}".replace(".", ",")