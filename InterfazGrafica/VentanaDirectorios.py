from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Ejemplo")


def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C: ",
                                         filetypes=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de Texto", "*.txt"),
                                                    ("Archivos Python", "*.py"), ("Todos los archivos", "*.*")))
    print(fichero)


Button(root, text="Abrir fichero", command=abreFichero).pack()
root.mainloop()
