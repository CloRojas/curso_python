import datetime

class Cine:
    def __init__(self, _name_cine, _rut_cine, _address_cine):
        self._name_cine = _name_cine
        self._rut_cine = _rut_cine
        self._address_cine = _address_cine
        self.salas = []
        self.cartelera = []
      
    
    def crearSala(self, _num_sala, _letra_fila_sala, _num_columna_sala, _category_sala):
        sala = Sala(  _num_sala, _letra_fila_sala, _num_columna_sala, _category_sala)
        self.salas.append(sala)
        return sala

class Asiento:
    def __init__(self, letra_fila, num_columna):
        self.letra_fila = letra_fila
        self.num_columna = num_columna
        self.vendido = False


class Sala:
    def __init__(self, _num_sala, _letra_fila_sala, _num_columna_sala, _category_sala):
        self._num_sala = _num_sala
        self._letra_fila_sala = _letra_fila_sala
        self._num_columna_sala = _num_columna_sala
        self._category_sala = _category_sala
        self._capacity_sala = self.asignarAsientos()

    def asignarAsientos(self):
        _capacity_sala = []
        for letra_fila in self._letra_fila_sala:
            for numero_columna in range(1, self._num_columna_sala + 1):
                asiento = Asiento(letra_fila, numero_columna)
                _capacity_sala.append(asiento)
        return _capacity_sala

    def obtenerPosicionAsientos(self):
        posiciones_asientos = []
        for asiento in self._capacity_sala:
            posicion_asiento = (asiento.letra_fila, asiento.num_columna)
            posiciones_asientos.append(posicion_asiento)
        return posiciones_asientos

    def obtenerCapacidad(self):
        return len(self._capacity_sala)



class Funcion:
    def __init__(self, pelicula, horario, duracion_pelicula, sala, cine, dia, _id):
        self.pelicula = pelicula
        self.horario = horario
        self.duracion_pelicula = duracion_pelicula
        self.sala = sala
        self.cine = cine
        self.dia = dia
        self._id = _id
        self.entradas_vendidas = 0
        self.tickets_vendidos = []

    def obtenerAsientosOcupados(self):
        asientos_ocupados = []
        for ticket in self.tickets_vendidos:
            asientos_ocupados.append(ticket.asiento)
        return asientos_ocupados

    def venderTicket(self):
        capacidad_sala = self.sala.obtenerCapacidad()
        asientos_ocupados = self.obtenerAsientosOcupados()

        if len(asientos_ocupados) >= capacidad_sala:
            print("No hay asientos disponibles para esta función.")
            return

        letra_fila = input("Ingrese la letra de la fila del asiento: ")
        num_columna = input("Ingrese el número de la columna del asiento: ")

        asiento = Asiento(letra_fila, num_columna)
        if asiento in asientos_ocupados:
            print("El asiento seleccionado ya está ocupado.")
            return

        ticket = Ticket(self, asiento)
        self.tickets_vendidos.append(ticket)
        self.incrementarEntradasVendidas()
        print("Ticket vendido exitosamente.")

    def incrementarEntradasVendidas(self):
        self.entradas_vendidas += 1

    def obtenerHorariosDisponibles(self, fecha):
        horarios_disponibles = []
        for funcion in self.cine.cartelera[fecha][self.sala]:
            horarios_disponibles.append(funcion.horario)
        return horarios_disponibles

class Pelicula:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion
    
class Cartelera:
    def __init__(self, cine):
        self.cine = cine
        self.funciones = {}
        self.calendario = {}

    def agregarFuncion(self, funcion):
        dia = funcion.dia

        if dia not in self.calendario:
            self.calendario[dia] = {}

        sala = funcion.sala
        if sala not in self.calendario[dia]:
            self.calendario[dia][sala] = []

        self.calendario[dia][sala].append(funcion)

    def obtenerCapacidadSala(self, sala):
        capacidad_sala = 0
        if sala in self.calendario:
            for dia in self.calendario:
                if sala in self.calendario[dia]:
                    capacidad_sala = sala.obtenerCapacidad()
                    break
        return capacidad_sala

    def obtenerAsientosOcupados(self, funcion):
        asientos_ocupados = []
        if funcion.dia in self.calendario and funcion.sala in self.calendario[funcion.dia]:
            funciones_sala = self.calendario[funcion.dia][funcion.sala]
            for funcion_sala in funciones_sala:
                asientos_ocupados.extend(funcion_sala.obtenerAsientosOcupados())
        return asientos_ocupados

