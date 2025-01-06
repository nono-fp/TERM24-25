
def recherche(tab, n):
    result = -1
    for i in range(len(tab)) : 
      if n == tab[i]:
          result = i
    return result
      


def recherche2(tab, n):
    for i in range (len(tab)):
        if n == tab[i]:
            return i
    return -1



def moyenne(tab):
    somme = 0
    moyenne= 0
    for n,c in tab:
        somme += c
        moyenne += c*n
    return (moyenne/somme)
