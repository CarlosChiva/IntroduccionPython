import math


def evaluaedad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas")

    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 65:
        return "eres maduro"


# print(evaluaedad(-15))

def calcularaiz(num1):
    if num1 < 0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)


op1 = int(input("introduce numero: "))
try:
    print(calcularaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Fin del programa")
