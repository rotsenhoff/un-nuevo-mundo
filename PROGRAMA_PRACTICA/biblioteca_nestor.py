
'''------ SISTEMA DE GESTION DE BIBLIOTECA ------'''

# Funcion para agregar un libro a la biblioteca

def agregar_libro(libro, biblioteca):
    biblioteca.append(libro)
    return biblioteca



# Definimos la clase Libro

class Libro:
    def __init__(self, titulo, autor, isbn):
        """Constructor de la clase Libro."""
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Todos los libros comienzan como disponibles
    
    def prestar(self):
        """Método para prestar un libro."""
        if self.disponible:
            self.disponible = False
            print("Libro prestado con éxito.")
        else:
            print("El libro ya está prestado.")
    
    def devolver(self):
        """Método para devolver un libro."""
        if not self.disponible:
            self.disponible = True
            print("Libro devuelto con éxito.")
        else:
            print("El libro ya estaba disponible.")
    
    def mostrar_info(self):
        """Método para mostrar la información del libro."""
        estado = "Sí" if self.disponible else "No"
        return f"{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"

# Lista para almacenar los libros
biblioteca = []

def agregar_libro():
    """Función para agregar un nuevo libro."""
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    libro = Libro(titulo, autor, isbn)
    biblioteca.append(libro)
    print("Libro agregado con éxito.")

def prestar_libro():
    """Función para prestar un libro buscando por ISBN."""
    isbn = input("Ingresa el ISBN: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.prestar()
            return
    print("Libro no encontrado.")

def devolver_libro():
    """Función para devolver un libro buscando por ISBN."""
    isbn = input("Ingresa el ISBN: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.devolver()
            return
    print("Libro no encontrado.")

def mostrar_libros():
    """Función para mostrar todos los libros en la biblioteca."""
    if not biblioteca:
        print("No hay libros en la biblioteca.")
    else:
        for libro in biblioteca:
            print(libro.mostrar_info())

def buscar_libro():
    """Función para buscar un libro por ISBN."""
    isbn = input("Ingresa el ISBN: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            print(libro.mostrar_info())
            return
    print("Libro no encontrado.")

def menu():
    """Función para manejar el menú de opciones."""
    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            buscar_libro()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

# Ejecutamos el menú
menu()
