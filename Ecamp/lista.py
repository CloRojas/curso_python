
lista = []
for numer in range(10):
    num= int(input('Ingrese un número: '))
    lista.append(num)

    if num == 0:
        print(num,'el numero es 0')
    elif num %2 == 0:
        print(num, 'es par')
    else:
        print(num, 'es impar')
print(lista)


