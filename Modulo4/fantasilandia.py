class Alumno:
    #variable de clase
    semestre = 1
    notas = [_nota1, _nota2, nota_3]

    def __init__(self, _name):
        #variable de instancia
        self.name = _name

    def inscribir_asignatura(self, _asignatura):
        self._asignatura = _asignatura

    def registrar_notas (self, notas):
        self._nota1 = _nota1
        self._nota2 = _nota2
        self._nota3 = _nota3

    def promedio_notas (self, _nota1, _nota2, nota3):
        self._nota1 = _nota1
        self._nota2 = _nota2
        self._nota3 = _nota3



    

alumno1 = Alumno('Marysabel')
alumno2 = Alumno('Majo')
alumno3 = Alumno('Marife')

print('alumno1:', alumno1.name, 'alumno2:', alumno2.name, 'alumno3:', alumno3.name)
print('semestre alumno1:', alumno1.semestre, 'semestre alumno2:', alumno2.semestre, 'semestre alumno3:', alumno3.semestre)

alumno2.semestre = 2

print('semestre alumno1:', alumno1.semestre, 'semestre alumno2:', alumno2.semestre, 'semestre alumno3:', alumno3.semestre)

Alumno.semestre = 3

print('semestre alumno1:', alumno1.semestre, 'semestre alumno2:', alumno2.semestre, 'semestre alumno3:', alumno3.semestre)

alumno1.inscribir_asignatura('química')

print(alumno1._asignatura)