class Ticket:
    def __init__(self, funcion, asiento):
        self.funcion = funcion
        self.asiento = asiento
        self.precio = self.getPrice()

    def getPrice(self):
        if self.funcion.sala._category_sala == 'vip':
            return 10.0  # Precio para sala VIP
        else:
            return 5.0

class Boleteria:
    def __init__(self, name, cine):
        self.cine = cine
        self.name = name

    # def mostrarFuncionesPorDia(self, dia):
    #     funciones = self.cine.cartelera.calendario.get(dia, {})
    #     for sala in funciones:
    #         funciones_sala = funciones[sala]
    #         for funcion in funciones_sala:
    #             print("ID:", funcion._id)
    #             print("Pelicula:", funcion.pelicula.titulo)
    #             print("Horario:", funcion.horario)
    #             print("Cantidad de tickets disponibles:", self.obtenerCantidadTicketsDisponibles(funcion))
    #             print("---------------------------------")


    # def obtenerCantidadTicketsDisponibles(self, funcion):
    #     capacidad_sala = self.cine.cartelera.obtenerCapacidadSala(funcion.sala)
    #     asientos_ocupados = self.cine.cartelera.obtenerAsientosOcupados(funcion)
    #     tickets_disponibles = capacidad_sala - len(asientos_ocupados)
    #     return tickets_disponibles

    def venderTicket(self, funcion):
        cantidad_tickets_disponibles = self.obtenerCantidadTicketsDisponibles(funcion)
        if cantidad_tickets_disponibles > 0:
            letra_fila = input("Ingrese la letra de la fila del asiento: ")
            num_columna = input("Ingrese el número de la columna del asiento: ")

            asiento = Asiento(letra_fila, num_columna)
            asientos_ocupados = self.cine.cartelera.obtenerAsientosOcupados(funcion)
            if asiento in asientos_ocupados:
                print("El asiento seleccionado ya está ocupado.")
                return

            ticket = Ticket(funcion, asiento)
            self.cine.registrarVentaTicket(ticket)
            print("Ticket vendido exitosamente.")
        else:
            print("No hay tickets disponibles para esta función.")

_dia = datetime.datetime(2023, 5, 21)


# Creación del cine y la boletería
cine1 = Cine('CinemaDo', '75444343-9', 'Los Alamos #454, Santiago')
boleteria1 = Boleteria('Boleteria 1', cine1)

# Creación de salas
num_sala = 1
letras_filas_sala1 = ['A', 'B', 'C', 'D', 'E']
num_columnas_sala1 = 5
_category_sala1 = 'vip'
sala1 = cine1.crearSala(num_sala, letras_filas_sala1, num_columnas_sala1, _category_sala1)
print(sala1.obtenerCapacidad())

num_sala = 2
letras_filas_sala2 = ['A', 'B', 'C', 'D']
num_columnas_sala2 = 4
_category_sala2 = 'normal'
sala2 = cine1.crearSala(num_sala, letras_filas_sala2, num_columnas_sala2, _category_sala2)

# Creación de una película
pelicula1 = Pelicula('Las aventuras de Poly', '95')

# Creación de una función
funcion1 = Funcion(pelicula1, '17:00', pelicula1.duracion, sala2, cine1, _dia, 1)

# Creación de la cartelera y agregado de la función
cartelera1 = Cartelera(cine1)
cartelera1.agregarFuncion(funcion1)

# Mostrar funciones disponibles para un día específico
#boleteria1.mostrarFuncionesPorDia(_dia)
