# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:36:07 2025

@author: n.faivrepierret
"""

import random

dic = {"bob":100,"Jane":65}

def max_dico1(dic):
    maxi= list(dic.keys())[0]
    for i in dic:
        if dic[i] > dic[maxi]:
            maxi = dic[i]
    return (maxi)


def max_dico(dic):
    maxi= 0
    pseudo = ''
    for k,v in dic.items():
        if v > maxi:
            maxi = v
            pseudo = k
    return (pseudo,maxi)


tableaux_aleatoires = [[random.randint(1, 100) for _ in range(10)]] 

def somme (tab):
    somme = 0
    for k in range (len(tab)) :
        somme += tab[k]
    return somme
    



def verif1():
    for i in range(1,100):
        tab =[[random.randint(1, 100) for _ in range(10)]]
        somme = 0
        for k in range (len(tab)) :
            somme += tab[k]
        if fonction ==somme
        return True
