# Definimos la función
def sumar(a,b):
    resultado_suma = a + b
    return resultado_suma

print(__name__)

# Prueba de la funcion sumar
if __name__ == '__main__':
    print(f'Prueba función sumar desde el módulo: {sumar(15,30)}')
