def moyenne(notes):
    somme_note_coeff = 0
    somme_coeff = 0
    
    for n,c in notes:
        somme_coeff+= c
        somme_note_coeff += n*c
                
        if somme_coeff == 0:
            return None
    
        m = somme_note_coeff/somme_coeff
    return m



coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
        des "*" , les 0 par un espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart,k):
    '''renvoie une liste contenant k fois chaque élément de
       liste_depart'''
    liste_zoomee = []
    for elt in liste_depart : 
        for i in range(k):
            liste_zoomee.append(elt) #on ajoute dans la liste les éléments
            liste_zoomee*i #chaque élément est ajoutés k fois
    return liste_zoomee

def dessin_zoom(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois 
       ET répétées k fois'''
    grille_zoomee=[]
    for ligne in grille: # pour chaque ligne de la grille
        ligne_zoomee = liste_zoom(ligne,k) #on zoom la ligne * k
        for i in range(k):
            grille_zoomee .append(ligne_zoomee) #la ligne est répétée k fois
    return grille_zoomee
