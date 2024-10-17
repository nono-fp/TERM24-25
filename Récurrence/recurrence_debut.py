# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:00:45 2024

@author: n.faivrepierret
"""

def fonction(n):
    if n>0:
        fonction (n-1)
    print(n)
    



def fact(n):    #chercher le lien entre fact(n) et fact(n-1)
     if n > 0 :
        return n*fact(n-1)
     else:
        return 1
     
    
def fib(n): # pour le grand oral, bon exemple pour montrer suite de fibonacci avec ou sans récursivité
    if n== 0:
        return 0
    elif n==1:
        return 1
    else :
        return fib(n-1)+ fib(n-2) #suite de fibonnacci, somme des deux précédents
    
#Pb : complexité est trop grande donc on crée une liste

suite =[]

def fib(n):
    global suite
    if n== 0:
        return 0
    elif n==1:
        return 1
    else :
        if len(suite) > n :
            return suite[n]
        else:
            fib