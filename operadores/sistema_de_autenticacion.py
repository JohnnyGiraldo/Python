print("*** SISTEMA DE AUTENTICACION ***")

usuario_valido = "admin"
pasword_valido = "123"

usuario = input("Ingresa tu usuario: ")
pasword = input("Ingresa tu password: ")

if usuario == usuario_valido and pasword == pasword_valido:
    print("Bienvenido al Sistema")
elif usuario == usuario_valido:
    print("Password Incorrecto, por favor de corregirlo!!")
elif pasword == pasword_valido:
    print("Usuario Incorrecto, favor corregirlo !!!")
else:
    print("Usuario y password incorrectos, por favor corregirlos !!")