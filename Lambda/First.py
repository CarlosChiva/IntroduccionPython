'''def area_triangulo(base, altura):
    return (base * altura) / 2


print(area_triangulo(5, 7))
'''

area_triangulo = lambda base, altura: (base * altura) / 2
print(area_triangulo(7, 5))
al_cubo = lambda numero: numero ** 3
print(al_cubo(2))
al_cubo2 = lambda numero: pow(numero, 3)
print(al_cubo2(2))

destacarValor=lambda comision:"¡{}!$".format(comision)
comision1=15585
print(destacarValor(comision1))
