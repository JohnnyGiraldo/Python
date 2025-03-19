print('***  VALOR DENTRO DEL RANGO ***')



# Definir las constantes
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

# Solicitar un valor entre 0 y 5
VALOR_USUARIO = int(input(f'ingrese el valor entre {VALOR_MINIMO} y {VALOR_MAXIMO} dentro gato siamesdel rango: '))

# verificamos si el dato se encuentra dentro del rango
dentro_rango = VALOR_USUARIO >= VALOR_MINIMO and VALOR_USUARIO <= VALOR_MAXIMO
esta_dentro_rango = VALOR_MINIMO <= VALOR_USUARIO <= VALOR_MAXIMO
print(f'Valor dentro del rango?: {dentro_rango}')
