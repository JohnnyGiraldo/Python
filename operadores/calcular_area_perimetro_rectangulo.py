print('*** CALCULO AREA Y PERIMETRO DE UN RECTANGULO ***   ')

# Solicitar los valores de altura y base a el usuario

base = float(input(f"Ingrese la base del rectangulo: "))
altura = float(input(f"Ingrese la altura del rectangulo: "))

# Calcular el area del rectangulo
area = base * altura

# Calcular el perímetro
perimetro = 2 * (base + altura)

print(f"El area del rectangulo es : {area} y el perimetro del rectangulo es: {perimetro}")