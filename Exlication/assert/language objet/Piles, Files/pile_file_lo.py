# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:39:32 2024

@author: n.faivrepierret
"""

class Pile:
    def pile_vide():
        return Pile()
    
    def __init__(self, tete=None, queue=None):
        self.tete = tete
        self.queue = queue
    
    def est_vide(self) : 
        return self.tete is None
    
    def  pop(self):
        if self.pile_vide():
            return None
        resultat = self.tete
        self.tete = self.queue.pop()
        return resultat
    
    
    def push(self, valeur):
        if  self.est_vide():
            self.queue = Pile.pile_vide()
        else:
            self.queue.push(self.tete)
        self.tete = valeur
        
    def taille(self):
        if self.est_vide():
            return 0
        return 1 + self.queue.taille()
    
    def sommet(self):
        return self.tete
    
    
class File : 
    
    def file_vide():
        return File()
    
    
    
    def __init__(self, tete=None, queue=None):
        self.tete = tete 
        self.queue = queue
    
    def est_vide(self):
        return self.tete is None
    
    def ajout(self, valeur):
        if  self.est_vide():
            self.queue = Pile.file_vide()
            self.tete = valeur
        else:
            self.queue.ajout(self.valeur)
        
    
    def retire(self):
        if self.file_vide():
            return None
        resultat = self.tete
        self.tete = self.queue.retire()
        return resultat
    
    def premier(self):
        return self.tete
    
    def taille(self):
        if self.est_vide():
            return 0
        return 1 + self.queue.taille()
        

file = File.file_vide()
file.ajout(1)
file.ajout(2)
file.ajout(3)
file.ajout(4)
print(file.taille())
while not file.est_vide():
    print(file.retire())
    
pile= Pile.pile_vide()
pile =Pile.pile_vide()
pile.ajout(1)
pile.ajout(2)
pile.ajout(3)
pile.ajout(4)
print(pile.taille())
while not pile.est_vide():
    print(pile.pop())    
