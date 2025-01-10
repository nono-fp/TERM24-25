  
def tri_selection(tab):
    for i in range (len(tab)):
        mini = i
        for j in range(i, len(tab)):
            if tab[j]< tab[mini]:
                mini=j
        tab[i],tab[mini]= tab[mini], tab[i]
    return tab
    
