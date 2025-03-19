print('***  SISTEMA DE PRESTAMO DE LIBROS ***')

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input('Cuentas con  redencial de estudiante (si/no)? : ')
distancia_biblioteca_km = int(input('A Cuantos km vives de la biblioteca? :'))

es_elegible_prestamo = (tiene_credencial.strip().lower() == 'si'
                        or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)

print(f'eres elegible para prestamo de libros ? {es_elegible_prestamo}')