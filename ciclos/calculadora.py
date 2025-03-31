print('*** CALCULADORA EN PYTHON ***')

operando1 = operando2 = resultado = 0
salir = False

while not salir:
    print(f''' Operaciones a realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir ''')
    opcion = int(input('Elige una opción: '))
    # Vamos a solicitar el valor de los operadores
    if 1 <= opcion <= 4:
        operando1 = float(input('Ingresa el valor 1: '))
        operando2 = float(input('Ingresa el valor 2: '))
    # Revisamos el tipo de operación a realizar
    if opcion == 1: # Suma
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2: # Resta
        resultado = operando1 - operando2
        print(f'El resultado de la Resta es: {resultado:.2f}\n')
    elif opcion == 3:  # Multiplicación
        resultado = operando1 * operando2
        print(f'El resultado de la Multiplicación es: {resultado:.2f}\n')
    elif opcion == 4:  # División
        resultado = operando1 / operando2
        print(f'El resultado de la División es: {resultado:.2f}\n')
    elif opcion == 5:
        print(f'Saliendo del programa de calculadora. Hasta pronto!!!')
        salir = True
else:
    print('Opcion inválida, selecciona otra opcion...\n! ')