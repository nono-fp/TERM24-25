
def multiplication(n1,n2):
    resultat = 0
    for i in range (abs(n1)):
        resultat += abs(n2) 
    return resultat
    if (n1 >0 and n2 > 0) or (n1< 0 and n2 < 0) :
        return resultat
    else:
        return -resultat
    
    
"""EXERCICE 2"""

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab,
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, i , m-1)
    elif tab[m] > x:
        return chercher(tab, x, m+1 , j)
    else:
        return m
