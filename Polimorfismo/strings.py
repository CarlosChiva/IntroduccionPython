nombreUsuario = input("Introduce tu nombre de usuario: \n")
print("El nombre de usuario es: ", nombreUsuario.lower())
print("El nombre de usuario es: ", nombreUsuario.upper())
print("El nombre de usuario es: ", nombreUsuario.capitalize())

edad = input("introduce la edad: \n")
while (edad.isdigit() == False):
    edad = input("Try again\n")

if (int(edad) < 18):
    print("No puedes pasar")
else:
    print("Puedes pasar")
