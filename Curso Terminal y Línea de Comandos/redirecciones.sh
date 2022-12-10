# Las redirecciones me permiten almacenar el stout (standard output) o el standard error en un archivo de texto.

# Almaceno todos los nombres de los archivos dentro de la carpeta Pictures en un archivo 
ls Pictures > misarchivos.txt

# OJO! Si solo uso > sobreescribe el archivo.
# Para concatenar uso >>
ls Pictures > misarchivos.txt
ls Downloads >> misarchivos.txt

# Si quiero almacenar el resultado del standard output, lo hago normal con >
ls njdhbcf > errors.txt

# Pero si quiero almacenar el standard error, uso 2>
ls fknbvhw 2> errors.txt

# Si quiero almacenar ambos
ls mfnfdonj >> output.txt 2>&1