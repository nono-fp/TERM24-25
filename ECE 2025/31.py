def  recherche_motif(motif,texte):
    tab =[] #stocke indices où motif apparait
    for i in range(len(texte)-len(motif)+1) :
        x = 0
        while x<len(motif) and motif[x]==texte[i+x]:
            x+=1
        if x == len(motif):
            tab.append(i)
    return tab


#x-ème caractère du motif est égal au x-ème caractère du texte, à partir de la position i.            
#x atteint la longueur du motif : tous  les caractères du motif ont été trouvés dans le texte à partir de la position i.            
            
assert recherche_motif("ab", "") == []
assert recherche_motif("ab", "cdcdcdcd") == []
assert recherche_motif("ab", "abracadabra") == [0, 7]
assert recherche_motif("ab", "abracadabraab") == [0, 7, 11]        




def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    #si x n'est pas déjà dans les sommets accessibles
    if x not in acc: 
        acc.append(x)
        for y in adj[x]: 
            parcours(adj,y,acc) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x,acc) 
    return acc
