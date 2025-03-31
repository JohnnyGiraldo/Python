print('*** Break y Continue ***')
# Ejemplo con break
print('Palabra Break:')
for numero in range(1, 10):
    if numero % 2 == 0: # Número par
        print(numero)
        break # Salimos del ciclo inmediatamente

# Ejemplo con continue
print('\nPalabra continue:')
for numero in range(1, 10):
    if numero % 2 == 1:   # Número impar
        continue
    print(numero)