print('*** Función con argumentos por Nombre ***')

def imprimir_persona(nombre,apellido='',edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero Llamamos la función pasando los argumentos de manera posicional
imprimir_persona('Ricardo','Qintana',32)
# Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Carlos',apellido='Rojas',edad=28)
#Llamar la funcion usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=28,apellido='Rojas',nombre='Carlos')
#Argumentos con valores por default
imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Jonny',apellido='Giraldo')
imprimir_persona(apellido='Piedrahita',nombre='Luz marina')
