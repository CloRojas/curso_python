class Animal:
    def __init__(self, _nombre, _raza, _edad, _peso):
        self._nombre = _nombre
        self._raza = _raza
        self._edad = _edad
        self._peso = _peso
    
    def comer(self):
        print('Estoy comiendo')
    
    def caminar(self):
        print('Estoy caminando')
    
    def dormir(self):
        print('Estoy durmiendo')

perro = Animal('Brando', 'San Bernardo', '3 años', '30 kilos')

gato = Animal('Roll', 'persa', '4 años', '3 kilos')


