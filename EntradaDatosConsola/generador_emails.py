print(f"***  Sistema generador de Emails ***")

# Datos del Cliente
nombre = input("Ingrese su Nombre:")
apellidos = input("Ingrese sus Apellidos: ")
nombre_empresa = input("Ingrese el Nombre de su empresa: ")
extension_dominio = input("Ingrese su extension del dominio del E-mail: ")

# Normalizar los valores
nombre_2 = nombre.lower().strip().replace(" ","")
apellido_2 = apellidos.lower().strip().replace(" ","")
nombre_empresa2 = nombre_empresa.lower().strip().replace(" ",".")
extension_dominio2 = extension_dominio.lower().strip().replace(" ",".")


# Generar el Email
email = f"{nombre_2}.{apellido_2}@{nombre_empresa2}{extension_dominio2}"
print(f'''Tu Nuevo Email Generado por el Sistema es: {email}
Felicidades!!!!!''')
