# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:53:12 2023

@author: UdeSA
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
#Uf y Uo






mean  = [290,153]#Uf y Uo para A
mean2 = [265,153]#Uf y Uo para B
cov   = [[20,19.66],
         [14.745,15]]  # [[f2,f*O][O*f,O2]]diagonal covariance para A
cov2  = [[20,19.66],
         [14.745,15]]#[[f2,f*O][O*f,O2]]diagonal covariance para A
x,y   = np.random.multivariate_normal(mean, cov, 80).T # Frecuencia y orientacion para A
x2,y2 = np.random.multivariate_normal(mean2, cov2, 80).T # Frecuencia y orientacion para B

#Transformo la Frecuencia en ciclos/grados y la Orientacion
for i in range(len(x)):
    x[i]  =.25+(x[i]/50)
    x2[i] =.25+(x2[i]/50)
    y[i]  = y[i]*(math.pi/500)
    y2[i] = y2[i]*(math.pi/500)
    
plt.plot(x, y, 'x')
plt.plot(x2, y2, 'x')
#Ploteo de orientacion vs frecuencia

plt.axis('equal')
plt.show()