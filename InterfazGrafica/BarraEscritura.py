from tkinter import *

root = Tk()
miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0)
cuadroTexto = Entry(miFrame)
# metodo grid posiciona cual tabla de coordenadas un elemento, posicionado por coordenadas row y column
cuadroTexto.grid(row=0, column=1)

# se puede cambiar la alineacion de el label con otro parametro grid sticky= e w s n
nombreLabel = Label(miFrame, text="Apellido: ")
nombreLabel.grid(row=1, column=0)

cuadroApellido = Entry(miFrame)
# justify para alineacion de texto
cuadroApellido.config(justify="center")
# padx y pady es padding en css, tod dentro de grid como parametro
cuadroApellido.grid(row=1, column=1)

nombrepassword = Label(miFrame, text="Password: ")
nombrepassword.grid(row=2, column=0)

password = Entry(miFrame)
# parametro show para que aparezcan el caracter indicado por el parametro envez de salir las palabras introducidas
password.config(show="*")
password.grid(row=2, column=1)
root.mainloop()
