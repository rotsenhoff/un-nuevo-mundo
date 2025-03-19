
# USO DE LA FUNCIÓN SUPER

class Padre(object):    # Creamos la clase Padre

    def __init__(self,ojos,cejas):
    # Definimos los atrbutos
        self.ojos = ojos
        self.cejas = cejas

class Hijo(Padre):    # Creamos clase hija que hereda de Padre

    def __init__(self, ojos, cejas, cara):    # Creamos el constructor de la clase
        # especificando atributos
        super().__init__(ojos, cejas)
    # Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara    # Especificamos el nuevo atributo para Hijo

Tomas = Hijo ('Marrones', 'Negras', 'Larga')

print (Tomas.ojos, Tomas.cejas, Tomas.cara)

    