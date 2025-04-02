print('*** Listas y Diccionarios ***')

personas = [
    {
        'nombre': 'Regina',
        'apellido':'Florez',
        'edad':21
    },
    {
        'nombre': 'Alejandro',
        'apellido':'Reyes',
        'edad':32
    }
]
print(personas)
# Acceder a un diccionario desde una lista
print(f'''Detalle del primer elemento de la lista :
    Nombre: {personas[0].get('nombre')}'
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}''')

# recorrer los elementos de la lista
print('\n')
for contador, persona in enumerate(personas):
    print(f'{contador} - Persona: {persona}')
    # print(f'Detalle: Nombre: {persona.get('nombre')}, Apellido: {persona.get('apellido')}')

