print('*** Lista de Suscriptores Dinámica ***')

# Definimos el set inicial
# suscriptores = {} # aqui se define un diccionario vacio
suscriptores = set() # definimos un set vacio

numero_suscriptores = int(input('Proporciona el número de suscriptores iniciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'Lista de suscriptores Inicial: {suscriptores}')
print('*********************')
# Verificamos  si un nuevo suscriptor ya esta en la lista
nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El Nuevo suscriptor ya esta en la lista: {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El Nuevo suscriptor se ha agregado a la lista de suscriptores: {nuevo_suscriptor}')

print(f'Lista de suscriptores actualizada: {suscriptores}')

#Eliminar un suscriptor
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor a eliminar de la lista fue: {suscriptor_eliminar}')
print(f'Lista de suscriptores actualizada: {suscriptores}')

# Verificamos la cantidad total de suscriptores hasta el momento
print(f'Cantidad total de suscriptores es: {len(suscriptores)}')

# Mostramos todos los suscriptores
print('---Lista de Suscriptores ---')
for suscriptor in suscriptores:
    print(f'{suscriptor}')