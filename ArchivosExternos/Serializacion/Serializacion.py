import pickle

lista_nombres = ["Pedro", "MAria", "Ambrosio"]
fichero_binario = open("lista_Nombres", "wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()
