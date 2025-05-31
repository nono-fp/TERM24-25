# -*- coding: utf-8 -*-

"""EXERCICE 1 """

def moyenne (tab):
    result = 0.0
    total_points = 0.0
    nb_notes = 0.0
    for i in range(len(tab)) :
        total_points += tab[i]
        nb_notes += 1
    result = total_points / nb_notes
    return result

"""EXERCICE 2 """

def binaire(a):
    '''convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0 :
        bin_a = str(a%2) + bin_a
        a = a //2
    return bin_a
        