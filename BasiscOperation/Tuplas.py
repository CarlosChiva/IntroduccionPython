tupla = ("elemento1", 25, "elemento3")
# Acceder a elemento
print(tupla[0])
# tupla en lista
lista = list(tupla)
print(lista)
# lista en tupla
nuevatupla = tuple(lista)
print(nuevatupla)
# cuantas veces aparece un objeto
print(tupla.count("elemento1"))
# longitud de tupla y lista
print(len(tupla))
print(len(lista))
# tupla unitaria
tupla_unitaria = ("Ambrosio",)
print(tupla_unitaria)
print(len(tupla_unitaria))
# o, alternativa de sintaxis de tupla
tupla2 = "ambrosio", 12
print(tupla2)
# añadir nombre de variable a valores de tupla, desempaquetado de tuplas
nombre, dia = tupla2
print(nombre)
print(dia)
print(tupla2.index("ambrosio"))
