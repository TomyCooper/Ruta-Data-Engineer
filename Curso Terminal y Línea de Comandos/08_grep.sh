# grep me permite encontrar coincidencias de texto dentro de archivos.

# Quiero encontrar todas las coincidencias que contengan la palabra the
grep the movies.csv

# OJO! El grep es Case Sensitive. Para solucionarlo si agregar -i
grep -i the movies.csv

# Para contar el número de coincidencias uso -c
grep -c the movies.csv

# Para encontrar las anti-coincidencias uso -v
grep -v Towers movies.csv

# Bonus: comando wc cuenta las líneas, palabras y letras/caracteres
wc movies.csv
# Para contar el número de líneas, palabras, caracteres
wc -l movies.csv
wc -w movies.csv
wc -c movies.csv