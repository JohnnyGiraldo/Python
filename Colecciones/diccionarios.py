print('*** Diccionarios en Python ***')

# Creamos un diccionario de persona con clave y valor
persona = {
    'Nombre': 'Sergio',
    'Edad': 30,
    'Pais': 'Colombia',
    'Ciudad': 'Manizales',
    'Profesión': 'ingeniero'
}
print(f'Diccionario de persona : {persona}')
print('*********************')
# Acceder a los elementos del diccionario
print(f'Ciudad: {persona['Ciudad']}')
print(f'Profesión: {persona.get('Profesión')}')
print(f'Edad: {persona['Edad']}')
print('*************************')
print('Modificar un valor')
#modificar un valor del diccionario
persona['Edad'] = 55
print(f'Diccionario de persona : {persona}')
persona['Profesión'] = 'Mecánico'
print(f'Diccionario de persona : {persona}')
print('*********************')
# Eliminar un elemento
del persona['Ciudad']
print(f'Diccionario de persona : {persona}')
persona.pop('Profesión') #  Eliminar mediante el método Pop
print(f'Diccionario de persona : {persona}')
print('*********************')
# Iterar los Elementos de un Diccionario (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')
print('*********************')
print('Valores')
print(f'Valores del diccionario: ')
# Obtener solo los valores
for valor in persona.values():
    print(f'- Valor: {valor}')
print('*********************')
print('LLaves')
# Obtener las llaver
for llave in persona.keys():
    print(f'- : {llave}')