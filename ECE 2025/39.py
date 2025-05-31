# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def moyenne(tab) :
    if tab == []:
        return None
    result = 0
    total_pt = 0
    nb_chiffre = 0
    for  i in range(len(tab)):
        total_pt += tab[i]
        nb_chiffre += 1
    result = total_pt / nb_chiffre
    return result

"""EXERCICE 2 """

def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée
    j = len(tab)-1 # dernier indice de la zone non triée
    while i < j:
        if tab[i] == 0:
            i = i +1
        else:
            valeur = tab[j]
            tab[j] = 1
            tab[i] = valeur
            j = j-1
