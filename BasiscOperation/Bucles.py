for i in [1, 2, 3]:
    print("hola")
    print(i)
# print de java
for j in ["ey", "Ya tu sabeh", "yo no seh"]:
    print("hola", end=" ")
print()
# cuando un string, caracter a caracter
hay_k = False
contador = 0
for x in "abadakedabra":
    print(x)
    contador += 1
    if x == "k":
        hay_k = True

if hay_k:
    print("Hay una K")

print("numero de letras es: ", contador)

# tipo range for con contador

for c in range(5):
    print(f"valor de la variable {c}", " eyy")

# valor inicial del for, valor final del for, y cuanto se le suma
for q in range(5, 500, 10):
    print(q)

# leer string caracter a caracter con bucle
nombre = "Elñordohumano"
for p in range(len(nombre)):
    if nombre[p] == "ñ":
        print("OK, its in position:", p)

# bucle while
i = 1
while i < 10:
    print(i)
    i += 1
k = 10
contador = 0
while k > 0:
    k += 1
    contador += 1
    print(k)
    if contador == 3:
        break
print(k, " ", contador)

# continue para pasar a la siguiente iteracion

for letra in "Python":
    if letra == "h":
        continue

    print(letra, end="")
# pass es null, utilizado para dejar algo a medias y no romper el resto programa
# se puede añadir un else para el for que se ejecutara si el for llega al final