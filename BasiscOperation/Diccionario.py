# parecido a Map, da igual el orden
# Clave y despues valor
midiccionario = {"Alemania": "Berlin", "Francia": "Paris", "España": "Madrid"}
# buscamos por la clave y nos dara su valor
print(midiccionario["Francia"])
#  imprimirlo all
print(midiccionario)
# agregar elemento
midiccionario["Italia"] = "Lisboa"
print(midiccionario)
# corregir un valor
midiccionario["Italia"] = "Roma"
print(midiccionario)
# eliminar elemento
del midiccionario["Italia"]
print(midiccionario)
# añadir claves en un diccionario a partir de una tupla
mitupla = ["España", "Francia", "Reino Unido"]
midiccionario = {mitupla[0]: "Madrid", mitupla[1]: "Paris", mitupla[2]: "Londres"}
print(midiccionario)

midiccionario2 = {23: "Jordan", "Nombre": "Michael", "anillos": [1991, 1992, 1993]}
print(midiccionario2)
print(midiccionario2["anillos"])
# diccionario con un diccionario dentro
midiccionarioconsub = {23: "Jordan", "Nombre": "Michael", "anillos": {"temporadas": [1991, 1992, 1993]}}
print(midiccionarioconsub["anillos"])
# ver las claves
print(midiccionarioconsub.keys())
# valores
print(midiccionarioconsub.values())
# longitud
print(len(midiccionarioconsub))

print(midiccionarioconsub["anillos"].keys())
print(midiccionarioconsub["anillos"].values())
