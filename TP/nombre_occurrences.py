texte = 'Bonjour'

def nombre_occurrences(texte):
    dico={}
    
    for lettre in texte :
        if  lettre in dico:
            dico[lettre] +=1
        else :
            dico[lettre] = 1
    return dico
        
