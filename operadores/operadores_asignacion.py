#Operadores de asignacion
print(f"***   OPERADORES DE ASIGNACION  ***")

numero = 5
print(f"Valor del numero : {numero}")
numero = 10
print(f"Valor del numero : {numero}")
cadena= "Saludos desde Python"
print(f"Valor de la cadena : {cadena}")

# Asignacion Multiple
x, y, z = 5, "Hola", -9.15
print(f"Valor de X={x}, Valor de Y={y}, valor de Z={z}")

# Asignacion Encadenada
a = b = c = 10
print(f"Valor de a={a}, Valor de b={b}, valor de c={c}")

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
# Aplicando el concepto de asignacion multiple, intercambiamos valores
x, y = y, x
print(f"El valor de X = {x}, El valor de Y es={y}")

# Recibir Multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu Nombre y Apellido separados por coma:').split(',')
print(f"tu Nombre es: {nombre.strip()}  "
      f"\ny tu Apellido es: {apellido.strip()}")


