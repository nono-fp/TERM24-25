# -*- coding: utf-8 -*-
"""
SUJET 47
"""

"""EXERCICE 1"""

def max_dico(dico):
    max_valeur= 0
    max_cle = ''
    for cle,valeur in dico.items():
        if valeur > max_valeur :
            max_valeur = valeur
            max_cle = cle
    return (max_cle,max_valeur)
    
"""EXERCICE 2"""

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
            if element != '+' or element != '*':
                p.empiler(element)
            else:
                if element == '+':
                    resultat = p.depiler() + p.depiler()
                else:
                    resultat = p.depiler()*p.depiler()
                p.empiler(resultat)
        return resultat


