
from math import pi

def area(r):

    # Verificamos los tipos correctos de los parámetros.
    if type(r) not in [int, float]:
        raise TypeError('El radio debe ser un valor numérico')
    
    if r < 0:
    #    raise ValueError('El radio no puede ser negativo')
        print('El radio no puede ser negativo')
    areaC = pi*(r**2)
    return areaC

valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']

for v in valores:
    areaCalculada = area(v)
    print('Para el valor', v, 'el area es', areaCalculada)
    
    