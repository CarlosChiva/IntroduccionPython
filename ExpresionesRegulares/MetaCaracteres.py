import re

listaNombres = ['Ana Gomez', 'Maria Martin', 'Sandra Lopez', 'Santiago Martin']
for elemento in listaNombres:
    # el simbolo ^ para delimitar que la cadena comienza por los caracteres escritos posteriormente al simbolo
    if re.findall('^Sandra', elemento):
        print(elemento, "comineza por Sandra")
    # el simbolo $ se utiliza para marcar que la linea de caracteres termina con la cadena descrita antes del simbolo
    elif re.findall('Martin$', elemento):
        print(elemento, "Termina en Martin")

lista_de_dominios = ['http://mimismo.com',
                     'http://mimismo.es',
                     'ftp://mimismo.com',
                     'ftp://mimismo.es']
for elmento in lista_de_dominios:
    if re.findall('^ftp', elmento):
        print(elmento, 'Comienza por ftp')


lista_de_dominios2 = ['http://mimismoñe.com',
                     'http://mimismone.es',
                     'ftp://mimismoñe.com',
                     'ftp://mimismo.es']
# simbolo de busqueda [] para buscar los caracteres de su interior, independientemente del orden, solo que existan
for elment in lista_de_dominios2:
    if re.findall('[ñ]', elment):
        print(elment, 'Contiene la ñ')

lista_de_nombres = ['hombres',
                      'mujeres',
                      'niños',
                      'niñes']

for elment2 in lista_de_nombres:
    if re.findall('niñ[oe]s', elment2):
        print(elment2, 'Contiene la ñ')

lista_de_cosas = ['hombres',
                    'mujeres',
                    'camión',
                    'camion']

for elment3 in lista_de_cosas:
    if re.findall('cami[oó]n', elment3):
        print(elment3, 'Contiene camion de distintas formas')
