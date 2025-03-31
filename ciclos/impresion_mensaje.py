print('*** Repeticion de un Mensaje ***')

mensaje = input('Proporciona un mensaje a repetir: ')
numero_repeticiones = int(input('Proporciona el número de repeticiones: '))

# Iterar sobre el rango de repeticiones
for i in range (numero_repeticiones):
    print(f'{i+1} - {mensaje}')

for _ in range (numero_repeticiones):
    print(mensaje)