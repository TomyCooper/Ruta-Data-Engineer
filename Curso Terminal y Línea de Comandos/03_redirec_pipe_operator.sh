# El Pipe Operator me permite redirigir el output de un comando hacia el input de otro.
comando1 | comando2

# El listado se ordena, luego se guarda en un archivo y al final lo veo con less.
ls -lh Pictures | sort | tee pictures.txt | less

# Algunos comandos chistosos.
cowsay "Hola amigos!" | lolcat