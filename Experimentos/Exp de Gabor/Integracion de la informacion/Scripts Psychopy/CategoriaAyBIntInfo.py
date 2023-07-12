# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:59:26 2022

@author: UdeSA


Categoria A y B para integracion de la informacion

""""""
Categoria A

MUf=272
sigma(f)=4,538
MUo=153
sigma(o)=4,538

"""
"""
Creo los parametros de A para la evaluacion

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
#Uf y Uo






mean  = [272,153]#Uf y Uo para A
mean2 = [327,120]#Uf y Uo para B
cov   = [[4.538,4.463], [4.463,4.538]]  # [[f2,f*O][O*f,O2]]diagonal covariance para A
cov2  = [[4.538,4.463], [4.463,4.538]]#[[f2,f*O][O*f,O2]]diagonal covariance para A
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

#Armo una lista con A repetido 80 veces para agregar a mi dataframe ParametrosA
d = {'Frecuencia': x, 'Orientacion': y, 'Categoria': ['A']*80, 'Tecla': ['Left']*80}
df = pd.DataFrame(data=d)
d2 = {'Frecuencia': x2, 'Orientacion': y2, 'Categoria': ['B']*80, 'Tecla': ['Right']*80}
df2 = pd.DataFrame(data=d2)
df3 = df.append(df2)
df3 = df3.sample(frac=1)
df3.to_csv("ParametrosAyBintinfo.csv")





"""
Creo los parametros de A para el testeo

"""
testA=np.random.multivariate_normal(mediasA, covarA, size=10)

#Transformo la Frecuencia en ciclos/grados
i=0
for i in range(len(testA)):
    j=0
    if j%2==0:
        testA[i][j]=.25+(testA[i][j]/50)
        j+=1
    else:
        continue
listaA=[]
for i in range(10):
    listaA.append("A")
listaA=pd.DataFrame(listaA, columns=["Categoria"])
print(listaA)

ParametrosAtest=pd.DataFrame(testA, columns=['Frecuencia', 'Orientacion'])

#print(type(ParametrosA))#Pandas core dataframe

ParametrosAtest=pd.concat([ParametrosAtest, listaA], axis=1)
print(ParametrosAtest)

ParametrosAtest.to_csv("ParametrosAtest.csv")    




"""
Creo los parametros B para el testeo
"""
testB=np.random.multivariate_normal(mediasB, covarB, size=10)

#Transformo la Frecuencia en ciclos/grados
i=0
for i in range(len(testB)):
    j=0
    if j%2==0:
        testB[i][j]=.25+(testB[i][j]/50)
        j+=1
    else:
        continue

#print(B)
ParametrosBtest=pd.DataFrame(testB)

#Armo una lista con B repetido 80 veces para agregar a mi dataframe ParametrosA

lista=[]
for i in range(10):
    lista.append("B")
listaBtest=pd.DataFrame(lista, columns=["Categoria"])
#print(listaB)

ParametrosBtest=pd.DataFrame(testB, columns=['Frecuencia', 'Orientacion'])

#print(type(ParametrosB))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria B
ParametrosBtest=pd.concat([ParametrosBtest, listaBtest], axis=1)

print(ParametrosBtest)

ParametrosBtest.to_csv("ParametrosBtest.csv")


"""
Al archivo de parametros A le agrego las columnas left, y right a B
"""
#Para A
teclaA=[]
for i in range(80):
    teclaA.append("left")
teclaA=pd.DataFrame(teclaA, columns=["tecla"])

#print(listaB)

#print(type(ParametrosB))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria B
ParametrosA=pd.concat([ParametrosA, teclaA], axis=1)

#Para B
teclaB=[]
for i in range(80):
    teclaB.append("right")
teclaB=pd.DataFrame(teclaB, columns=["tecla"])
ParametrosB=pd.concat([ParametrosB, teclaB], axis=1)

"""
Armo un archivo csv que contenga frecuencia, orientacion y 
categoria tanto A como B

"""

frames=[ParametrosA, ParametrosB]

ParametrosAyB=pd.concat(frames)

print(ParametrosAyB)


ParametrosAyB.to_csv("ParametrosAyB.csv")



"""
En el testeo repito:
Al archivo de parametros A le agrego las columnas left, y right a B
"""
#Para A
teclaA=[]
for i in range(10):
    teclaA.append("left")
teclaA=pd.DataFrame(teclaA, columns=["tecla"])

#print(listaB)

#print(type(ParametrosB))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria B
ParametrosAtest=pd.concat([ParametrosAtest, teclaA], axis=1)

#Para A
teclaB=[]
for i in range(10):
    teclaB.append("right")
teclaB=pd.DataFrame(teclaB, columns=["tecla"])
ParametrosBtest=pd.concat([ParametrosBtest, teclaB], axis=1)

"""
Armo un archivo csv que contenga frecuencia, orientacion y 
categoria tanto A como B

"""

frames=[ParametrosAtest, ParametrosBtest]

ParametrosAyBtest=pd.concat(frames)

print(ParametrosAyBtest)


ParametrosAyBtest.to_csv("ParametrosAyBtest.csv")