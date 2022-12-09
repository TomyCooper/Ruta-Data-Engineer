# Quiero listar (ls) todos los archivos que terminen en .txt.
ls *.txt

# Quiero listar todos los archivos que empiecen con datos
ls datos*

# Quiero todos los archivos que empiecen con "datos" y tengan un caracter más.
ls datos?

# Quiero todos los archivos que empiecen con "datos" y tengan tres caracteres más.
ls datos???

# Aquí me ayudo de expresiones regulares. Quiero todos los archivos que empiecen con mayúscula.
ls [[:upper:]]*
# Si solo quiero directorios agrego la flag -d.
ls -d [[:upper:]]*

# Todos los que empiecen con a o d.
ls [ad]*