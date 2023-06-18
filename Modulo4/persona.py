class Persona:
    def __init__(self, _edad, _genero, _nacionalidad)
        self._edad = _edad
        self._genero =_genero
        self._nacionalidad = _nacionalidad

class Maestro(Persona):
    def __init__(self, _edad, _genero, _nacionalidad, _titulo)
        super().__init__(self, _edad, _genero, _nacionalidad)
        self._titulo = _titulo

class Estudiante(Persona):
    def __init__(self, _edad, _genero, _nacionalidad, _lugar_estudio)
        super().__init__(self, _edad, _genero, _nacionalidad)
        self._lugar_estudio = _lugar_estudio

class Universitario(Estudiante):
    def __init__(self, _edad, _genero, _nacionalidad, _lugar_estudio, _carrera)
        super().__init__(self, _edad, _genero, _nacionalidad, _lugar_estudio)
        self._carrera = _carrera





