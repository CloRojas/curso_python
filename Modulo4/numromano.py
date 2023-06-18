##Escribe una clase en python que convierta un número entero a número romano

class NoEscribirCeroException(Exception):
    def __init__(self, _message):
        self._message = _message


class ConvierteNum:
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    def __init__(self, num):
         self.num = num

    def convertir_a_romano(self, num):

        resultado = ""
        i = 0
        while self.num > 0:
            if self.num >= self.valores[i]:
                resultado += self.simbolos[i]
                self.num -= self.valores[i]
            else:
                i += 1
        print(resultado)


try:
    numingresado= int(input('Ingresa un número entero'))
    romano = ConvierteNum(numingresado)
    if (numingresado == 0):
        raise NoEscribirCeroException ('Número 0 no es válido')
    else:
        romano.convertir_a_romano(numingresado)
except ValueError : 
    print('Número no válido')
except Exception as error:
    print(error.args)