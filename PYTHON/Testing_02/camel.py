
import re

def capitalize(word):

    """Convierta la palabra para que tenga la primera letra en mayúscula, el rsto en minúsculas."""

    return word[0:1].upper() + word[1:].lower()
# Los segmentos no producen errores de tipo "index out of bounds".
# Así que esto todavía funciona en cadenas vacías y cadenas de longitud 1

def lowercase(word):

    """Convierta la palabra en minúsculas."""

    return word.lower()

def camel_case(sentence):

    remove_multiple_spaces = re.sub(r'\s+', ' ', sentence) # Reemplaza 
    # cualquier grupo de espacios en blanco con un solo espacio.
    remove_surrounding_spaces = remove_multiple_spaces.strip() # Elimina cualquier
    # espacio en blanco restante.

    words = remove_surrounding_spaces.split(' ') # Segmenta por espacios.
    first_word = lowercase(words[0]) # Convierte la primera palabra a minúsculas.
    
# Escribe con mayúsculas la segunda palabra y las siguientes y las pone en una nueva lista.

    capitalized_words = [capitalize(word) for word in words[ 1: ] ] 

# Reúne todas las palabras en una lista
    camel_cased_words = [first_word] + capitalized_words

# Vuelve a unir las palabras.
    camel_cased_sentence = ''.join(camel_cased_words)

    return camel_cased_sentence

def main():
    sentence = input('Introduce una frase: ')
    camelcased = camel_case(sentence)
    print(camelcased)

if __name__ == '__main__':
    main()
    