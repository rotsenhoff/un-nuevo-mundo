
"------------ SISTEMA DE GESTIÓN DE BIBLIOTECA ---------"

# Funcion para agregar un libro a la biblioteca

def agregar_libro(libro, biblioteca):
    biblioteca.append(libro)
    return biblioteca

 # Primero de todo, definimos la clase Libro

class Libro():

    # Ahora definimos los atributos de la clase Libro y declaramos su constructor.
    
    def __init__(self, titulo, autor, isbn):

        self.titulo = titulo(str)
        self.autor = autor(str)
        self.isbn = isbn(str)
        self.disponible = True(bool) # Todos los libros comienzan como disponibles

    # Ahora definimos los métodos de la clase Libro

    def prestar(self): # Método para el prestamo del libro
        
        if self.disponible:
            
            self.disponible = False
            print("Libro prestado con éxito.")
        
        else:
            
            print("El libro ya está prestado.")
    
    def devolver(self): # Método para devolver un libro.
        
        if not self.disponible:
            
            self.disponible = True
            print("Libro devuelto con éxito.")
            
        else:
            
            print("El libro ya estaba disponible.")
    
    def mostrar_info(self): # Método para mostrar la información del libro.
        
        estado = "Sí" if self.disponible else "No"
        
        print(f"{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}")

# Lista para almacenar los libros

biblioteca = []

def agregar_libro(): # Función para agregar un nuevo libro.
    
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    libro = Libro(titulo, autor, isbn)
    biblioteca.append(libro)
    

def prestar_libro(): # Función para prestar un libro buscando por ISBN.
    
    isbn = input("Ingresa el ISBN: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.prestar()
            return
    

def devolver_libro(): # Función para devolver un libro buscando por ISBN.
    
    isbn = input("Ingresa el ISBN: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.devolver()
            return
    

def mostrar_libros(): # Mostrar libros en la biblioteca.
    
    for libro in biblioteca:
        
        print(libro.mostrar_info())

def buscar_libro(): # Búsqueda de un libro por ISBN
    
    isbn = input("Ingresa el ISBN: ")
    
    for libro in biblioteca:
    
        if libro.isbn == isbn:
            
            print(libro.mostrar_info())
            return
    
    print("Libro no disponible.")

def menu():
    """Función para manejar el menú de opciones."""
    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agrega un libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Mostrar todos libros")
        print("5. Buscar un libro por ISBN")
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
    
    