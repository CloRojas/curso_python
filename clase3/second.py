# empty_dic = {}

# fullfiled_dic = {
#     "id": 1,
#     "name":"Valeria",
#     "age": 25,
#     "address": "Catedral #254"
# }


# print(fullfiled_dic.get("name"))

# fullfiled_dic['nacionalidad']= "chilena"

# fullfiled_dic['name']="Barbara"
# fullfiled_dic['deporte']='football'


# print(fullfiled_dic)



# print(empty_dic)
# print(fullfiled_dic)

lista_1 = ['a1','b2']
dict_converted = dict(lista_1)
print(lista_1, dict_converted)

tupla_1 = ('a1', 'b2')
print(tupla_1, dict(tupla_1))

list_dimensional = [['a',1],['b',2]]

print(list_dimensional, dict(list_dimensional))

empty_dict2 = dict()
print(empty_dict2)

full_dict = dict(
    genero = 'M',
    nacionalidad = 'E'
)
print(full_dict)

empleado = {
    "name": "Valeria",
    "apellido": "Mardones",
    "edad": 32,
     "rut": "13323987-9"
}

print(empleado)
for variablex in empleado.values():
    print(variablex)

for clave, valor in empleado.items():
    print(clave, valor) 

edad = 60
if edad > 50:
    print("Holaaa")
    print("Holaaaa dentro del el if ")

print("print fuera del if")

temperatura = 38
if temperatura >= 37:
    print("Alerta de temperatura alta")
else:
    print("Temperatura es normal")


temperatura = 5
pais = 'Chile'

if temperatura < 10:
    if pais == 'Chile':
        print('cccc')
    else:
        print('zzzz')
else:
    if pais == 'Chile':
        print('1111')   
    else:
        print('2222')   
    

if temperatura < 10:
    print('Es altamente probable que nieve')
elif temperatura >= 10 and temperatura <= 20:
    print('Es medianamente probable que nieva')
else:
    print('No hay posibilidad de nieve')  


persMarvel = 'Spiderman'
volar = False  
humano = True
mascara = True

if volar == True:
    print(persMarvel + ' puede volar')
else:
    print(persMarvel + ' no puede volar')
if humano == True:
    print(persMarvel + ' es humano')
else:
    print(persMarvel + ' no es humano')
if mascara == True:
    print(persMarvel + ' usa mascara')
else:
    print(persMarvel + ' no usa mascara')


want_exit = 'n'
print(want_exit)
num_questions = 0

while want_exit =='n':
    print('Hola como estas?')
    want_exit = input('Quieres salir S/N')
    num_questions += 1
    if num_questions == 4:
        print('Alcanzaste el maximo permitido')
        break

print('Fuera del while')

