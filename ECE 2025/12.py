# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def recherche(elt, tab):
    if elt not in tab:
        return None
    for i in range(len(tab)):
        if tab[i] == elt :
            return i
        
"""EXERCICE 2 """

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a
    print (tab_a)
    # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab_a[i+1]:
        tab_a[i] = tab_a[i+1]
        tab_a[i+1] = a
        i = i+1
    return tab_a
