from io import open

# w es por escritura
archivo_Texto = open("archivo.txt", "w")
frase = "el filewriter\n jejeje"
archivo_Texto.write(frase)
archivo_Texto.close()
# r de read
archivo_Texto = open("archivo.txt", "r")
texto = archivo_Texto.read()
archivo_Texto.close()
print(texto)
# a de append
archivo_Texto = open("archivo.txt", "a")
archivo_Texto.write("\n texto adjunto")
archivo_Texto.close()
