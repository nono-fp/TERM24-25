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

def parcours_infixe(arbre):
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