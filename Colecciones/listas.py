print('*** Manejo de Listas ***')

mi_lista = [1, 2, 3, 4, 5]
print(f"{mi_lista} -> Lista Original")

# Largo de una lista
print(f"Largo de una lista: {len(mi_lista)}")

# Acceder a los elementos de la lista por índice
print(f'Accedemos al valor del índice 4: {mi_lista[4]}')
print(f'Accedemos al último índice de la lista: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor del índice 1: {mi_lista[1]}')

# Obtener sublista
sublista = mi_lista[1:3] # Genera una sublista del índice 1 al 2 (El 3 no se incluye)
print(f'Sublista [1:3]: {sublista}')

# Agregar un Nuevo elemento al final de la Lista
mi_lista.append(6)
print(f'{mi_lista} -> se agrego el elemento 6')

# Añadir un nuevo elemento en un índice especifico
mi_lista.insert(2, 25)
print(f'{mi_lista} -> se agrego el en número 25 al índice 3')

# Eliminar elementos de una lista
# Usando el método remove
mi_lista.remove(5)
print(f'{mi_lista} -> Se removio el valor 5')
# Removemos por índice con el metodo Pop
mi_lista.pop(1) #Remueve el elemento del índice 1
print(f'{mi_lista} -> Se Elimino el índice 1')

# Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} -> Se Elimino el índice 2 con del')