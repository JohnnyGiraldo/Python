print('*** Creacion y Validacion de un password ***')

password = input('Ingresa un Password (Debe de tener al Menos 6 caracteres: ')

# Validar el password
while len(password) <6:
    print(f'El password es inválido, debe de tener al menos 6 caracteres ')
    password = input('Ingresa un Nuevo valor de password: ')
else:
    print('El valor del password es válido')