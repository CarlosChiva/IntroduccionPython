import re

nombre1 = 'Jara Lopez'
nombre2 = 'Antonio Gomez'
nombre3 = 'Lara Lopez'
# match devuelbe booleano y busca al inicio de una cadena de texto
# re.ignorecase es para que no haga distincion de mayusculas
# el . pede ser un caracter sin determinar
if re.match(".ara", nombre3, re.IGNORECASE):
    print("Nombre encontrado")
else:
    print("no lo hemos encontrado")

cadena1 = 'Jara Lopez'
cadena2 = '5648973'
cadena3 = 'a563543'
# simbolo \d para expresar digito y busca
if re.match("\d", cadena2):
    print("Numero encontrado")
else:
    print("no lo hemos encontrado")

# Search busca en toda la cadena de texto
cadena1 = 'Jara Lopez'
cadena2 = 'Antonio Gomez'
cadena3 = 'Lara Lopez'

if re.search("Lopez", cadena1, re.IGNORECASE):
    print("Nomre encontrado")
else:
    print("no lo hemos encontrado")
