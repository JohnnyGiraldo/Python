print("***   Generador de Email   ***")

nombre_completo = (" Johnny Alexander Giraldo ")
print(f"Nombre de usuario: {nombre_completo}")
# Procesar o normalizar el nombre del usuario
# Limpiamos los espacios en blanco al inicio y al final
nombre_normalizado = nombre_completo.strip()
# Reemplazamos los espacios en blanco por puntos
nombre_normalizado = nombre_normalizado.replace(" ",".")
# Convertimos a Minusculas
nombre_normalizado = nombre_normalizado.lower()
print(f"Nombre usuario Normalizado: {nombre_normalizado}")

#Datos de la empresa
nombre_empresa = "Global mentoring."
print(f"\nNombre empresa: {nombre_empresa}")
extension_dominio = "gmail.com"
print(f"Extension del Dominio: {extension_dominio}")

# quitamos los espacios en blanco y convertimos a mayusculas
nombre_empresa_normalizado = nombre_empresa.replace(" ","").lower()
dominio_email = f"@{nombre_empresa_normalizado}{extension_dominio}"
print(f"dominio del email normalizado: {dominio_email}")
#creamos el email final
email = f"{nombre_normalizado}{dominio_email}"
print(f"\nEmail final generado: {email}")