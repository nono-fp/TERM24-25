# -*- coding: utf-8 -*-


"""EXERCICE 1 """

def selection_enclos (animaux, num_enclos):
    tab1 = []
    for animal in animaux:
        if animal['enclos'] == num_enclos :
            tab1.append(animal)
    return tab1

"""EXERCICE 2 """

def trouver_intrus(tab, g, d):
    """Renvoie la valeur de l'intrus situé entre les indices g et d
    ↪
    dans le tableau tab où :
    tab vérifie les conditions de l'exercice,
    g et d sont des multiples de 3."""
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice+1]:
            return trouver_intrus(tab,indice+3,d)
        else:
            return trouver_intrus(tab,g,indice)
