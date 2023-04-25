words='Esto es una cadena de texto '
word=''

for letters in words:
    if letters != ' ':
        word += letters
    else:
        print(word)
        word = ' '
   
for letters in words:
    if letters != ' ':
        print(letters)

    else:
        break

wordss = "Otra cadena de texto"

letter = wordss.split()

for letter in letter:

  print(letter)

animals_list = ['perro', 'gato', 'pajaro', 'ardilla']
for animal in animals_list:
    print(animal)

list1 = range(2,3)#[0,1,2,3]
print(list1)
for number_in in range (1, 10):
    print(number_in)
for number_in in range (1, 10,2):
    print(number_in)

for num_tabla in range(1, 11):
    for num_mul in range(1, 11):
        result = num_tabla * num_mul
        print(num_tabla, 'x', num_mul, '=', result)
    print("\n---------------\n")

def saludar (name):
    print('Hola',name,'!!!')

saludar('Claudia')
saludar('Emma')

def saludar_dos(first_name, last_name):
    print('Hola', first_name, last_name, '!!')

saludar_dos('Claudia', 'Rojas')

saludar_dos(last_name = 'Escobar', first_name ='Cristian')

def multiplicar_texto(texto, multiplier = 2):
    print(texto * multiplier)

multiplicar_texto('A', 5)

multiplicar_texto('B')

def varieltal(param1, param2, *others):
    print(param1)
    print(param2)
    print(others)

varieltal('A1', 'A2', 0, 'xxx', [ 0, 2])


def varieltal_dos(param1, **others):
    print(param1)
    print(others)

varieltal_dos('A1', id = 0, name = 'Carlos')

