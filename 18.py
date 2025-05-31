# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def moyenne(tab):
    total_pt = 0
    total_nb = 0
    for i in range(len(tab)):
        total_pt += tab[i]
        total_nb += 1
    return total_pt / total_nb

"""EXERCICE 2 """

def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""
    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        m = (debut+fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m+1
        else:
            fin = m-1
    return False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) ==False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) == False

assert dichotomie([], 28) == False