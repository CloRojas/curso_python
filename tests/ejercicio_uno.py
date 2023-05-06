# 1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva 
#el valor de la letra asociada con esa calificación. con al siguiente tabla                                                                                                        

#     0   - 2     D
#     2.1 - 5     C
#     5.1 - 6     B
#     6.1 - 7     A

while True:
    try:
        puntaje_uno = float (input('Ingresa el primer puntaje: '))
        puntaje_dos = float (input('Ingresa el segundo puntaje: '))
        puntaje_tres = float (input ('Ingresa el tercer puntaje: '))
    except ValueError:
        print("Para ingresar tu puntaje debes utilizar numeros y separar decimales con punto.")
        continue

    if puntaje_uno < 0 or puntaje_uno > 7 or puntaje_dos < 0 or  puntaje_dos > 7 or puntaje_tres < 0 or puntaje_tres > 7 :
        print("El puntaje debe ser un número entre 0 y 7")
        continue
    else:
        break

puntajes = [puntaje_uno, puntaje_dos, puntaje_tres]


suma = 0
for puntaje in puntajes:
    suma = suma + puntaje

cantidad_puntajes = len(puntajes)
promedio = suma / cantidad_puntajes

if (promedio >= 0 and promedio <= 2):
    print('La calificación de tu promedio es D')
elif (promedio >= 2.1 and promedio <= 5):
    print('La calificación de tu promedio es C')
elif (promedio >= 5.1 and promedio <= 6):
    print('La calificación de tu promedio es B')
elif (promedio >= 6.1 and promedio <= 7):
    print('La calificación de tu promedio es A')
        
    





