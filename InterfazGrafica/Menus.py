from tkinter import *
# ventanas emergentes hay que importarlos aparte
from tkinter import messagebox

root = Tk()
root.title("Ejemplo")


def infoAdicional():
    messagebox.showinfo("Procesador de titulo", "Procesador de textos version 2022")


def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo mi licencia version 2022")


def salirAplicacion():
    # askquestion devuelve el valor de las opciones si o no
    valor = messagebox.askquestion("Salir", " Deseas salir de la aplicacion?")
    if valor == "yes":
        # destroy para eliminar la ventana entera
        root.destroy()


# tambien se puede hacer con askokcancel que devuelve valores booleanos
def cerrarDocum():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor == False:
        root.destroy()


barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
# tearoff para que no haya una barra extra al principio del menu
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
# add separator para crear una linea para separar graficamente los elementos
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirAplicacion)
archivoMenu.add_command(label="Cerrar", command=cerrarDocum)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barraMenu)
archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de..", command=infoAdicional)
# label para el texto y menu para el tipo de menu al que se le añadira a la barra de menu
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()
