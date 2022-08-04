edad = int(input())

if 0 < edad < 100:
    print("Edad Correcta")
else:
    print("Edad incorrecta")

jefe = int(input("Salario jefe"))
print("salario del jefe: " + str(jefe))
# con una coma traga perfectamente un str con un int
administrativo = int(input("Salario administrativo"))
print("salario del administrativo: " + str(administrativo))

currela = int(input("Salario del currela"))
print("salario del currela: ", currela)

if jefe > administrativo > currela:
    print("cobran lo que toca")
else:
    print("Te han timao")

# operadores logicos
distancia = 40
numerodehermanos = 2
salariofamiliar = 20000
distancia_escuela = int(input("Escribe tu distancia a la escuela"))
numero_de_hermanos = int(input("Escribe numero de hermanos"))
salario_de_la_familia = int(input("Escribe salario de casa"))
if distancia_escuela > distancia and numero_de_hermanos > numerodehermanos and salario_de_la_familia < salariofamiliar:
    print("Tienes derecho a beca")
else:
    print("no tienes derecho a nada")

# en socialismo

if distancia_escuela > distancia or numero_de_hermanos > numerodehermanos or salario_de_la_familia < salariofamiliar:
    print("Sanchez aproved")
else:
    print("A la casta ni agua")

# operador in

print("Informatica - Software - SexShop")
asignatura = input("escribe la asignatura").lower()
if asignatura in ("informatica", "software", "sexShop"):
    print("Asignatura elegida es " + asignatura)
else:
    print("No existe esa asignatura")
