import pickle


class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena)


coche1 = Vehiculos("Mazda", "MXS")
coche2 = Vehiculos("Renault", "M2S")
coche3 = Vehiculos("Opel", "M3D")
coches = [coche1, coche2, coche3]
fichero = open("Los_Coches", "wb")
pickle.dump(coches, fichero)
fichero.close()
# del para eliminar de la memoria
del fichero

