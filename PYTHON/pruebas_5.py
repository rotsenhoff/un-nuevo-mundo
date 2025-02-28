a = 'Python'    # Scope global (al módulo)
print('Valor fuera:', a)

def funcion():
    a=33
    print('Valor dentro', a)    # Scope local a la función

funcion()

print('Valor fuera', a)





