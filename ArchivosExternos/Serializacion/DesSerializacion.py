import pickle
fichero=open("lista_Nombres","rb")

lista=pickle.load(fichero)

print(lista)
