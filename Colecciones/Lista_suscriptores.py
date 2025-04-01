print('*** Lista de Suscriptores ***')

suscriptores = {'luisa@mail.com','marcos@mail.com','elena@mail.com'}
print(f'Lista de suscriptores Inicial: {suscriptores}')
print('*********************')
# Verificamos  si un nuevo suscriptor ya esta en la lista
nuevo_suscriptor = 'lucy@mail.com'
if nuevo_suscriptor in suscriptores:
    print(f'El Nuevo suscriptor ya esta en la lista: {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El Nuevo suscriptor se ha agregado a la lista de suscriptores: {nuevo_suscriptor}')

print(f'Lista de suscriptores actualizada: {suscriptores}')
print('*********************')
#Eliminar un suscriptor existente
suscriptor_eliminar = 'elena@mail.com'
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor a eliminar de la lista fue: {suscriptor_eliminar}')
print(f'Lista de suscriptores actualizada: {suscriptores}')
print('*********************')
# Verificamos la cantidad total de suscriptores hasta el momento
print(f'Cantidad total de suscriptores es: {len(suscriptores)}')
print('*********************')
# Mostramos todos los suscriptores
print('---Lista de Suscriptores ---')
for suscriptor in suscriptores:
    print(f'{suscriptor}')