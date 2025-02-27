def f1(a):    # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x):    # Función anidada
        print(x)    # Llamamos a f2 desde f1
    f2(b)

f1('Python')    # Llamamos a f1

def f1(a): # Función que "encierra" a f2


 def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
    
 factorial(5)


