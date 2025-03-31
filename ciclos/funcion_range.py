print('*** Función Range ***')

print('Secuencia del 0 al 4:')
# inicio = 0 Por default
# fin = 5 - 1 = (4)
# Incremento = 1 ( Opcional )
for i in range(5): # fin de la secuencia = 5 - 1 = (4)
    print(i, end=' ')

print('\n\nSecuencia del 10 al 20: ')
for i in range(10, 20 + 1): # fin de la secuencia = 5 - 1 = (4)  # Incluimos el número límite
    print(i, end=' ')

print('\n\nSecuencia del 20 al 30 de 2 en 2:')
for i in range(20, 30 + 1, 2): # fin de la secuencia = 5 - 1 = (4)  # Incluimos el número límite
    print(i, end=' ')