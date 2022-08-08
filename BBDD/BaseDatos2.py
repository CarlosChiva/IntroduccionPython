import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()


def createAndFillTable():
    miCursor.execute('''
     CREATE TABLE PRODUCTOS (
     Id INTEGER PRIMARY KEY AUTOINCREMENT ,
     NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
     PRECIO INTEGER ,
     SECCION VARCHAR (20))
 ''')
    productos = [
        ("pelota", 20, "jugueteria"),
        ("pantalon", 15, "confeccion"),
        ("destornillador", 25, "ferreteria"),
        ("jarron", 45, "ceramica")
    ]

    # NULL ya que se autorrellenara con la clave primaria autoincremental
    miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)



# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")
miCursor.execute("DELETE FROM PRODUCTOS WHERE  Id=4")
miConexion.commit()
miConexion.close()
