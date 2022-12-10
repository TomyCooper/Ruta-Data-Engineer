# Dónde se encuentra un comando o archivo
which ls

# Dónde se encuentra un archivo.
find ./ -name archivo.txt
# Recibe la ruta desde donde empieza a buscar.

# También podemos buscar archivo o directorios con -type
find ./ -type d f nombre-archivo-directorio

# Encontrar por al menos un tamaño de archivo
find ./ -size 20M