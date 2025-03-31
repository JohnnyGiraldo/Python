print('*** Dibujo de triángulo Simétrico ***')
numero_filas = int(input('Proporciona el Número de filas:  '))

# Iterar Sobre cada fila del triángulo
for fila in range (1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios_blanco}{asteriscos}')