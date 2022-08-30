import math


def raizCuadrada(listaNumeros):
    """
    La funcion devuelve una lista con la raiz uadrada de los elementos numericos pasados por parametros

    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4,-9,16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """
    return [math.sqrt(n) for n in listaNumeros]


import doctest

doctest.testmod()
