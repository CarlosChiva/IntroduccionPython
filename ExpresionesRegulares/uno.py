import re

cadena = "Expresiones regulares level 1 para empezar para toquetearlo todo"
# primer parametro la cadena a buscar y segundo parametro la variable a la que buscar
print(re.search("level", cadena))
# aparecera none si no encuentra nada
print(re.search("Esparragos", cadena))
textoABuscar = "regulares"
if re.search(textoABuscar, cadena) is not None:
    print("cadena encontrada en el texto")
else:
    print("cad3ena no encontrado")

# tambien se puede almacenar
textoEncontrado = re.search(textoABuscar, cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
#guarda en tupla
print(textoEncontrado.span())

# encontrar todos los caracteres descritos si se repiten
testo_aEncontrar="para"
print(re.findall(testo_aEncontrar,cadena))
print(len(re.findall(testo_aEncontrar,cadena)))

