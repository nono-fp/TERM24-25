# -*- coding: utf-8 -*-



"""EXERCICE 1"""

def ecriture_binaire_entier_positif (n):
    binaire = ''
    if n == 0:
        return '0'
    while n >0:
       binaire = str(n%2) + binaire
       n= n//2
    return binaire


"""EXERCICE 2 """

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp
    
def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n):
        for j in range(n-i):
            if tab[j] > tab[j+1]:
                echange(tab, j,j+1 )
    return tab

