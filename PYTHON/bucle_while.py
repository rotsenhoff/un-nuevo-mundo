# WHILE
# Imprime edad cuando el contador llegue a 18
edad = 0
while edad < 18: 
    edad=edad+1
print("Tienes "+str(edad))

# Pregunta la edad mientras sea negativa

edad=int(input("Introduce edad: "))

while edad<0:
    print("Edad incorrecta")
    edad=int(input("Introduce edad: "))

print("tu edad es: "+str(edad))

# Calcula la raiz cuadrada de un número. Tenemos tres intentos y 
# el número no puede ser negativo.
import math;
intentos=0;
num = int(input("Introduce numero: "))

while num<0:
    intentos=intentos+1
    print("Incorrecto")
    num=int(input("Introduce numero: "))

    if intentos==2:
        print("Demasiados intentos") 
    break

if intentos<2:
    intentos=intentos+1
    solucion=math.sqrt(num)
    print("la raiz cuadrada de "+str(num)+ " es: "+str(solucion))

# Bucle while con un if anidado y un break
# Salga del bucle cuando num sea 3:
num = 1
while num < 6:
    print(num)
    if num == 3:
        break
    num += 1

# LISTAS
"""
La lista es un tipo de colección ordenada
y modificable.
Es decir, una secuencia de valores de
cualquier tipo, ordenados y de tamaño
variable.
Se escriben entre corchetes. []
"""

miLista=["Angel", 43, 667767250]
miLista2 = [22, True, "una lista", [1,
2]]

# MÉTODOS DE LAS LISTAS

# Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)

# Acceder a los elementos de una lista
miLista = [22, True, "una cadena", [1,2]]
print(miLista[0])

miLista = [[1,2] , [3,4] , [5,6]]
miVar = miLista[1,1]
print(miVar)

# Función con una lista como parámetro

def miFunccion(listaFrutas):
    for x in listaFrutas:
        print(x)

frutas = ["Manzana", "banana", "cereza"]

miFunccion(frutas)

# TUPLAS

"""Una tupla es una colección ordenada e
inmutable.
En Python, las tuplas se escriben entre
paréntesis.
"""

# Declaración de una tupla

miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])

# Otra forma de declararla

miTupla = tuple(("manzana", "banana", "cereza"))
print(miTupla)

# Indexación Negativa

miTupla = ("manzana", "banana", "cereza")
print(miTupla[-1])

# Rango de índices
# Devuelve el tercer, cuarto y quinto elemento:

miTupla = ("manzana", "banana", "cereza",
           "naranja", "kiwi", "melon", "mango")
print(miTupla[2:5])

# Convierta la tupla en una lista para
# poder cambiarla:

miTupla = ("manzana", "banana", "cereza")
miLista = list(miTupla)
miLista[1] = "kiwi"
miTupla = tuple(miLista)

print(miTupla)

# Recorrer una tupla

miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
    print(x)

# Comprobar si existe un elemento
# Compruebe si "manzana" está presente en la tupla:

miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
    print("Sí, 'manzana' está en la tupla.")

# Otra forma, simplemente con un boolean

print("manzana" in miTupla)

# Longitud de la tupla

miTupla = ("manzana", "banana", "cereza")
print(len(miTupla))

# Unir dos tuplas

tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)

tupla3 = tupla1 + tupla2
print(tupla3)

# Cuantas veces se encuentra el elemento 4 en miTupla?

miTupla = ("manzana", "banana", "cereza"
, "manzana")
print(miTupla.count("manzana"))

# Desempaquetdo de tupla
miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3=miTupla

print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)