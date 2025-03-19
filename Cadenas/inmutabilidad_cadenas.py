# inmutabilidad en cadenas
cadena1 = "Hola Mundo"
# no podemos modificar los acarcterees    cadena1[0] = "h"
cadena2 = cadena1
cadena1 = "Adios"
print(cadena1)
print(cadena2)