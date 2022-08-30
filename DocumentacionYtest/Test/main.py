def areaTriangulo(base, altura):
    """Calcula el area de un triangulo segun los parametros
    >>> areaTriangulo(3,6)
    'El area del triangulo es: 9.0'
    >>> areaTriangulo(4,5)
    'El area del triangulo es: 10.0'
    >>> areaTriangulo(9,3)
    'El area del triangulo es: 13.5'
    """
    return "El area del triangulo es: " + str((base * altura) / 2)


def arrobaCheck(mailUsuario):
    """
    Comprueba el mail de usuario que contenga un arroba y no este en el principio ni en el final
    >>> arrobaCheck('yomismo@yo.org')
    True
    >>> arrobaCheck('yomismo@yo.org@')
    False
    >>> arrobaCheck('yomismoyo.org')
    False
    >>> arrobaCheck('y@mismo@yo.org')
    False
    """
    arroba = mailUsuario.count('@')
    if (arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario) - 1) or mailUsuario.find('@') == 0):
        return False
    else:
        return True


import doctest

doctest.testmod()
