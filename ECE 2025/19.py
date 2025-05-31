# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def recherche_min(tab):
    mini = 0
    for i in range (len(tab)):
        if tab[i] < tab[mini] :
            mini = i
    return mini

"""EXERCICE 2 """

def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab) -1
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = gauche +1
        else :
            tab[gauche] = tab[droite]
            tab[droite] = 1
            droite = droite -1
    return tab
