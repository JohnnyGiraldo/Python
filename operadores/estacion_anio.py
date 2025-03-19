print("*** ESTACION DEL AÑO ***")
#Solicitar al cliente el valor del mes valor numerico entero entre 1 y 12
valor_mes = int(input("Ingrese el mes del año en numero (1-12): "))
estacion = None
#Validacion del mes
if valor_mes == 1 or valor_mes == 2 or valor_mes == 12:
    estacion = "invierno"
elif valor_mes == 3 or valor_mes == 4 or valor_mes == 5:
    estacion = "Primavera"
elif valor_mes == 6 or valor_mes == 7 or valor_mes == 8:
    estacion = "Verano"
elif valor_mes == 9 or valor_mes == 10 or valor_mes == 11:
    estacion = "Otoño"
else:
    estacion = "Estación Desconocida"
# Imprimir el resultado de las validaciones
print(f"La estación para el mes proporcionado para el mes: {valor_mes}  es: {estacion}")
