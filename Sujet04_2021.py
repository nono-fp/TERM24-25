# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:47:06 2024

@author: n.faivrepierret
"""

def fonction1(tab, i):
 nb_elem = len(tab)
 cpt = 0
 for j in range(i+1, nb_elem):
     if tab[j] < tab[i]:
         cpt += 1
 return cpt


def fonction2(tab):
    S = 0
    for i in range(len(tab)):
        S+= fonction1(tab, i)
    return S



def moitie_gauche(tab):
    return tab[:(len(tab)+1)//2]


def moitie_droite (tab):
    return tab[(len(tab))//2:]

def nb_inv_tab(tab1,tab2):
    new_tab = tab1+ tab2
    return fonction2(new_tab)


def tri(tab):
    return tab[:].sort

def nb_inversions_rec(tab):
    tab_gauche = moitie_gauche(tab)
    tab_droit= moitie_droite(tab)
    total_inversion = 0#nb_inversions_rec(tab_gauche) + nb_inversions_rec(tab_droit)

    trier_droit = tri( tab_droit)
    trier_gauche = tri( tab_gauche)
     
    return total_inversion + nb_inv_tab(trier_gauche, trier_droit)

