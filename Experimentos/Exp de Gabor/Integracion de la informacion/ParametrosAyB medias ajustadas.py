# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:34:02 2023

@author: UdeSA
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import panda as pd

#Ejemplo con datos del paper

# Define the parameters of the bivariate normal distributions
mean1 = [272, 153]            # Mean values of the first distribution
cov1 = [[4.538, 3.463],         # Covariance matrix of the first distribution
        [3.463, 4.538]]

mean2 = [327, 147]            # Mean values of the second distribution
cov2 = [[4.538, 3.463],         # Covariance matrix of the second distribution
        [3.463, 4.538]]

# Generate random samples from the first distribution
samples1 = np.random.multivariate_normal(mean1, cov1, size=1000)
x1=samples1[:, 0]
y1=samples1[:, 1]

# Generate random samples from the second distribution
samples2 = np.random.multivariate_normal(mean2, cov2, size=1000)
x2=samples2[:, 0]
y2=samples2[:, 1]

# Plot the scatter plots of the samples
plt.scatter(x1, y1, label='Distribution 1')
plt.scatter(x2, y2, label='Distribution 2')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Bivariate Normal Distributions')
plt.legend()
plt.grid(True)
plt.show()


#Transformo la Frecuencia en ciclos/grados y la Orientacion
for i in range(len(x1)):
    x1[i]  =.25+(x1[i]/50)
    x2[i] =.25+(x2[i]/50)
    y1[i]  = y1[i]*(math.pi/500)
    y2[i] = y2[i]*(math.pi/500)
    
#Armo una lista con A repetido 80 veces para agregar a mi dataframe ParametrosA
d = {'Frecuencia': x1, 'Orientacion': y1, 'Categoria': ['A']*80, 'Tecla': ['Left']*80}
df = pd.DataFrame(data=d)
d2 = {'Frecuencia': x2, 'Orientacion': y2, 'Categoria': ['B']*80, 'Tecla': ['Right']*80}
df2 = pd.DataFrame(data=d2)
df3 = df.append(df2)
df3 = df3.sample(frac=1)
df3.to_csv("ParametrosAyB.csv")