from io import open

# el + para decir que puede leer y escribir
archivoDeTexto = open("archivo.txt", "r+")
# metodo seek para posicionar el puntero de lectura
archivoDeTexto.seek(7)
# parametro de read es hasta que punto lee
print(archivoDeTexto.read(11))
archivoDeTexto.seek(0)
# readLines devuelve una lista
lista_texto = archivoDeTexto.readlines()
lista_texto[1] = "Nueva linea insertada desde el programa\n"
archivoDeTexto.writelines(lista_texto)
archivoDeTexto.close()
