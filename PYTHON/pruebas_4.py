def maxmin (lista):
   return max (lista), min (lista)    # Devuelve una tupla de 2 elementos

l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin (1)    # Desempaqueta la tupla en 2 variables

print (minimo, maximo, sep= ' ')