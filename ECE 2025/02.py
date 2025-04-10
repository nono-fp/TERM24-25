# -*- coding: utf-8 -*-
"""
Sujet 02
"""

def fibonacci(n):
    if n<3:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

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
