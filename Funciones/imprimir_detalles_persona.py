print('*** Imprimir detalles de una persona usando kwargs ***')

# Función que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')

    # Iteramos
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

#LLamamos a la funcion
imprimir_detalle_persona(nombre='Karla',edad=30,Pais='Colombia')
imprimir_detalle_persona(nombre='Johnny',edad=44,Pais='Colombia',profesión='Tecnólogo')