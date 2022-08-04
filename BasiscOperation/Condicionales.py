print("Condicionales y Scanner")


# nota1 = input("Introduce los numeros: \n")
# nota2 = input()


def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


# importante el int, el escanner lo detecta como string
# print(evaluacion(int(nota1)))
# print(evaluacion(int(nota2)))

print("----------------")
edadusuario = int(input("introduce tu edad: \n"))


def mayoredad(numero):
    if numero < 18:
        print("No puedes pasar")
    else:
        print("Puedes Pasar")


mayoredad(edadusuario)


def mayoredadavanced(number):
    if number < 18:
        print("No puedes pasar")
    elif number > 100:
        print("Ni de broma tienes esa edad")
    else:
        print("Puedes pasar")


mayoredadavanced(int(input("Edad: \n")))
