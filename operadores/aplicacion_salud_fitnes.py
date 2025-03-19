print("*** APLICACION DE SALUD Y FITNESS ***")

# Definimos las constantes
META_PASOS_DIARIOS = 10000
CALORIAS_PASO = 0.04    # Valor aproximado, son kilocalorias

# Solicitamos los valores al usuario
nombre_usuario = input("Por favor ingresa tu Nombre:")
pasos_diarios = int(input("Cuantos pasos has caminado Hoy?:"))

# Verificar si el usuario alcanzo la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = "SI" if meta_alcanzada else "NO"

# Calculamos las calorias quemadas

calorias_quemadas = pasos_diarios * CALORIAS_PASO

# Mostramos la informacion

print(f"\nNombre del usuario: {nombre_usuario}")
print(f"Pasos caminados hoy: {pasos_diarios}")
print(f"Calorias quemadas hoy: {calorias_quemadas} Kilo-calorias")
print(f"Meta de pasos diaria alcanzada: {meta_alcanzada_txt}")
print(f"la meta de pasos diarios es de: {META_PASOS_DIARIOS} pasos")
