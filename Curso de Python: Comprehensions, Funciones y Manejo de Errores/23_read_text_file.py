file = open('/Users/tomycooper/Documents/Ruta Data Engineer/Curso de Python: Comprehensions, Funciones y Manejo de Errores/text.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close() #OJO! Importante cerrar el archivo para liberar espacio en memoria.

# La mejor manera de abrir archivos es con el with open.
# Pues cierra el archivo y libera espacio en memoria de manera automática.
with open('/Users/tomycooper/Documents/Ruta Data Engineer/Curso de Python: Comprehensions, Funciones y Manejo de Errores/text.txt') as file:
  for line in file:
    print(line)