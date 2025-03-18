# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 14:20:13 2025

@author: n.faivrepierret
"""


def ecrtiure_binaire_positif1(n):
    string = ""
    k = 0
    if n == 0 :
        string += f"{n}"
    while n > 0 :
        k = n % 2
        n = n// 2
        string = f"{k}"+string
    return string




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
        for j in range(n-i-1):
            if tab[j] > tab[j+1]:
                  echange(tab, j, j+1)
                    
#i dit combien d'élément sont fixés
