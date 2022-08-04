from tkinter import *

root = Tk()
miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

nombreTexto = Entry(miFrame)
nombreTexto.grid(row=0, column=1, padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")

cuadroApellido = Entry(miFrame)
cuadroApellido.config(justify="center")
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

comentarioLabel = Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")

textoComentario = Text(miFrame, width=16, height=5)
# para barra de scroll se crea un scrollbar al que se le pone de parametros elcontenedor, en comand se le dice a que elemento se añadira y con el metodo de yview o  xview para que eje hará scroll
scrollVertical = Scrollbar(miFrame, command=textoComentario.yview)
scrollVertical.grid(row=2,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVertical.set)
textoComentario.grid(row=2, column=1, padx=10, pady=10)

botonDeEnvio=Button(root,text="Enviar")
botonDeEnvio.pack()

root.mainloop()
