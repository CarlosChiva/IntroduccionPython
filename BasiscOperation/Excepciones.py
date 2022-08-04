def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("no se puede dividir por cero")
        return "Operacion erronea"


def multiplica(num1, num2):
    return num1 * num2


while True:
    try:
        op1 = int(input())
        op2 = int(input())
        break
    except ValueError:
        print("Deben ser numeros, intentalo de nuevo")

# el break lo lee si no salta la excepcion
operacion = input("Introduce la operacion a realizar: ")
if operacion == "suma":
    print(suma(op1, op2))
elif operacion == "resta":
    print(resta(op1, op2))
elif operacion == "multiplica":
    print(multiplica(op1, op2))
elif operacion == "divide":
    print(divide(op1, op2))
else:
    print("Operacion no contemplada")
print("Fin del programa")


def dividir():
    try:
        op1 = float(input("Introduce el primer numero: "))

        op2 = float(input("Introduce el segundo numero: "))
        print(f"la division es {op1 / op2}")
    except ValueError:
        print("Fallo en los valores")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    finally:
        print("Calculo finalizado")

dividir()