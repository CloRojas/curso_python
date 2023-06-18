class NoEscribirDosException(Exception):
    def __init__(self, _message):
        self._message = _message

try:
    number = input('Ingresa un número')
    if (number == '2'):
        raise NoEscribirDosException('Número 2 no es válido')
    else:
        print('Número válido')
except Exception as error:
    print(type(error))
    print(error.args)
