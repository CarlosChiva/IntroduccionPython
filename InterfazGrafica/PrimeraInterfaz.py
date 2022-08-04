from tkinter import *

# Tk igual a JFrame
raiz = Tk()
raiz.title("Ventana de pruebas")
# booleanos o 2 parametros weigh and heith
# raiz.resizable(True, 0)
# imagen de titulo con extension ico
raiz.iconbitmap("ohm.ico")
# tamaño de la ventana, quitarlo si tiene frame ya que siempre se adaptara al tamaño de sus frames
# raiz.geometry("500x350")
# bg background
raiz.config(bg="grey")
miFrame = Frame()
miFrame.pack()
# miFrame.pack(side=Right) con esto al redimensionar, el frame se coloca en esa posicion mas otro parametro anchor para las esquinas
#  miFrame.pack(fill="x/y/Both") el frame se adaptara a las coordenadas indicadas por el fill "y" necesita segundo parametro "expand=True para funcionar
miFrame.config(bg="red")
miFrame.config(width=200, height=300)
# borde
miFrame.config(bd=35)
miFrame.config(relief="groove")
# raton al posicionarse encima del frame
miFrame.config(cursor="pirate")
# mainLoop siempre al final para que la ventana se quede a la espera de instrucciones
raiz.mainloop()
