
# Iterable e Iterador
class Contador:
    def __init__(self, limite):
        self.limite = limite  # Número hasta donde queremos contar
        self.numero = 0  # Empezamos en 0

    def __iter__(self):
        return self  # Un iterador debe devolverse a sí mismo

    def __next__(self):
        if self.numero >= self.limite:
            raise StopIteration  # Detenemos la iteración cuando llegamos al límite
        self.numero += 1  # Aumentamos el número
        return self.numero  # Devolvemos el número actual

# Crear un objeto iterador que cuenta hasta 5
contador = Contador(5)

# Recorrer el iterador con un bucle for
for num in contador:
    print(num)  # Salida: 1, 2, 3, 4, 5

