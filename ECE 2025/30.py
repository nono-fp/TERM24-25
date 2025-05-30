# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def delta(liste):
    new_tab =[liste[0]]
    for i in range(1,len(liste)) :
        new_tab.append(liste[i]-liste[i-1])
    return new_tab

"""EXERCICE 2 """

class Expr:
    """Classe implémentant un arbre d'expression."""

def __init__(self, g, v, d):
    """un objet Expr possède 3 attributs :
    - gauche : la sous-expression gauche ;
    - valeur : la valeur de l'étiquette, opérateur ou nombre ;
    - droite : la sous-expression droite."""
    self.gauche = g
    self.valeur = v
    self.droite = d

def est_une_feuille(self):
    """renvoie True si et seulement
    si le noeud est une feuille"""
    return self.gauche is None and self.droite is None

def infixe(self):
    """renvoie la représentation infixe de l'expression en
    chaine de caractères"""
    s = ''
    if self.gauche is not None:
        s =  '(' + self.gauche.infixe()
    s = s + str(self.valeur)
    if self.droite is not None:
        s = s + self.droite.infixe() + ')'
    return s
