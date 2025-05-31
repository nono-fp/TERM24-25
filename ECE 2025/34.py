# -*- coding: utf-8 -*-
from random import randint

"""EXERCICE 1 """

def tri_selection(tab):
    for i in range(len(tab)):
        mini = i
        for j in range(i, len(tab)):
            if tab[j] < tab[mini] :
                mini = j
        tab[i], tab[mini] = tab[mini], tab[i]
    return tab

"""EXERCICE 2 """

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 10 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print ("Perdu ! Le nombre était ", nb_mystere)
