# -*- coding: utf-8 -*-
"""
SUJET 48
"""

"""EXERCICE 1"""


def voisins_entrants(adj,x):
    voisins = []
    for i in range (0, len(adj)):
        if x in adj[i] : #on ne met pas adj{i} == x car c'est un tableau de tableau, mais ça marche si c'est juste un tableau simple
            voisins.append(i)
    return voisins  


"""EXERCICE 2"""

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representÃ© par s
    en appliquant le procÃ©dÃ© de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += f'{compte}' + f'{chiffre}' 
            chiffre = s[i]
            compte = 1
    lecture_chiffre = f'{compte}' + f'{chiffre}' 
    resultat += lecture_chiffre
    return resultat
