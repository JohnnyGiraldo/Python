print('*** Manejo de Sets ***')
# Crear un Conjunto
mi_set = {1,2,3,4,5,4}
print(f'Mi set: {mi_set}')

# Agregar Elementos al Set
mi_set.add(6)
mi_set.add(7)
mi_set.add(8)
print(f'Mi set modificado: {mi_set}')

# Intentamos agregar un elemento duplicado
mi_set.add(3)
print(f'Mi set con el elemento duplicado: {mi_set}') # se ignora el elemento duplicado

# Eliminar un Elemento del conjunto
mi_set.remove(4)
print(f'Mi set con el elemento (4) Eliminado: {mi_set}')

# Iterar Los elementos del set
for elemental in mi_set:
    print(elemental, end='-')

# Comprobar si existe un elemento en el set
print(f'Existe el valor de 1 en el set?: \n{1 in mi_set}')

# Obtenemos la longitud del set
print(f'Largo o longitud del conjunto es: {len(mi_set)}')