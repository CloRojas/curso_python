class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

gato = Animal('Angora', 'Persa')
print(gato.type)
gato.type = 'Siames'
print(gato.type)

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

usuario1 = Usuario('esarab', '11111')
print(usuario1.password)
usuario1.password = '233223'
print(usuario1.password)


class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self) -> str:
        return self.hidden_name

    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name

android = Droid('R2')

print(android.name)
android.name = 'C3PO'
print(android.name)

android.hidden_name = 'Red'
print(android.hidden_name)
print(android.name)

class CalculatedValue:
    def __init__(self, name, _height):
        self.name = name
        self.height = _height

    @property
    def get_calculate_value(self) -> float:
        return 0.35 * self.height

valuex = CalculatedValue('ratio', 10)

print('el', valuex.name, 'es:', valuex.get_calculate_value)

class Dog:
    obeys_owner = True

    def __init__(self, _name):
        self.name = _name

dog_one = Dog('Lulu')
dog_two = Dog('Cuca')
dog_three = Dog('Emma')

print(dog_one.name, 'obedece a su dueño', dog_one.obeys_owner)
print(dog_two.name, 'obedece a su dueño', dog_two.obeys_owner)
print(dog_three.name, 'obedece a su dueño', dog_three.obeys_owner)

dog_one.obeys_owner = True
print(dog_one.name, 'obedece a su dueño', dog_one.obeys_owner)
print(dog_two.name, 'obedece a su dueño', dog_two.obeys_owner)
print(dog_three.name, 'obedece a su dueño', dog_three.obeys_owner)

Dog.obeys_owner = False
print(dog_one.name, 'obedece a su dueño', dog_one.obeys_owner)
print(dog_two.name, 'obedece a su dueño', dog_two.obeys_owner)
print(dog_three.name, 'obedece a su dueño', dog_three.obeys_owner)











