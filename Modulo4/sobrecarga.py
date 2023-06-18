class Propiedades:
    estado = 'nuevo'
    def __init__(self, _tipo):
        self.tipo = _tipo

    def vender(self):
        print(self.estado)

    def vender(self, _reserva =''):
        estado1 = self.estado
        if ( _reserva != ''):
            estado1 = self.estado, 'con', _reserva
        print(estado1)

    def vender (self, _reserva ='', _fecha = ''):
        estado2 = self.estado
        if (_reserva != '' and _fecha == ''):
            estado2 = self.estado, 'con', _reserva
        if (_reserva != '' and _fecha != ''):
              estado2 = self.estado, 'con', _reserva, 'el día', self._fecha
        print(estado2)

departamento1 = Propiedades('A52')

departamento1.vender('reservado', '05/08/2022')
            