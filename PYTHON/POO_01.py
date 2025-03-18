
# Declaración de clase

class Coche():

    # Declaración de atributos
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_enMarcha = False

    # Declaración de métodos
    def arrancar(self):  # self es una referencia a la instancia de la clase

        self.is_enMarcha = True     # Es como si pusieramos coche.is_enMarcha = True

    def estado(self):

        if (self.is_enMarcha == True):
            return "El coche está en marcha"
        
        else:
            return "El coche está parado"

# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.

miCoche = Coche()
miCoche2 = Coche()

# Acceso a un atributo de la clase Coche. Nomencaltura del punto.

print("El largo del coche es: ", miCoche.largo, "cm.")
miCoche.arrancar()
print(miCoche.estado())

# Acceso a un método de la clase Coche. Nomencaltura del punto.
print("Elcoche está arrancado: " , miCoche.arrancar())

# Modificamos el valor de una propiedad

miCoche2.ruedas = 10
print("El coche 2 tiene:" , miCoche2.ruedas, "ruedas")

# CREACIÓN DE LA CLASE

class Usuario():

    # Declaración de atributos
    nombre = "Angel"
    edad = 47
    login = "admin"
    password = "1234"
    email = "angel@loquesea.com"
    telefono = "123456789"

    # Declaración de métodos

    def resumen(self): # self es una referencia a la instancia de la clase

                print(
                    f'''Los datos del usuario son:
        Nombre: {self.nombre}
        Edad: {self.edad}
        Login: {self.login}
        Password: {self.password}
        Email: {self.email}
        Teléfono: {self.telefono}'''
                )
        
    def cambiaEdad(self):
        edadIntroducida = int(input("Introduce edad entre 18-100: "))
        if 18 < edadIntroducida < 100:
            
            print("Edad introducida correcta")
            return ""
        else:
            print("Edad introducida incorrecta")
            self.cambiaEdad()
            return ""
        
    def muestraEdad(self):
        print('La edad del usuario es:', self.edad, 'años')
        return ""
    
    # Creación de una instacnia de la clase Usuario a la que llamaremos administrador

administrador = Usuario()

    # una vez creado el objeto administrador, hacemos uso del método "resumen()" perteneciente
    # a la clase Usuario

administrador.resumen()

# Usamos los métodos cambiaEdad() y muestraEdad() de la clase Usuario.
print(administrador.cambiaEdad())
print(administrador.muestraEdad())




