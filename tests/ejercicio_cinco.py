#5. Escriba un programa que eliminar un signo de exclamación del final de una cadena, 
#puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.

cadena = 'Qué hermoso día!'
print('Eliminaremos el signo de exclamación final en la siguiente oración: ')
print(cadena)

signo = cadena.replace('!', '')

print('Ahora sin signo de exclamación final: ', signo)