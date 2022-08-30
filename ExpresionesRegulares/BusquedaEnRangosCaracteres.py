import re

lista_de_nombres = ['Ana',
                    'Pedro',
                    'Maria',
                    'Celia']
# el guion entre [] simboliza rango, hace distincion entre mayusculas y minusculas
for elmento in lista_de_nombres:
    if re.findall('[o-t]', elmento):
        print(elmento, 'estan entre rangos o y t')

lista_de_Ciudades = ['Madri1',
                     'Sevil1',
                     'Madri2',
                     'Barcel1',
                     'Madri3',
                     'Val1',
                     'Madri4']
for ciudad in lista_de_Ciudades:
    if re.findall('Madri[1-4]', ciudad):
        print(ciudad)

# si se escribe [^ x-y] el acento define el que no cumpla el rango

for norango in lista_de_Ciudades:
    if re.findall('Madri[^1-2]', norango):
        print(norango, " no estan en el rango 1-2")

lista_de_Ciudades2 = ['Ma1',
                      'Sev1',
                      'Ma2',
                      'Bar1',
                      'Ma3',
                      'Val1',
                      'Ma4',
                      'MaA',
                      'MaC',
                      'MaB']

for biRango in lista_de_Ciudades2:
    if re.findall('Ma[0-3A-B]', biRango):
        print(biRango, " estan en los rangos especificados")
