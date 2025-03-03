
# Programa que pide una nota por consola y valora si el alumno ha aprobado o no.
notaIn=int(input("Introduzca nota:"))
if notaIn<5:
    calificacion="Suspenso"
else: calificacion="Aprobado"

print(calificacion)
# IF no sólo evalúa un boleano, también
# si una variable contiene información

variable = 19

if variable:
    print("Contiene información")
else:
    print("No contiene información")
#En este ejemplo sí evalúa un boleano

variable = 19

if variable == True:
    print("Contiene información")
else:
    print("No contiene información")
# Programa que pide una edad por
# consola y valora si el usuario es mayor
# de edad o no.
edad=int(input("Introduce edad: "))

if edad<18:
    print("No puedes pasar")
elif edad>100:
    print("Edad incorrecta")
else:
    print("Adelante")

# Programa que pide una nota por
# consola y valora las posibles
# calificaciones del alumno.
nota=int(input("Introduce tu nota: "))

if nota<5:
    print("Suspenso")
elif nota<7:
    print("Aprobado")
elif nota<9:
    print("Notable")
else:
    print("Sobresaliente")

# IF abreviado
n_num1 = 5
n_num2 = 10
if n_num1 > n_num2: print(n_num1 , "es mayor que" , n_num2)

# IF...ELSE abreviado
a = 2
b = 330
print("A") if a > b else print("B")
# Se pueden concatenar operadores de comparación:

edad=117
if 0<edad<100: # Sería como poner: if edad>0 and edad<100
    print("Edad correcta")
else:
    print("Edad incorrecta")

# Otro ejemplo de operadores de
# comparación concatenados

salarioPresidente = int(input("Introduce salario presidente: "))
print("El salario del presidente es de" ,salarioPresidente)

salarioDirector = int(input("Introduce salario Director: "))
print("El salario del director es de" ,salarioDirector)

salarioJefe = int(input("Introduce salario jefe: "))
print("El salario del jefe es de" ,salarioJefe)

salarioOperario = int(input("Introduce salario operario: "))
print("El salario del operario es de" , salarioOperario)

if salarioOperario<salarioJefe<salarioDirector<salarioPresidente:
    print("Todo ok")
else:
    print("Algo no va bien")

# Operadores AND y OR
distancia = int(input("Introduce distancia: "))
numHermanos = int(input("Introduce número de hermanos en el centro: "))
notaMedia = int(input("Introduce notaMedia: "))

if distancia>20 or numHermanos<2 or notaMedia<=5:
    print("NO eres candidato a la beca")
else:
    print("Sí eres candidato a la beca")

# Operador IN

opcion = input("ELige opcion: opcion1, opcion2, opcion3, opcion4: ")
pasoMinusculas = opcion.lower()
if pasoMinusculas in("opcion1",
"opcion2", "opcion3", "opcion4"):
    print("Opción válida: " + pasoMinusculas)
else:
    print("Opción inválida: " + pasoMinusculas)

# If anidados. Queremos comprar un
# coche. Necesitamos ser mayores de edad y tener 20000€

n_edad = int(input("Introduzca su edad: "))
n_dinero = int(input("Introduzca presupuesto: "))

if n_edad < 18:
    print("No tienes la edad suficiente para conducir.")
else:
    if n_dinero < 20000:
        print("Tienes la edad pero no el dinero para comprar el coche.")
    else:
        print("Puedes comprar el coche.")


# Operador ternario
num = 12
var = "par" if (num % 2 == 0) else "impar"

print(var)

# Sería como escribir

num = 12

if num % 2 == 0:
    print="Par"
else: print="Impar"

# El bucle for
# Ejecuta el print dos veces
for i in [1,10]:
    print("Hola")
# Imprime el contenido del diccionario
for i in ["primavera", "verano", "otoño", "invierno"]:
    print(i)
# Repite el print tantas veces como
# caracteres hay en el string

# Evaluamos si un mail contiene el caracter @
for i in "frase":
    print("Hola", end=" ")

miEmail=input("Introduce email")
email=False
for i in miEmail:
    if i=="@":
        email=True
if email==True: #Se puede simplificar if email:
    print("El email es correcto")
else:
    print("EL mail no es correcto")
# Podemos unir valores de texto con
# valores de variable a la hora de imprimir:
for i in range(5):
    print(f"Valor de la variable {i}")
for i in range(5,10):
    print(f"Valor de la variable {i}")

# Podemos poner un tercer argumento con
# el que especificamos de cuanto en cuanto
# va el conteo:
for i in range(5,10,2):
    print(f"Valor de la variable {i}")

# validar un mail en función de si tiene
# @ simplemente recorriendo la logitud del string:

valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
        print("Email correcto")
else:
    print("Email incorrecto")

# Las cadenas son objetos iterables,
# contienen una secuencia de caracteres:
for x in "banana":
    print(x)

# Con la instrucción break podemos
# detener el ciclo antes de que haya pasado
# por todos los elementos:

# Salga del bucle cuando x es "banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)
    if x == "banana":
        break
# Salga del bucle cuando x es "banana",
# pero esta vez el corte se produce antes
# de la impresión:

frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    if x == "banana":
        break
    print(x)

# Con la instrucción continue podemos detener la iteración actual del ciclo y
# continuar con la siguiente:

# En este caso no me imprimiría
"banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    if x == "banana":
        continue
    print(x)

# Para recorrer un conjunto de código un número específico de veces, podemos
# usar la función range ()

for x in range(6):
    print(x)

# Función range con parámetro de inicio incrementado por defecto en 1.

for x in range(2, 6):
    print(x)
# Función range con parámetro de inicio incrementado en 3.

for x in range(2, 30, 3):
    print(x)

# Bucle for anidado
# Imprime cada color para cada fruta:

color = ["verde", "amarilla", "roja"]
frutas = ["manzana", "banana", "cereza"]

for x in frutas:
    for y in color:
        print(x, y)

# Los bucles for no pueden estar vacíos. 
# Si por alguna razón tenemos un bucle for sin contenido, usaremos la
# instrucción pass para evitar un error.
for x in [0, 1, 2]:
    pass


