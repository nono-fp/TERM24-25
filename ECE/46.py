# -*- coding: utf-8 -*-
"""
SUJET 46
"""

"""EXERCICE 1"""
 
def recherche(tab,n):
    a = 0
    b = len(tab)-1
    while a <= b:
        m = (a+b) // 2
        if tab[m] == n:
            return m
        elif tab[m] < n:
            a = m+1
        else :
            b = m-1
    return None

"""EXERCICE 2"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat+c
    return resultat
