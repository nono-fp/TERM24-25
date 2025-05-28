# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def nb_repetitions(elt, tab):
    repet = 0
    for i in range(len(tab)):
        if tab[i] == elt :
            repet += 1
    return repet

"""EXERCICE 2 """
def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = '' 
    while a > 0: 
        bin_a = str (a % 2) + bin_a 
        a = a//2
    return bin_a



