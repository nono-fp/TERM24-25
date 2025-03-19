# -*- coding: utf-8 -*-
"""
SUJET 18
"""


"""EXERCICE 1"""

def multiplication(n1,n2):
    result = 0
    for i in range (abs(n2)):
        if n1<0 and  n2<0 :
            result += -n1
        else :
            result += n1
    return result


"""EXERCICE 2"""

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab,
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m+1 , j )
    elif tab[m] > x:
        return chercher(tab, x, i , m-1)
    else:
        return m