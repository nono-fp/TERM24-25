# -*- coding: utf-8 -""*-

""" EXERCICE 1"""

def voisins_entrants(adj, x):
    liste= []
    for i in range(len(adj)):
        if x in adj[i]:
            liste.append(i)
    return liste

assert voisins_entrants([[1, 2], [2], [0], [0]], 0) == [2, 3]

assert voisins_entrants([[1, 2], [2], [0], [0]], 1) == [0]


"""EXERCICE 2"""

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(s)):
        if s[i] == chiffre:
            compte = compte +1
        else:
            resultat += f"{compte}" + f"{chiffre}"
            chiffre = s[i]
            compte = 1
    lecture_chiffre = f"{compte}" + f"{chiffre}"
    resultat += lecture_chiffre
    return resultat