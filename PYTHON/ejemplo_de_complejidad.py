
# Genero una lista de 100 millones de números aleatorios

import numbers as np
x = list(np.random.randint(low=1,high=500000,
                       size=99999999))

%%time
def constante(x:list) -> list:
    return x
constante(x)
