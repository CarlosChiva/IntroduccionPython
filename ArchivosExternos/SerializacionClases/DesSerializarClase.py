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


ficheroApertura=open("Los_Coches","rb")
misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for i in misCoches:
    print(i.estado())
