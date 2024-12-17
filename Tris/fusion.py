
import random as rd

liste = [rd.randint(1,10) for _ in range(10)]

[2, 1, 9, 7, 10, 8, 19, 7, 25, 8]


def fusion(l1, l2):
    l = []
    i = 0
    j = 0
    while i < len(l1) or j < len (l2) :
        if i == len(l1):
            l += l2[j:]
            j = len (l2)
        elif j == len(l2):
            l += l1[i:]
            i = len(l1)
        elif l1[i] < l2[j]: 
            l.append(l1[i])
            i += 1
        else: 
            l.append(l2[j])
            j += 1
    return l
    
    
    
    
def tri_fusion(liste):
    if len(liste)<= 1 :
        return liste
    else:
        milieu = len(liste) // 2
        l1 = tri_fusion(liste[:milieu])
        l2= tri_fusion(liste[milieu:])
        return fusion(l1,l2)
