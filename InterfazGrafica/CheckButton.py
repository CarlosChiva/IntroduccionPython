from tkinter import *

root = Tk()
root.title("Ejemplo")
playa = IntVar()
montanya = IntVar()
turismo = IntVar()


def opcionesViaje():
    opcionEscogida = ""
    if (playa.get() == 1):
        opcionEscogida += "playa"
    if (montanya.get() == 1):
        opcionEscogida += "Montaña"
    if (turismo.get() == 1):
        opcionEscogida += "Turismo"
    textoFinal.config(text=opcionEscogida)


foto = PhotoImage(file="ohm.png")
Label(root, image=foto).pack()
frame = Frame(root)
frame.pack()
Label(frame, text="Elige destino", width=50).pack()
# seleccionamos la variable asociada a cada checkbutton, onvalue para darle un valos a la hora de presionarlo y offvalue para resetear a 0 el valor de la variable y boton seleccionado
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montanya, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo", variable=turismo, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()
root.mainloop()
