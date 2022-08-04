from tkinter import *

root = Tk()
# IntVar para especificar que la variable sera tipo enteros
varOption = IntVar()


def printt():
    print(varOption.get())
    if varOption.get() == 1:
        etiqueta.config(text="Has elegido masculino")
    elif varOption.get() == 2:
        etiqueta.config(text="Has elegido femenino")
    else:
        etiqueta.config(text="Has elegido otros")


Label(root, text="Genero: ").pack()
Radiobutton(root, text="Masculino", variable=varOption, value=1, command=printt).pack()
Radiobutton(root, text="Femenino", variable=varOption, value=2, command=printt).pack()
etiqueta = Label(root)
etiqueta.pack()
root.mainloop()
