# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:26:20 2024

@author: n.faivrepierret
"""

def hauteur (arbre):
    if arbre== ():
        return 0
    else:
        ag,n,ad= arbre
        return 1 + max(hauteur(ag), hauteur(ad))


def taille (arbre):
    if arbre==():
        return 0
    else:
        ag,n,ad=arbre
        return 1+ taille(ag)+taille(ad)

def parcours_infixe1(arbre):
    if arbre !=():
        ag,n,ad=arbre
        parcours_infixe(ag)
        print(n)
        parcours_infixe(ad)



def parcours_prefixe(arbre):
    if arbre!= ():
        ag,n,ad =arbre
        print(n)
        parcours_prefixe(ag)
        parcours_prefixe(ad)


def parcours_suffixe(arbre):
    if arbre!= ():
        ag,n,ad =arbre
        print(n)
        parcours_suffixe(ag)
        parcours_suffixe(ad)    

def arbre_recherche(arbre,k):
    if arbre == ():
        return False
    else :
        ag,n,ad=arbre
        if k== n:
            return True
        elif k < n:
            return arbre_recherche(ag,k)
        elif k>n:
            return arbre_recherche(ad,k)
            
def arbre_insertion(arbre,y):
    if arbre == ():
        return ((),y,())
    ag,n,ad=arbre
    if y < n:
         return (arbre_recherche(ag,y), n ,ad)
    elif y>n:
        return (ag, n ,(ad,y))
    
    
    
abr=arbre_insertion ((),6)
abr=arbre_insertion ((),4)   
abr=arbre_insertion ((),10)
abr=arbre_insertion ((),3)  
abr=arbre_insertion ((),6)
abr=arbre_insertion ((),4)   
abr=arbre_insertion ((),10)
abr=arbre_insertion ((),3) 



def parcours_infixe(arbre):
    if arbre ==():
        return []
    ag,n,ad=arbre
    liste = parcours_infixe(ag)
    liste.append (n)
    liste+= parcours_infixe(ad)
    return liste
    
liste = parcours_infixe(arbre) 


def creer_arbre(liste):
    taille=len(iste)
    if len(liste) ==0:
        return ()
    else:
        lg = liste[:taille//2]
        n= liste[taille//2]
        ld=liste[1+taille //2 :]
        return (creer_arbre(lg),n,creer_abre(ld))

arbre = (
    (
        (((), 4, ()), 2, ((), 5, ())),
        1,
        (
            ((), 6, ()),
            3,
            (
                ((), 8, ()),
                7,
                ((), 9, ((), 10, ()))
            )
        )
    )
)

arbre_30_noeuds = (
    (
        (
            (((), 8, ()), 4, (((), 9, ()), 5, ((), 10, ()))),
            2,
            (((), 11, ()), 6, (((), 12, ()), 7, ((), 13, ())))
        ),
        1,
        (
            (
                (((), 17, ()), 15, (((), 18, ()), 16, ((), 19, ()))),
                3,
                (((), 20, ()), 21, ((), 22, ()))
            ),
            14,
            (
                (((), 25, ()), 23, (((), 26, ()), 24, ((), 27, ()))),
                28,
                ((), 29, ((), 30, ()))
            )
        )
    )
)


abr_30_noeuds = (
    (
        (
            (
                (
                    ((), 1, ()),
                    2,
                    ((), 3, ())
                ),
                4,
                ((), 5, ())
            ),
            6,
            (
                (), 7,
                ((), 8, ())
            )
        ),
        9,
        (
            (
                ((), 10, ()),
                11,
                ((), 12, ())
            ),
            13,
            (
                (), 14,
                ((), 15, ())
            )
        )
    ),
    16,
    (
        (
            (
                (), 17,
                ((), 18, ())
            ),
            19,
            (
                (), 20,
                ((), 21, ())
            )
        ),
        22,
        (
            (
                (), 23,
                (
                    (), 24,
                    ((), 25, ())
                )
            ),
            26,
            (
                ((), 27, ()),
                28,
                (
                    (), 29,
                    ((), 30, ())
                )
            )
        )
    )
)
