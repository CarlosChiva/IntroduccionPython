class Areas():
    """Esta clase genera el area de las distintas figuras"""

    def areaCuadrado(lado):
        """ Calcula el area de un cuadrado a partir del parametro"""

        return "El area del cuadrado es: " + str(lado * lado)

    def areaTriangulo(base, altura):
        """Calcula el area de un triangulo segun los parametros"""
        return "El area del triangulo es: " + str((base * altura) / 2)


print(Areas.areaCuadrado.__doc__)
help(Areas.areaCuadrado)

print(Areas.areaTriangulo.__doc__)
help(Areas.areaTriangulo)

help(Areas)
