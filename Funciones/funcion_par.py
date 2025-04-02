print('*** Funcion Par ***')

# Función para saber si un número es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# LLamamos a la función
if __name__== '__main__':
    numero = int(input('Proporciona un Valor Numérico: '))
    print(f'Número par? {es_par(numero)}')