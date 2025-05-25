# -*- coding: utf-8 -*-


"""EXERCICE 1 """

def multiplication (n1,n2):
    result = 0
    for i in range(abs(n1)):
        result = result + n2
    if n2 > 0 and n1 > 0 or n1 <0 and n2 < 0:
        return result
    else :
        return -result
    
"""EXERCICE 2 """

def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False