def funcion_Decoradora(funcion_parametro):
    # *args por convencion para pasarle un numero indeterminado de parametros
    def funcion_interior(*args):
        print("realizacion del calculo:")
        funcion_parametro(*args)
        print("Calculo terminado")

    return funcion_interior


@funcion_Decoradora
def suma(num1, num2):
    print(num1 + num2)


@funcion_Decoradora
def resta(num1, num2):
    print(num1 - num2)


suma(7, 5)
resta(12, 10)


def funcion_decoradora(funcion_parametro):
    # **kwargs por convencion para pasarle clave valor
    def funcion_interior(*args, **kwargs):
        print("realizacion del calculo:")
        funcion_parametro(*args, **kwargs)
        print("Calculo terminado")

    return funcion_interior


@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


potencia(base=5,exponente=3)