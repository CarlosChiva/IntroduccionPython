def generaPares(limite):
    num = 1
    milista = []
    while num < limite:
        milista.append(num * 2)
        num += 1
    return milista


print(generaPares(10))


# ahora con generador

def generaparesgenerador(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1


devuelvepares = generaparesgenerador(10)

print(next(devuelvepares))
print("otras lineas")
print(next(devuelvepares))


# el * para decir que va a recibir un numero indeterminado de parametros en forma tupla
# yeld from se utiliza como un for anidado para subelementos
def devuelveciudades(*ciudades):
    for elemento in ciudades:
            yield from elemento


ciudades_devueltas = devuelveciudades("Madrid", "Barcelona", "Bilbao")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
