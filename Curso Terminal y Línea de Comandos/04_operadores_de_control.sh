# Los operadores de control me permite ejecutar comandos
# sincronos, asincronos, condicionados y no condicionados.

# Sincronos: los ejecuta uno después del otro.
ls; mkdir nuevo_directorio; cal

# Asincronos: los ejecuta todos al tiempo.
ls & date & cal

# Condicionados: El comando2 se ejecuta si y solo si el comando1 fue exitoso.
ls && cal #Exitoso: sí se ejecuta cal
ls mkdcsk && #NoExitoso: no se ejecuta cal

# NoCondicionados: Ejecuta el comando1 o el comando2.
echo "comando1" || echo "comando2"