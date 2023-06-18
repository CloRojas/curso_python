class Vehiculo:
    def __init__(self, _color, _ruedas, _tipo_freno):
        self.color = _color
        self.ruedas = _ruedas
        self.tipo_freno = _tipo_freno

    def frenar(self):
        print('He frenado')

class Auto(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido):
        super().__init__(self, _color, _ruedas, _tipo_freno)       
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido

class Moto(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido, _tipo_cadena):
        super().__init__(self, _color, _ruedas, _tipo_freno)       
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido
        self._tipo_cadena = _tipo_cadena

class Bicicleta(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_manubrio):
        super().__init__( _color, _ruedas, _tipo_freno)       
        self.tipo_manubrio = _tipo_manubrio
        

mbike = Bicicleta('fucsia', 2, 'torpedo','recto', )

mbike.frenar()