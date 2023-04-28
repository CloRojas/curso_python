class Motocicleta:
    is_new = True
    motor = False

    def __init__(self, color, matricula, combustible_litro, num_ruedas, marca, modelo, fecha_fab, vel_punta, peso, cap_max):
        self.color = color
        self.matricula = matricula
        self.combustible_litro = combustible_litro
        self.num_ruedas = num_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fab = fecha_fab
        self.vel_punta = vel_punta
        self.peso = peso
        self.cap_max = cap_max

    def arrancar(self):
        if self.motor:
            print('El motor ya estaba arrancado')
        else:
            print('El motor ha arrancado')

    def detener(self):
        if self.motor:
            print('El motor se ha detenido')
        else: 
            print('El motor ya estaba detenido')
    
    def consultar_precio(self):
        print('El precio de la motocicleta', self.marca, self.modelo,  'es', self.precio)
    
    def reporte_combustible(self):
        print('Reporte del depósito de motocicleta', self.marca, ' modelo', self.modelo)
        print('Litros de combustible disponible:', self.combustible_litro)
        print('Capacidad máxima de tanque:', self.cap_max)
        print('Faltan', self.cap_max - self.combustible_litro, 'para llenar el tanque')

    def cargar_combustible(self):
        self.carga_combustible = float(input('¿Cuantos litros de combustible desea cargar?'))
        if self.carga_combustible + self.combustible_litro <= self.cap_max:
            self.combustible_litro = self.combustible_litro + self.carga_combustible
            print(' Carga realizada, el tanque ahora tiene', self.combustible_litro, 'litros')
        else:
            print('Supera la capacidad máxima del tanque')

 



moto1 = Motocicleta('negro', 'XX57', 10, 2, 'Honda', 'city', '01/03/2022', 150, 100, 20)
print(moto1.color)

moto2 = Motocicleta(
    matricula = 'HH33',
    peso = 150,
    vel_punta = 220,
    combustible_litro = 0,
    num_ruedas = 2,
    marca = 'Kawasaky',
    fecha_fab = '12/12/2023',
    modelo = 'Vesta',
    cap_max = 17,
    color = 'azul'
    
    )
print(moto2.matricula)

moto1.arrancar()
moto1.detener()

moto1.precio = 10000
moto1.consultar_precio()
moto1.reporte_combustible()
moto1.cargar_combustible()


print('El precio de la motocicleta', moto1.marca, moto1.modelo,  'es', moto1.precio)




