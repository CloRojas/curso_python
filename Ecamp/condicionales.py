num = int(input('Ingrese un número entero'))

if num < 0:
    print( num, 'es un número negativo')
    if num % 2 == 0:
        print(num, 'es un número par')
    else:
        print(num, 'es un número impar')
elif num > 0:
    print(num, 'es un número positivo')
    if num % 2 == 0:
        print(num, 'es un número par')
    else:
        print(num, 'es un número impar')
else:
    print('El número ingresado es cero')



