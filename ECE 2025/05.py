# -*- coding: utf-8 -*-



"""EXERCICE 1 """

def renverse (mot):
    nouveau_mot = ""
    for i in range (len(mot)):
        nouveau_mot = str(mot[i]) + nouveau_mot
    return nouveau_mot


"""EXERCICE 2 """

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = i 
            while multiple < n:
                tab[multiple] = False
                multiple = multiple + i
    return premiers
