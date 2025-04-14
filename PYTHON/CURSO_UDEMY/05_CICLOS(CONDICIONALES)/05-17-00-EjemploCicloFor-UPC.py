print('*** Repeticion de un Mensaje ***')

mensaje = input('Proporciona un mensaje a repetir: ')
numero_de_repeticiones = int(input('Proporciona el número de repeticiones: '))

# iterar sobre el rango de repeticiones
for _ in range(numero_de_repeticiones): # Se usa _ porque no se necesita el valor de la variable, 
    # pero de esta manera se cumple con la sintaxis del for
    
    print(mensaje)