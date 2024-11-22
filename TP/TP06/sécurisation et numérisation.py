
"""def bin_to_oct(binaire):
    caractere = len(binaire)
    ajout = 8-caractere
    return  "0"*ajout+binaire"""
    

def bin_to_oct1(binaire):
    return  "0"*(8-len(binaire))+binaire



def str_to_bin(texte):
    for c in "texte" :
        nbr = ord(c)
        binaire=bin(nbr)
        return binaire[2:]
