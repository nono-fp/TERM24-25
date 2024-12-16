import random as rd

liste = [rd.randint(1,10) for _ in range(10)]

[2, 2, 9, 7, 10, 8, 7, 7, 9, 8]


def fusion(l1, l2):
    l = []
    i = 0
    j = 0
    while i < len(l1) and j < len (l2) :
        if i == len(l1):
            l += l2[j:]
            j = len (l2)
        elif j == len(l2):
            l += l1[i:]
            i = len(l1)
        elif l1[i] < l2[i]: 
            l.append(l1[i])
            i += 1
        else: 
            l.append(l2[j])
            j += 1
        return l
