print('*** Argumentos VariBLES *** ')

def superheroe_superpoderes(superheroe,nombre,*args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    #Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')


# LLamar la funcion
superheroe_superpoderes('Spiderman','Peter Parker','Instinto arácnido','telaraña')
superheroe_superpoderes('Iroman','Tony Stark','Armadura','Play boy','Millonario','Vuelo integrado', 'rayo laser')

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino','Juan Perez',)