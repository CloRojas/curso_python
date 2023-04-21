print("Hello world")
edad = 40
sueldo = 5000.3
name = "Claudia"
surname ="Rojas"
isTeacher = False

print(edad, sueldo, name + " " + surname, isTeacher)

numero1 = 4
numero2 = 7
resultado = (numero1 + numero2) / 3
print(resultado)

mensaje1 = "Hola " * 3
print(mensaje1)

mensaje2= "manzanas"

mensaje2 += ","
print(mensaje2)

print(len(mensaje2))

cadena ="love will tear us apart again"
posicion = cadena.find("tear")

print(posicion)

nombre = "Claudia".lower()

print(nombre)

aes = "aaaaaa"

nueva = aes.replace ("a","b", 3)

print(nueva)


empty_list =[]
print(empty_list)

fullfiled_list = [1, 3, 500, 1.4, [2, "a"], {name: "Claudia"}, (1, 3, 5)]
print(fullfiled_list)



print(list("Concurso"))

range_one = range(50)
print(list(range_one))

numeros = [1, 4, 6]
print(numeros)
numeros.append(10)
print(numeros)

print(numeros[2])

for x in numeros:
 print(x)

eliminado = numeros.pop(0)

print(eliminado)

empty_tuple = ()

fullfiled_tuple= (1, "a", 90)

print(empty_tuple, fullfiled_tuple)

print(type(fullfiled_tuple))

one_tuple = ('claudia',)
print(type(one_tuple))

hojas = 'carta', 'oficio'
print(type(hojas))
print(hojas)

empty_tuple_2 = tuple()
print(empty_tuple_2)

list_to_convert = [2, 6, 8, 9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)


tuple3 = (2, 4, 6)
result = reversed(tuple3)
result = tuple(result)
print(result)

s=(2,5,8)
s_append = s + (8, 16, 67)
print(s_append)
print(s)



