from tkinter import *

root = Tk()
# sintaxis, contenedor, otras que afectan al contenido a adjuntar
miFrame = Frame(root, width=500, height=400)
miFrame.pack()
miLabel = Label(miFrame, text="Hola", fg="red", font=("Arial", 18))
# place se utiliza para ubicar el label dentro de su contenedor
miLabel.place(x=100, y=100)
# Se puede abreviar en una sola linea Label(miFrame,text="Hola").place(x=100,y=100)
miImagen = PhotoImage(file="ohm.png")
Label(miFrame, image=miImagen).place(x=250, y=230)
root.mainloop()
