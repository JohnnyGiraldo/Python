print('*** GENERACION TICKET DE VENTA ***')

precio_leche = float(input('Ingrese el precio de la leche: '))
precio_pan = float(input('Ingrese el precio del pan: '))
precio_lechuga = float(input('Ingrese el precio de la lechuga: '))
precio_platanos = float(input('Ingrese el precio de los platanos: '))
descuento_porcentaje = int(input('Aplicar algun descuento (%)?'))

# calculo del subtotal sin impuestos
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# aplicar el descuento
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# calculo del impuesto (16%)
impuesto = subtotal * 0.16

# Calcular el total de la compra (con impuestos)
costo_total_compra = subtotal + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje}%)
subtotal con descuento: ${subtotal_con_descuento}
Impuesto (16%) $ {impuesto:.2f}
costo total de la compra: ${costo_total_compra:.2f}''')