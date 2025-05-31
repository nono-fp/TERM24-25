# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def moyenne(notes):
    total_points = 0
    total_coeff = 0
    note = 0
    for i in range(len(notes)):
        total_points += notes[i][0]*notes[i][1]
        total_coeff += notes[i][1]
    note = total_points / total_coeff
    return note

"""EXERCICE 2 """

def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1]
    for i in range(1,len(ligne)):
        ligne_suiv.append(ligne[i-1]+ligne[i])
    ligne_suiv.append(1)
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle
