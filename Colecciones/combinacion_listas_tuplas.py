from desempaquetado_de_duplas import descripcion

print('*** Combinación de listas y Tuplas ***')
# Definir una Lista que almacena tuplas de productos

productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00),
]
'''Imprimir la informacion de cada producto
 y además calculamos el precio total'''
precio_total = 0

print(f'Información de los productos: ')
for producto in productos:
    id, descripcion, precio = producto   # Unpacking
    print(f'Producto: id = {id}, descripción: {descripcion}, Precio = ${precio}')
    precio_total += precio  # Producto[2]
print(f'Precio total de los productos = ${precio_total}')
