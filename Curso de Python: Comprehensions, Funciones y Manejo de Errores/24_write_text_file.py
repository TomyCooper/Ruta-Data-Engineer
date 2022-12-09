with open('/Users/tomycooper/Documents/Ruta Data Engineer/Curso de Python: Comprehensions, Funciones y Manejo de Errores/text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nNuevas cosas en esta linea\n')
    file.write('Otra linea\n')
    file.write('Otra linea mas\n')
    file.write('Nueva linea final')