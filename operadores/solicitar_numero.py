print( '***  SOLICITAR NUMERO *** ')

# Solicitar un Numero
solicitud = int(input("por favor ingresa un numero: "))

# validacion

if solicitud > 0:
    print(f"El Numero es: {solicitud} positivo ")
elif solicitud < 0:
    print(f"El Numero es:  {solicitud} negativo")
else:
    print(f"El Numero es Cero: {solicitud}")

