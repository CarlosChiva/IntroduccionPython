def funcion_Decoradora(funcion_parametro):
    def funcion_interior():
        print("realizacion del calculo:")
        funcion_parametro()
        print("Calculo terminado")

    return funcion_interior


# el arroba se utiliza para denominar el metodo que este asociado a la funcion decoradora
@funcion_Decoradora
def suma():
    print(15 + 20)


@funcion_Decoradora
def resta():
    print(30 - 10)


suma()
resta()