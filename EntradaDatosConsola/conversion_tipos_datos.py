#  Conversion de Tipos de Datos

#  Convertir de cadena a numero

numero_cadena = "10"
numero_entrero = int(numero_cadena)

print(f"Valor Numerico en cadena: {numero_cadena}")
print(f"cadena a Entero: {numero_entrero}")

# Convertir de cadena a Flotante

numero_cadena = "3.14"
numero_flotante = float(numero_cadena)
print(f"Cadena a Flotante: {numero_flotante}")

# Convertir Numero a cadena

numero_entero = 25
numero_cadena = str(numero_entero)
print(f"Numero a cadena: {numero_cadena}")

# Convertir a booleano
# Tipo Bool es false en los siguientes casos :
# si el valor es 0, cadena vacia o none, entonces regresa False
# Regresa True, si el valor es distinto de 0, si es distinto de cadena vacia
#y tambien si es distinto de None

numero_entero = 0
booleano = bool(numero_entero)
print(f"Valor Booleano de 0: {booleano}") # Flse, incluye 0,  0.0

numero_entero = 5
booleano = bool(numero_entero)
print(f"Valor Booleano de 5:{booleano}")  # True

cadena = ""
booleano = bool(cadena)
print(f"Valor Booleano de cadena Vacia: {booleano}") #  Falso, incluye colecciones vacias

cadena = "Cadena con valor"
booleano = bool(cadena)
print(f" Valor Booleano de cadena no vacia: {booleano}") # True

variable = None
booleano = bool(variable)
print(f"Valor booleano de None: {booleano}") # debe regresar False por ser None