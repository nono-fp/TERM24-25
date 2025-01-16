def recherche_motif(motif,texte):
    liste=[]
    for i in range(len(texte)+1-len(motif)):
        test = True
        for j in range(0,len(motif)):
                if texte[i+j] != motif [j]:
                    test=False
        if test :
            liste.append(i)
    return liste
      
