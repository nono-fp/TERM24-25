# -*- coding: utf-8 -*-
"""
Terminale
Faivre-Pierret Noémie
TP 06
"""


def bin_to_oct(binaire):
    return  "0"*(8-len(binaire))+binaire



def str_to_bin(texte):
    resultat= ""
    for c in texte:
        binaire=bin(ord(c))
        binaire=bin_to_oct(binaire[2:]) 
        resultat+=binaire
    return resultat


def bin_to_str(binaire):
    texte = ""
    for i in range (0,len(binaire),8):
        octet = binaire[i:i+8]
        caractere= chr(int(octet,2))
        texte+=caractere
    return texte

def xor (a,b):
    return "1" if a!=b else "0"



def chiff_sym_bin(message,cle):
    cle_complete =cle *( len(message)//len(cle) +1)
    
    resultat =""
    for i in range (len(message)):
        resultat += xor(message[i],cle_complete[i])
    return resultat


def chiff_sym (message, cle):
    message_bin = str_to_bin (message)
    cle_bin=str_to_bin(cle)
    resultat_bin = chiff_sym_bin(message_bin,cle_bin)
    return bin_to_str(resultat_bin)
