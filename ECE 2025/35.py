# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def max_dico1(dico):
    cle_max  = None
    val_max = 0
    for key, value in dico.items() :
        if value > val_max :
            val_max = value
            cle_max = key
    return cle_max, val_max

""" EXERCICE 2 """

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for element in tab: 
        if element != '+' and element != '*': 
            p.empiler(element) 
        else:
            if element == '+': 
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler() 
            p.empiler(resultat) 
    return p.depiler()


