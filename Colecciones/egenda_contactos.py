print('*** Agenda de Contactos ***')

agenda = {
    'Carlos': {
        'telefono':'321585487',
        'email':'carlos@mail.com',
        'direccion': 'calle principal 132'
    },
    'Maria':{
        'telefono':'99887733',
        'email':'maria@mail.com',
        'direccion':'Avenida Central 456'
    },
    'Pedro': {
        'telefono':'55139078',
        'email':'pedro@mail.com',
        'direccion':'Plaza Mayor 789'
    }
}
print(f'Agenda: {agenda}')

# Acceder a la informacion de un contacto en especifico
print(f'''Información del telefono de Maria es: 
     {agenda['Maria']['telefono']}''')

#Imprimir la direccion de email y direccion de Maria
print(f'''Información del email de Maria es: 
    Email: {agenda['Maria']['email']}''')
print('***********************')
print(f'''Información de la dirección de Maria es: 
    {agenda['Maria']['direccion']}''')

# Agregar un Nuevo contacto
agenda['Ana']={
    'telefono':'55678392',
    'email':'ana@email.com',
    'direccion':'Calle salvador diaz 321'
}
print(agenda)
# Eliminar un contacto existente
agenda.pop('Pedro')
# del agenda['Pedro']   # metodo (del) para eliminar
print(agenda)

# Mostramos los contactos de la agenda
print(f'\nContactos en la Agenda')

for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}
''')