# -*- coding: utf-8 -*-


"""EXERCICE 1 """

def indices_maxi(tab):
    indices = [0]
    for i in range(1,len(tab)):
        if tab[i]>tab[indices[0]]:
            indices = [i]
        elif tab[i] == tab[indices[0]]:
            indices.append(i)
    return (tab[indices[0]], indices)



"""EXERCICE 2 """

def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop())
    return pile_inverse


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        x = pile.pop()
        if x >= 0:
            pile_positifs.append(x)
    return renverse(pile_positifs)
