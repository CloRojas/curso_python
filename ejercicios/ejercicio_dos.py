# Utilizando dos while anidados, construya la tablas de multiplicación,                                    
# Ejemplo while anidados:
# while codicion1
# 		while codicion2
# 			.....

print('Tabla de multiplicacion  del numero ingresado ')

while True:
    try:
        tabla = int (input('Ingresa la tabla que quieres ver: '))
    except ValueError:
        print("Debes ingresar un valor numerico")
        continue
    if tabla <= 0:
        print("Debe ser un numero mayor a 0")
        continue
    else:
        break


while tabla:
    print("Tabla del", tabla)
    multiplicador = 1
    while multiplicador <= 10:
        resultado = tabla * multiplicador
        print(tabla , 'x' , multiplicador , '=' , resultado)
        multiplicador += 1
    break
  