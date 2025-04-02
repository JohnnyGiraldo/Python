print('*** Alcance de Variables ***')

# Variable Global
contador_global = 0

def incrementas_contador():
    # Declaramos una variable local
    contador_local = 0

    # Usar la variable global
    global contador_global
    # Incrementamos la variable global
    contador_global += 1

    # Incrementamos la variable local
    contador_local += 1

    # Imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador Global: {contador_global}\n')

# LLamamos varia veces la función
incrementas_contador()
incrementas_contador()
incrementas_contador()

# terminando el programa
print(f'Valor variable global: {contador_global}')