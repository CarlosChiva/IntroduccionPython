from tkinter import *

root = Tk()
miFrame = Frame(root)
miFrame.pack()
operacion = ""
resultado = 0

# -----------Pantalla-----------
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable=numeroPantalla)
# columnspan para que ocupe las diferentes columnas del resto de elementos para no separarlos
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


# ----------pulsaciones de teclado----------------
def numeropantalla(numero):
    global operacion
    if operacion != "":
        numeroPantalla.set(numero)
        operacion = ""

    else:
        numeroPantalla.set(numeroPantalla.get() + numero)


# ---------------Funcion--------------------------
def suma(numero):
    global operacion
    global resultado
    resultado += int(numero)
    operacion = "suma"
    numeroPantalla.set(resultado)


def restar(numero):
    global operacion
    global resultado
    resultado -= int(numero)
    operacion = "restar"
    numeroPantalla.set(resultado)


def multiplicar(numero):
    global operacion
    global resultado
    resultado *= int(numero)
    operacion = "multiplicar"
    numeroPantalla.set(resultado)


def dividir(numero):
    global operacion
    global resultado
    resultado = resultado / int(numero)
    operacion = "dividir"
    numeroPantalla.set(resultado)


def elResultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0


# ----------Fila 1-----------------
boton7 = Button(miFrame, text="7", width=3, command=lambda: numeropantalla("7"))
boton7.grid(row=2, column=1)

boton8 = Button(miFrame, text="8", width=3, command=lambda: numeropantalla("8"))
boton8.grid(row=2, column=2)

boton9 = Button(miFrame, text="9", width=3, command=lambda: numeropantalla("9"))
boton9.grid(row=2, column=3)

botonDiv = Button(miFrame, text="/", width=3, command=lambda: dividir(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)
# ----------Fila 2-----------------
boton4 = Button(miFrame, text="4", width=3, command=lambda: numeropantalla("4"))
boton4.grid(row=3, column=1)

boton5 = Button(miFrame, text="5", width=3, command=lambda: numeropantalla("5"))
boton5.grid(row=3, column=2)

boton6 = Button(miFrame, text="6", width=3, command=lambda: numeropantalla("6"))
boton6.grid(row=3, column=3)

botonMult = Button(miFrame, text="*", width=3, command=lambda: multiplicar(numeroPantalla.get()))
botonMult.grid(row=3, column=4)
# ----------Fila 3-----------------
boton1 = Button(miFrame, text="1", width=3, command=lambda: numeropantalla("1"))
boton1.grid(row=4, column=1)

boton2 = Button(miFrame, text="2", width=3, command=lambda: numeropantalla("2"))
boton2.grid(row=4, column=2)

boton3 = Button(miFrame, text="3", width=3, command=lambda: numeropantalla("3"))
boton3.grid(row=4, column=3)

botonDiv = Button(miFrame, text="-", width=3, command=lambda: restar(numeroPantalla.get()))
botonDiv.grid(row=4, column=4, )
# ----------Fila 4-----------------
boton0 = Button(miFrame, text="0", width=3, command=lambda: numeropantalla("0"))
boton0.grid(row=5, column=1)

botonDot = Button(miFrame, text=".", width=3, command=lambda: numeropantalla("."))
botonDot.grid(row=5, column=2)

botonequal = Button(miFrame, text="=", width=3, command=lambda: elResultado())
botonequal.grid(row=5, column=3)

botonadd = Button(miFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get()))
botonadd.grid(row=5, column=4)

root.mainloop()
