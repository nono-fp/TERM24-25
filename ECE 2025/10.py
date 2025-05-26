# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def recherche (tab, n):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin)//2
        if n == tab [m]:
            return m
        if n > tab[m]:
            debut = m+1
        else:
            fin = m-1
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
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c
    return resultat
