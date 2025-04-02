print('*** Comprensión de Listas ***')

#  Una lista con el cuadrado de cada número
numeros = [1,2,3,4,5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

# Lista de Números pares
numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# Lista saludando a cada Nombre
nombres = ['Ana','jerónimo','Carlos']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)