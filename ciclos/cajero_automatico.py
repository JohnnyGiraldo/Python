print('*** APLICACIÓN DE CAJERO AUTOMÁTICO ***')

saldo = 1000
salir = False

while not salir:
    print(f''' Operaciones que puedes realizar:
    1. Consultar el Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Elige una opción: '))
    if opcion == 1:
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Proporciona la cantidad a retirar: '))
        if retiro <= saldo:
            saldo -= retiro # saldo = saldo - retiro
            print(f'Tu nuevo saldo es: {saldo:2f}\n')
        else:
            print(f'No cuentas con el saldo suficiente. Saldo actual es: ${saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito  # saldo = saldo + deposito
        print(f'Tu nuevo saldo es: {saldo:.2f}\n')
    elif opcion == 4:
        print(f'Saliendo del cajero automatico. Hasta pronto !!! ')
        salir = True
else:
    print('Terminando la Opción de cajero Automático! ')