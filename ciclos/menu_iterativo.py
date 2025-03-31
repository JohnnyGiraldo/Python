print('*** Sistema de administracion de cuentas ***')

salir = False
while not salir:
    print(f'''Menu:
    1. Crear cuenta
    2. Eliminar Cuenta
    3. Salir''')
    opcion = int(input('Escoge una opcion: '))
    if opcion == 1:
        print('Creando tu cuenta ....')
    elif opcion == 2:
        print('Eliminando tu cuenta....')
    elif opcion == 3:
        print('Saliendo del sistema. hasta pronto! ,,,\n')
    else:
        print('Opcion Inválida, proporciona otra opción...')
else:
    print('Terminando el sistema de administración de cuentas')