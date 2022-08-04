import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    # str para traducir en cadena de texto la informacion del objeto
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    pers0nas = []

    def __init__(self):
        # ab+ es igual a append binary
        listaDEPersonas = open("ficheroExterno", "ab+")
        listaDEPersonas.seek(0)
        try:
            self.pers0nas = pickle.load(listaDEPersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.pers0nas)))
        except:
            print("Fichero vacio")
        finally:
            listaDEPersonas.close()
            del listaDEPersonas

    def agregarPersonas(self, personas):
        self.pers0nas.append(personas)
        self.guardarPersonas()

    def guardarPersonas(self):
        listaPersonas = open("ficheroExterno", "wb")
        pickle.dump(self.pers0nas, listaPersonas)
        listaPersonas.close()
        del listaPersonas

    def mostrarPersonas(self):
        for i in self.pers0nas:
            print(i)
    def mostrarInformFicheroExterno(self):
        print("Personas guardadas: \n")
        for i in self.pers0nas:
            print(i)

miLista = ListaPersonas()
p = Persona("Sandra", "Femenino", 18)
miLista.agregarPersonas(p)
p = Persona("Pepe", "Fluido", 20)
miLista.agregarPersonas(p)
p = Persona("JoseAntonio", "Helicoptero", 10)
miLista.agregarPersonas(p)
miLista.mostrarInformFicheroExterno()
