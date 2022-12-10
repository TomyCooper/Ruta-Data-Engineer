# Para comprimir un archivo en formato TAR
tar -cvf [nombre archivo].tar [dir documento]

	c 	:create
	v 	:verbose : vervosely list files processed
	f 	:files (regular file)

# Formato GZIP
tar -cvzf [nombre archivo].tar.gz [dir documento]

	c 	:create
	v 	:verbose : vervosely list files processed
	f 	:files (regular file)
    z   :agrega formato GZIP

# Para descomprimir un GZIP
tar -xzvf [nombre archivo].tar.gz

	x 	:extract
    z   :GZIP
	v 	:verbose : vervosely list files processed
	f 	:files (regular file)

# Formato ZIP
zip -r ToCompressInZip.zip ToCompress

    r   :recursive

# Para descomprimir un ZIP
unzip ToCompressInZip.zip