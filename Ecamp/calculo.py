num = int(input('Ingrese un número entero positivo para calcular su factorial'))

if num >= 0:
    resultado = 1
    factorial = 1
    while  factorial <= num:
        resultado = resultado * factorial
        factorial = factorial + 1
    print('El factorial de', num, 'es', resultado)
else:
    print('Número ingresado no es entero positivo')