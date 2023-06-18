nombres = [['Harry Houdini', 'David Blaine', 'Teller'], ['Newton', 'Hawking', 'Einstein'], ['Messi', 'Pele', 'Juanes']]

magos = nombres[0]
cientificos = nombres[1]
otros = nombres[2]

def hacer_grandioso(lista):
    for i in range(len(lista)):
        lista[i] = 'El gran ' + lista[i]
    
def imprimir_nombres(lista):
    for i in range(len(lista)):
        print(lista[i])


print('La lista completa:', nombres)

hacer_grandioso(magos)
print('Los magos grandiosos son:')
imprimir_nombres(magos)
print('Los científicos son:')
imprimir_nombres(cientificos)
print('Los otros son:')
imprimir_nombres(otros)

    
