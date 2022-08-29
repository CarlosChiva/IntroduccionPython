def numero_par(num):
    if num % 2 == 0:
        return True


numeros = [17, 24, 7, 39, 8, 51, 92]
# filter con dos parametros, funcion a utilizar y lista o objeto a analizar
# para que se pueda ver hay que castearlo a lista con el list del principio
print(list(filter(numero_par, numeros)))

print(list(filter(lambda numero_par: numero_par % 2 == 0, numeros)))


# ----------------------------------para objetos-------------------------------------

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja de {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [Empleado("Juan", "Director", 750000),
                  Empleado("Ana", "Presidenta", 850000),
                  Empleado("Antonio", "Administrativo", 25000),
                  Empleado("Sara", "Secretaria", 27000)]

salarios_altos = filter(lambda empleado: empleado.salario > 50000, listaEmpleados)
for empleadosRicos in salarios_altos:
    print(empleadosRicos)
