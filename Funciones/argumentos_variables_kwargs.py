
# * args - arguments - tupla
# **kwargs - keyword arguments (key,value) como un dict
print('*** Argumentos variables en forma de Diccionario ***')

def superheroe_superpoderes(nombre,*args,**kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas información: {kwargs}')

# Llamamos la función
superheroe_superpoderes('Spiderman','Instinto Arácnido',edad=17,empresa="Marbel")
superheroe_superpoderes('Ironman','Armadura','Play boy', edad=45, estato_civil='soltero')

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', personalidad = 'Buena onda')
