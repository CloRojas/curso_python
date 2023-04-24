print('Calcular el maximo comun divisor entre dos numeros enteros ')

while True:
    try:
        num1 = int (input('Ingresa el primer numero: '))
        num2 = int (input('Ingresa el segundo numero: '))
    except ValueError:
        print("Debes ingresar un numero entero")
        continue
    else:
        break
#Algoritmo de Euclides
def mcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

resultado = mcd(num1, num2)

print("El maximo comun divisor de", num1, "y", num2, "es:", resultado)

