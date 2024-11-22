
"""def bin_to_oct(binaire):
    caractere = len(binaire)
    ajout = 8-caractere
    return  "0"*ajout+binaire"""
    

def bin_to_oct1(binaire):
    return  "0"*(8-len(binaire))+binaire



def str_to_bin(texte):
    resultat= ""
    for c in texte:
        binaire=bin(ord(c))
        binaire=bin_to_oct(binaire[2:]) 
        resultat+=binaire
    return resultat
