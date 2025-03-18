
class Coche:

    # Declaración del constructor con parámetros

    def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):

        self.largo = largo
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso = peso
        self.color = color
        self.is_enMarcha = is_enMarcha

    # Declaración de dos instancias de clase pasándoles los parámetros requeridos en el constructor.
    
coche_1 = Coche(400, 160, 4, 1200, "amarillo", True)
coche_2 = Coche(300, 140, 4, 1000, "verde", False)

# Destructores

class Book():

    """ Clase para trabajar con libros """

    # Constructor

    def __init__(self, title, author = "", electronic = False):

        self.title = title
        self.author = author
        self.is_electronic = electronic

    # Destructor

    def __del__(self):

        print("Acabas de llamar al método destructor. Le objeto acaba de ser eliminado")
        
# para eliminar un objeto, utilizamos la pabra reservada del

book_1 = Book("El Quijote", "Cervantes", False)

del book_1

# Si intentásemos acceder al objeto book, obtendríamos error pues ha dejado de ser una
# instancia de la clase Book porque lo hemos eliminado.

# print(book_1)
