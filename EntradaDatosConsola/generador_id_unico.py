from random import randint

print(f"***   Sistema Generado de ID Unico ***")

nombre = input("Ingrese su Nombre:")
apellido = input("Cual es tu apellido")
anio_nacimiento = input("Cual es tu año de Nacimiento (YYYY)?: ")

# Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento2 = anio_nacimiento.strip()[2:] # tambien puede ser [2:4]

#Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el valor de id unico
id_unico = f"{nombre_2}{apellido_2}{anio_nacimiento2}{aleatorio}"

print(f"""\nHola {nombre}
Tu Nuevo Numero de Indentificacion ID Generado por el sistema es: {id_unico}
Felicidades !!!""""")


