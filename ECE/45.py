# -*- coding: utf-8 -*-
"""
SUJET 45
"""

"""EXERCICE 1"""

def compte_occurrences(x,tab):
    compteur = 0
    for i in tab:
        if i == x :
            compteur += 1
    return compteur

"""EXERCICE 2"""

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = []
    a_rendre = somme_versee-somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(pieces[i])
        a_rendre = a_rendre-pieces[i]
    return rendu
