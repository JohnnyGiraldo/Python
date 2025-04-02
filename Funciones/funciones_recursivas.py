print('*** Imprimir del 1 al 5 de forma recursiva ***')

# Definimos la función recursiva
def funcion_recursiva(numero):
    # Caso base
    if numero == 1:
        print(numero, end=' ')  # imprime 1
    else:
        funcion_recursiva(numero - 1)
        print(numero, end= ' ')

# Ejecutamos el programa Principal
funcion_recursiva(20)