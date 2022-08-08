# 1er paso
import sqlite3

# 2o paso
# si no hay BBDD, al abrirla, la creara
miConexion = sqlite3.connect("PrimeraBase")
# 3er paso
miCursor = miConexion.cursor()


# 4o paso
def createTable():
    miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER ,SECCION VARCHAR(20))")


# 5o Paso
def insertValue():
    miCursor.execute("INSERT INTO PRODUCTOS VALUES('Pelota',20,'Deporte')")


def insercion_multiple():
    variosProductos = [
        ("Camiseta", 10, "Deportes"),
        ("Jarron", 90, "Deportes"),
        ("Camion", 30, "Jugueteria")
    ]
    miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)


def queryDataBase():
    miCursor.execute("SELECT * FROM PRODUCTOS")
    #fetchall devuelve como lista los registros extraidos por execute
    variosProductos = miCursor.fetchall()
    #print(variosProductos) o
    for productos in variosProductos:
        print(productos)
        print(productos[0])


queryDataBase()
miConexion.commit()

miConexion.close()
