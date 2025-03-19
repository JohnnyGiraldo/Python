print('***  OPERADOR NOT ***')
condicion1 = True
resultado = not condicion1

print(f"operador not {condicion1}: {resultado}")

# Revisar si una variable es cadena vacia
nombre = "Juan"
es_cadena_vacia = not nombre
print(f'\nLa variable no tiene ningun valor ? {es_cadena_vacia}')

# Revisar si una variable no tiene ningun valor asignado
variable = None
es_variable_sin_valor = not variable
print(f"\nLa variable no tiene ningun valor asignado? : {es_variable_sin_valor}")
