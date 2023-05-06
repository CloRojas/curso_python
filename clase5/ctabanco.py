from datetime import datetime

class Banco:
    def __init__(self):     
        self._cuentas = {}
        
    def crear_cuenta(self):
        while True:
            try:
                self.rut = int (input('Ingrese el numero de rut:'))
                self.nro_cta = int (input('Ingrese el número de cuenta: '))
                break
            except ValueError:
                print("Solo debes ingresar números")

        cuenta = {
            'rut' : self.rut,
            'saldo' : 0,
            'movimientos' : {}
        }
        self._cuentas[self.nro_cta] = cuenta
        print("Cuenta", self.nro_cta, "registrada correctamente.")

    def abonar_cta(self):
        while True:
            try:
                self.nro_cta = int (input('Ingrese el número de cuenta: '))
                self.abono = float (input('Ingrese el monto:'))
                break
            except ValueError:
                print("Solo debes ingresar números, separar decimales utiliza punto")

        if self.nro_cta in self._cuentas:
            cuenta = self._cuentas[self.nro_cta]
            cuenta['saldo'] += self.abono
            cuenta['movimientos'] = ('abono', self.abono)
            print('Abono realizado correctamente. Nuevo saldo:', cuenta['saldo'])
        else:
            print('No se encontró la cuenta.')
        
    def cargar_cta(self):
        while True:
            try:
                self.nro_cta = int (input('Ingrese el número de cuenta: '))
                self.cargo = float (input('Ingrese el monto:'))
                break
            except ValueError:
                print("Solo debes ingresar números, separar decimales utiliza punto")

        if self.nro_cta in self._cuentas:
            cuenta = self._cuentas[self.nro_cta]
            cuenta['saldo'] -= self.cargo
            cuenta['movimientos'] = ('cargo', self.cargo)
            print('Cargo realizado correctamente. Nuevo saldo:', cuenta['saldo'])
        else:
            print('No se encontró la cuenta.')

    def pedir_estadocta(self):
        while True:
            try:
                self.nro_cta = int(input('Ingrese el número de cuenta: '))
        
                break
            except ValueError:
                print("Solo debes ingresar números")

        if self.nro_cta in self._cuentas:
            cuenta = self._cuentas[self.nro_cta]
            print(cuenta)



banco = Banco()
banco.crear_cuenta()
banco.abonar_cta()
banco.cargar_cta()
banco.pedir_estadocta()





