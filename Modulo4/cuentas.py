class Cuenta:
    def __init__(self,_titular, _cantidad):
        self._titular = _titular
        self._cantidad = _cantidad
    
    def imprimir_datos(self):
        print('El titular de la cuenta es ', self._titular, ' el monto en su cuenta es ', self._cantidad)

class Plazo_fijo(Cuenta):
    def __init__(self,_titular, _cantidad, _plazo, _interes):
        super().__init__( _titular, _cantidad) 
        self._plazo = _plazo
        self.interes = _interes

    def obtener_importe(self):   
        importe_interes = (self._cantidad *(self.interes/100))*self._plazo
        return importe_interes
    
    def obtener_datos(self):
        importe_interes = self.obtener_importe()
        print('El titular ', self._titular, 'tiene', self._cantidad, 'a un plazo de', self._plazo, ' con un interés de', self._interes, ', obtiene', importe_interes)
       

class Caja_ahorro(Cuenta):
    def __init__(self,_titular, _cantidad):
        super().__init__(_titular, _cantidad) 


cta1 = Cuenta('Marcela Mora', 3000)
cta2 = Plazo_fijo('Luisa Rojas', 5000, 2, 1.5)
cta3 = Caja_ahorro('Felipe Santos', 4000)

cta2.obtener_datos()