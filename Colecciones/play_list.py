print('*** Play List de Canciones ***')

# Creamos la lista vacia
lista_reproduccion = []
numero_canciones = int(input('Cuantas canciones deseas agregar?: '))

# Iteramos cada elemento de la lista para agregar un Nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporcione la canción {indice + 1}: ')
    lista_reproduccion.append(cancion)


# Comenzamos a agregar canciones
lista_reproduccion.append('Hotel california - Eagles')
lista_reproduccion.append('Staying Alive - Bee Gees')
lista_reproduccion.append('Dream on - Aerosmith')

# Ordenar la Lista en orden Alfabetico con el metodo . sort
lista_reproduccion.sort()

# # Mostrar la lista de Canciones
# print(f'\nLista de reproduccion en orden alfabético:')
# print(lista_reproduccion)

# Mostrar la Lista Iterando los elementos
print('\niteramos el Play List')
for cancion in lista_reproduccion:
    print(f'* {cancion}')