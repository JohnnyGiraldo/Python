print('*** Operaciones con el tipo Set ***')

a = {1,2,3,4}
b = {3,4,5,6}
# Operacion para unir dos set con | carater de (pie)
union = a | b
print(f'Union de a | b: {union}')
print('***********************')
# operación de interseccion con & caracter de (andperson)
interseccion = a & b
print(f'Intersección de a & b: {interseccion}')
print('***********************')
# operación de diferencia , se eliminan los elementos que se repiten
diferencia = a - b
print(f'Diferencia de a - b: {diferencia}')