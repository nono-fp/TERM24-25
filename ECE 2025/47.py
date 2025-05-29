# -*- coding: utf-8 -*-


"""EXERCICE 1 """

def taille (arbre,lettre):
    if lettre == '':
        return 0
    else :
        return 1 + taille(arbre,arbre[lettre][0])+taille(arbre,arbre[lettre][1])

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}
    
"""EXERCICE 2 """

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N-1):
        imin = k
        for i in range(k, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, imin, k)
    return tab

