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
        print("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena)


class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(Vehiculos):
    jcaballito = ""

    def caballito(self):
        self.jcaballito = "Voy hacinendo el caballito"

    # override
    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena, "\n", self.jcaballito)


class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


mimoto = Moto("Honda", "Cbr")
mimoto.estado()
mimoto.caballito()
mimoto.estado()

mifurgoneta = Furgoneta("Renault", "Kangoo")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))


# doble herenncia
class BicicletaElectrica(VElectricos, Vehiculos):
    def descripcion(self):
        super().estado()


mibici = BicicletaElectrica("opel","1500")
mibici.descripcion()
# isinstance = instance of
print(isinstance(mibici,Vehiculos))
