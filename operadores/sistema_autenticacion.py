print('*** SISTEMA AUTENTICANCION ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario_ingresado = input('ingresa usuario? :')
password_ingresado = input('Ingresa contraseña: ')

son_datos_correctos = (usuario_ingresado.strip() == USUARIO_VALIDO
                       and password_ingresado.strip() == PASSWORD_VALIDO)

print(f"datos correctos? {son_datos_correctos}")