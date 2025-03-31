from random import randint

print('*** Juego de adivinanzas ***')

numero_secreto = randint(1, 50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el Numero Secreto el cual es entre (1 al 50): '))
    # Agregamos una ayuda para orientar al jugador
    if adivinanza < numero_secreto:
        print('El Número es mayor')
    elif adivinanza > numero_secreto:
        print("El Numero secreto es menor")
# Incrementamos la variable de intentos
    intentos += 1
if adivinanza == numero_secreto:
    print(f'Felicidades, adivinaste el número secreto en: \n{intentos} intentos')
else:
    print(f'Lo siento, Has agotado tus intentos máximos: {INTENTOS_MAXIMOS} ')
    print(f'El Número secreto era: {numero_secreto}')