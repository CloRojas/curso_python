class Artefacto:
    def __init__(self, name, form, color):
        self.__name = name
        self.__form = form
        self.color = color

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self,name: str) -> None:
        self.__name = name

    @property
    def form(self) -> str:
        return self.__form

    @form.setter
    def form(self,form: str) -> None:
        self.__form = form

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self,color: str) -> None:
        self.__color = color


artefacto1 = Artefacto('casa','cuadrada', 'verde')

print(artefacto1.name)
print(artefacto1.form)
print(artefacto1.color)

class Empleado:
    sueldo_base = 100.000

    def __init__(self, _name):
        self.__name = _name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,_name):
        self.__name = _name

    @classmethod
    def get_sueldo_base(cls):
        return cls.sueldo_base

    @classmethod
    def set_sueldo_base(cls, _sueldo):
        cls.sueldo_base = _sueldo
