x = "el valor de (a+b)*c es"
a, b, c = 4, 3, 2
d = (a+b)*c
imprimir = True
if imprimir:
    print(x, d)

# Esto es un comentario, Python lo ignora

"""Esto es un comentario 
de varias lineas de código, que Python ignora, ya sea 
colocando 2 o 3 comillas dobles"""

if True:
    print("True")

#if True:
#print("True")
"""Esto dará error, puesto que la función "if" no tiene bloque
de código"""

# Otros lenguajes como C requieren de ; al final de cada línea x = 10;
# en Python no
x = 5
y = 10
# Se puede usar un punto y coma, para tener dos sentencias en la misma línea
x= 5; y = 10

# Se puede romper el código en varias lineas usando \
x = 1 + 2 + 3 + 4 +\
5 + 6 + 7 + 8
# Si se trata de un bloque, basta con saltar a la siguiente línea
x = (1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8)
# Se puede hacer lo mismo par las funciones
def funcion(a, b, c):
    return a+b+c

d = funcion(10,
            23,
            3)



