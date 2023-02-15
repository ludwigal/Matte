# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 08:57:47 2023

"""

import numpy as np
landvetter = 1/3
centralen = 1/3
uthyrning = 1/3

b=np.array([centralen,landvetter,uthyrning]) #Vn vektorn

for i in range(100):
    v = np.array([[0.7,0.1,0.3],[0.1,0.6,0.2],[0.2,0.3,0.5]]) #Matris från teoriuppgift 2. Rad 1 är ändringen på centralens antal bilar 
    #KOLUMN 1 är procent fördelningen av centralensbilar från en vecka till nästa. Osv
    b = np.matmul(v,b) #Matrismultiplikation
print(b)