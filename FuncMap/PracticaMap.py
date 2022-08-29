class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja de {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [Empleado("Juan", "Director", 7500),
                  Empleado("Ana", "Presidenta", 8500),
                  Empleado("Antonio", "Administrativo", 2500),
                  Empleado("Sara", "Secretaria", 2700)]


def calculo_Comision(empleado):
    empleado.salario = empleado.salario * 1.03
    return empleado

# la mayor diferencia con filtrer es que map utiliza una funcion exogena a esta
listaEmpleadosComision = map(calculo_Comision, listaEmpleados)
for empleado in listaEmpleadosComision:
    print(empleado)
