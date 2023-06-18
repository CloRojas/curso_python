class Taza:    
    sizes = {
        'small': 'pequeño',
        'medium': 'mediano',
        'large': 'grande'
    }
    def __init__(self):
        self.size = self.sizes['small']

class Maquina:
    tipo_cafe = {
        ''
    }
    def __init__(self, _tipo_cafe, _cantidad_agua, _cantidad_cafe):
        self._tipo_cafe = _tipo_cafe
        self._cantidad_agua = _cantidad_agua
        self._cantidad_cafe = _cantidad_cafe


class Cafe:
    pass

class Leche:
    pass