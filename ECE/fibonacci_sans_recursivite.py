# -*- coding: utf-8 -*-

import time

def fibonacci(n):
    tab = [0,1]

    for i in range (len(tab),n+1):
        
        tab.append(tab[i-1]+tab[i-2])
    return tab[-1]

start = time.time()
fibonacci(10000)
print(time.time()-start)
