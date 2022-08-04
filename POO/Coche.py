class Coche():
    # constructor
    def __init__(self):
        self.__largochasis = 250
        self.__anchochasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    # __ dos guiones bajos para encapsular= private

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif (self.__enmarcha and chequeo == False):
            return "Algo ha ido mal"
        else:
            return "el coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchochasis, " y un largo de ",
              self.__largochasis)
    # METODO PRIVATE CON GUION BAJO
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


micoche = Coche()
print(micoche.arrancar(True))
micoche.estado()

print("--A continuacion creamos el segundo objeto---")

micoche2 = Coche()
print(micoche2.arrancar(False))
micoche2.estado()
