print('*** Suma Argumentos Variables ***')

# Función Sumar que acepta argumentos variables
def suma(*args):
    total = 0
    # Iteramos
    for numero in args:
        total += numero
    return total
# LLamamos a la función Sumar
resultado = suma(1,2,3,4,5,6,7,8,9,10)
print(f'Resultado de la Suma: {resultado}')
