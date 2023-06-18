# requisitos = {
#     'título': 'requerido',
#     'notas': 'requerido',
#     'foto': 'opcional'
# }

# print(requisitos)

# #acceder a una propiedad
# print('Las notas son de tipo:', {requisitos['notas']})
# print('La foto es de tipo:', {requisitos['foto']})

# #modificar una propiedad
# requisitos ['foto'] = 'requerido'
# requisitos ['título'] = 'opcional'
# print('El título es de tipo:', {requisitos['título']})
# print('La foto es de tipo:', {requisitos['foto']})

# #Construir diccionario de datos para guardar la informacion de un avión, 
# #al menos 6 propiedades, imprima 3 de ellas y cambie el valor de 2
# #al menos debe existir una propiedad booleana, una entera, una flotante
# #un arreglo, un diccionario y un string

# avion = {
#     'modelo': 'DDD454',
#     'cap_pasajeros': 100,
#     'vuelo_activo':True,
#     'capacidad_combustible_lt': 220.3,
#     'asientos':['economic','turist','bussiness'],
#     'tripulantes':{
#         'piloto':'Marcelo Mora'
#         'auxiliar1': 'Luisa Rojas'
#     }

# }

#Construya un programa que solicite el peso en kg de una persona y si el peso 
#está entre 60 y 70 kg recomiende una dieta de 5 comidas altas en carbohidratos
#si el peso está entre 70 y 80 kg, 4 comidas altas en proteinas y si es mayor
#a 80 una dieta alta en fibras de 3 comidas. Utilice solo diccionarios para agrupar menues

peso_persona = float(input('Ingrese peso en kilos: '))

menues = {
    'dieta_carbo': {
    'desayuno':'cereales de chocolate con leche',
    'colación':'barra energética',
    'almuerzo': 'pastas',
    'once':'pizza',
    'cena':'papas'
    },

    'dieta_proteinas' : {
    'desayuno':'huevo ',
    'almuerzo': 'legumbres',
    'once':'pan con huevo',
    'cena':'carne con ensaladas',
    },
    'dieta_fibras' :{
    'desayuno':'avena',
    'almuerzo': 'ensaladas',
    'once':'pan integral',
    'cena':'ensaladas'   
    }
}

if peso_persona >= 60 and peso_persona <=70:
    print('Dieta recomendada alta en carbohidratos:', menues['dieta_carbo'])
elif peso_persona > 70 and peso_persona <=80:
    print('Dieta recomendada proteica:', menues['dieta_proteinas'])
elif peso_persona > 80 :
    print('Dieta recomendada alta en fibra:', menues['dieta_fibras'])
else:
    print('Fuera de rango')


######
# Dieta recomendada en función del rango de peso

dietas = {

     'flaco': {

        'numero_comidas': 5,

         'tipo_dieta': 'alta en carbohidratos',

        'menu': [

            'Desayuno: Pan con mermelada y juguito de naranja',

            'colación: Barra de proteina',

            'Almuerzo: Pasta con salsa de tomate',

            'once: avena y granola',

            'Cena: Arroz con vegetales'

        ]

    },

    'medio': {

        'numero_comidas': 4,

        'tipo_dieta': 'alta en proteínas',

    'menu': [

        'desayuo: Huevos revueltos con tostadas',

        'almuerzo: Pechuga de pollo con ensalada',

        'once: jugo con proteinas',

        'Cena: pollo a la parrilla con brócoli'

         ]

     },

     'obeso': {

         'numero_comidas': 3,

         'tipo_dieta': 'alta en fibra',

        'menu': [

        'Desayuno: Avena con frutas y nueces',

        'Almuerzo: Quinoa con vegetales',

         'once: Ensalada de  porotos negros '

         ]

     }

}




# Solicitar el peso de la persona

peso = float(input("Ingrese su peso en kg: "))




# condicional para decidir




#dieta_recomendada pasa a ser una propiedad del diccionario




if peso >= 60 and peso <= 70:

    dieta_recomendada = 'flaco'

elif peso >= 71 and peso <= 80:

    dieta_recomendada = 'medio'

elif peso > 80:

    dieta_recomendada = 'obeso'

else:

    dieta_recomendada = None




# Imprimir la dieta recomendada

if dieta_recomendada:

    print("Su nutricionista le recomienda una dieta de", dietas[dieta_recomendada]['numero_comidas'], "comidas",dietas[dieta_recomendada]['tipo_dieta'])

    print("El menú es:")

    for comida in dietas[dieta_recomendada]['menu']:

    print(comida)

else:
    print("coloque un peso real ")