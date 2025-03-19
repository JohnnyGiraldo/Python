print(f"*** SISTEMA DE DESCUENTOS VIP *** ")

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input(f"Cuantos Productos Compraste Hoy ?: "))
tiene_membresia = input(f"Tienes la membresia de la tienda (si/no) ?:")
es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO
                         and tiene_membresia.strip().lower() == "si")
print(f"Tienes acceso al descuento VIP ?: {
es_elegible_descuento
}")
