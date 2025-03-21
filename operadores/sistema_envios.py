print(f"*** SISTEMA DE ENVIOS ***")

#Definimos las tarifas de envio por Kilogramo
TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

# Solicitamos los valores de destino y peso al usuario
destino = input("ingresa el destino del paquete (nacional/internacional): ")
peso = float(input("Ingresa el peso del paquete (en Kg): "))

# Calculo del envio del paquete
costo_envio = None
destino = destino.strip().lower()
if destino == "nacional":
    costo_envio = peso * TARIFA_NACIONAL
elif destino == "internacional":
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    print(f"Destino no válido, ingresa el destino nacional o internacional")

# Mostramos el costo del envio solo si es un valor válido
if costo_envio is not None:
    print(f"El costo de envio del paquete es: ${costo_envio:.2f}")