# Cree una función notaFinal, que calcule la nota final de un estudiante en función de dos parámetros: 
#una nota para el examen y una cantidad de proyectos completados.
#Esta función debe tomar dos argumentos: examen - calificación del examen (de 0 a 100); 
#proyectos - número de proyectos completados (de 0 en adelante);
#Esta función debería devolver un número (calificación final). Hay cuatro tipos de calificaciones finales:

#100, si la calificación del examen es superior a 90 o si el número de proyectos terminados es superior a 10.
#90, si la calificación del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
#75, si la calificación del examen es superior a 50 y si el número de proyectos completados es mínimo 2

while True:
    try:
        nota_examen = int (input('Ingresa nota exámen: '))
        num_proyectos = int (input('Ingresa número de proyectos completados: '))
    except ValueError:
        print("Recuerda ingresar números enteros.")
        continue

    if nota_examen < 0 or nota_examen > 100  :
        print("La nota del exámen va de 0 a 100")    
    elif num_proyectos  < 0 :
        print('Si no entregaste proyectos ingresa 0')
        continue
    else:
        break

def notaFinal(nota_examen,num_proyectos):
    if nota_examen > 90 or num_proyectos > 10:
        return '100'
    elif nota_examen > 75 and num_proyectos >= 5:
        return '90'
    elif nota_examen > 50 and num_proyectos >= 2:
        return '75'
    else:
        return '0'

calificacion = notaFinal(nota_examen, num_proyectos)
print('Tu calificación final es', calificacion)

