#Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero. 
#Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio),
#forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.

print('¿ A que trimestre del año pertenece el mes ingresado?')

meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

while True:
    try:
        mes = int (input('Ingresa el mes con valor numerico: '))
    except ValueError:
        print("Debes ingresar un valor numerico")
        continue
    if mes <= 0  or mes >= 13:
        print("Debe ser un numero entre 1 y 12")
        continue
    else:
        break

mes_elegido = meses[mes-1]

if mes_elegido in meses[:3]:
    print( 'El mes', mes, '(', mes_elegido,'), forma parte del primer trimestre.')
elif mes_elegido in meses[:6]:
    print( 'El mes', mes, '(', mes_elegido,'), forma parte del segundo trimestre.')
elif mes_elegido in meses[:9]:
    print( 'El mes', mes, '(', mes_elegido,'), forma parte del tercer trimestre.')
else:
    print( 'El mes', mes, '(', mes_elegido,'), forma parte del cuarto trimestre.')

   