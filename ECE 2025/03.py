# -*- coding: utf-8 -*-


"""EXERCICE 1"""

def fibo(n):
    if n<= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

"""EXERCICE 2 """

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(len(notes)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]
    return (note_maxi, meilleurs_eleves)