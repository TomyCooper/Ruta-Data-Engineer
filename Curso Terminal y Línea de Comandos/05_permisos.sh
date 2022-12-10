# Los archivos y directorios tienen permisos individuales.
# Estos permisos tienen una convención.
# r:read     w:write    x:execute

# Para poder modificar los permisos de los archivos usaremos chmod.
chmod 755 #Usando el modo octal.

# Cambiar al usuario root.
su root
# Pedirá pass que es la misma del PC.

# Puedo cambiar permisos al usuario u, grupos o, otros o sobre un archivo.
chmod u=rwx,g=rw,o=x archivo.txt



