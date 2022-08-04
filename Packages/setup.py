from  setuptools import setup

setup(
    name="Paquete Calculos",
    version="1.0",
    description="Paquete de calculos",
    author="Yomismo",
    author_email="sdggdsfgdsfg",
    url="dsfgdsgds",
    packages=["calculos","calculos.CalculosGenerales"]


)
# Una vez creado este fichero, ir desde comandos y poner "python setup.py sdist"
# Eso creara un archivo comprimido y una carpeta llamada dist
# para la instalacion del packete en el sistema python, desde linea de comandos vamos a la carpeta dist, y escribimos "pip3 install nombrePackete"
#Para desinstalar , desde donde sea "pip3 uninstall nombrePaquete"