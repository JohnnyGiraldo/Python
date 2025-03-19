print(f"***   SISTEMA DE REGISTRO DE EMPLEADOS  ***")

nombre_empleado = input("Introduce tu Nombre por favor:")
edad_empleado = int((input("Por favor Intruduce tu edad: ")))
salario_empleado = float((input("Ingresa tu salario de ingreso mensual: ")))
es_jefe_departamento = input("Eres jefe de departamento (Si/No)?")

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"


# Imprimimos los valores del empleado
print("\nDatos del Empleado")
print(f"Nombre : {nombre_empleado}")
print(f"La edad : {edad_empleado}")
print(f"el salario : {salario_empleado:.2f}")
print(f"Eres jefe de departamento ? {es_jefe_departamento}")