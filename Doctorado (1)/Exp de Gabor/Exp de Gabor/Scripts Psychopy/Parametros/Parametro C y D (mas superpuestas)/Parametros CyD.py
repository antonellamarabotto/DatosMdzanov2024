# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:18:22 2022

@author: UdeSA
"""

import numpy as np
import pandas as pd
"""
Scritp para generar los parametros de frecuencia y orientacion
de los parches de Gabor segun Maddox 2004. Estoy usando los datos 
de la funcion normal bivariada de ellos.

"""

"""
Categoria C

MUf=200
sigma(f)=60
MUo=125
sigma(o)=9

"""
"""
Creo los parametros de A para la evaluacion

"""
#Uf y Uo
mediasC=[200,125]
#Sigma de f y O
covarC=[[60,0], [0,9]]

C=np.random.multivariate_normal(mediasC, covarC, size=40)

#Transformo la Frecuencia en ciclos/grados
i=0
for i in range(len(C)):
    j=0
    if j%2==0:
        C[i][j]=.25+(C[i][j]/50)
        j+=1
    else:
        continue
    

print(C)

#Armo una lista con A repetido 80 veces para agregar a mi dataframe ParametrosA

lista=[]
for i in range(40):
    lista.append("C")
listaC=pd.DataFrame(lista, columns=["Categoria"])
print(listaC)

ParametrosC=pd.DataFrame(C, columns=['Frecuencia', 'Orientacion'])

#print(type(ParametrosA))#Pandas core dataframe

ParametrosC=pd.concat([ParametrosC, listaC], axis=1)
print(ParametrosC)

ParametrosC.to_csv("ParametrosC.csv")

"""
Creo los parametros de C para el testeo

"""
testC=np.random.multivariate_normal(mediasC, covarC, size=10)

#Transformo la Frecuencia en ciclos/grados
i=0
for i in range(len(testC)):
    j=0
    if j%2==0:
        testC[i][j]=.25+(testC[i][j]/50)
        j+=1
    else:
        continue
listaC=[]
for i in range(10):
    listaC.append("C")
listaC=pd.DataFrame(listaC, columns=["Categoria"])
print(listaC)

ParametrosCtest=pd.DataFrame(testC, columns=['Frecuencia', 'Orientacion'])

#print(type(ParametrosA))#Pandas core dataframe

ParametrosCtest=pd.concat([ParametrosCtest, listaC], axis=1)
print(ParametrosCtest)

ParametrosCtest.to_csv("ParametrosCtest.csv")    


"""

Categoria D:
    
MUf=290
sigma(f)=60
MUo=125
sigma(o)=9

"""
#Uf y Uo
mediasD=[290,125]
#Sigma de f y O
covarD=[[60,0], [0,9]]

D=np.random.multivariate_normal(mediasD, covarD, size=40)

#Transformo la Frecuencia en ciclos/grados
i=0
for i in range(len(D)):
    j=0
    if j%2==0:
        D[i][j]=.25+(D[i][j]/50)
        j+=1
    else:
        continue

#print(B)
ParametrosD=pd.DataFrame(D)

#Armo una lista con D repetido 80 veces para agregar a mi dataframe ParametrosD

lista=[]
for i in range(40):
    lista.append("D")
listaD=pd.DataFrame(lista, columns=["Categoria"])
#print(listaB)

ParametrosD=pd.DataFrame(D, columns=['Frecuencia', 'Orientacion'])

#print(type(ParametrosB))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria B
ParametrosD=pd.concat([ParametrosD, listaD], axis=1)

print(ParametrosD)

ParametrosD.to_csv("ParametrosD.csv")

"""
Creo los parametros D para el testeo
"""
testD=np.random.multivariate_normal(mediasD, covarD, size=10)

#Transformo la Frecuencia en ciclos/grados
i=0
for i in range(len(testD)):
    j=0
    if j%2==0:
        testD[i][j]=.25+(testD[i][j]/50)
        j+=1
    else:
        continue

#print(B)
ParametrosDtest=pd.DataFrame(testD)

#Armo una lista con B repetido 80 veces para agregar a mi dataframe ParametrosD

lista=[]
for i in range(10):
    lista.append("D")
listaDtest=pd.DataFrame(lista, columns=["Categoria"])
#print(listaB)

ParametrosDtest=pd.DataFrame(testD, columns=['Frecuencia', 'Orientacion'])

#print(type(ParametrosD))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria D
ParametrosDtest=pd.concat([ParametrosDtest, listaDtest], axis=1)

print(ParametrosDtest)

ParametrosDtest.to_csv("ParametrosDtest.csv")


"""
Al archivo de parametros C le agrego las columnas left, y right a D
"""
#Para A
teclaC=[]
for i in range(40):
    teclaC.append("left")
teclaC=pd.DataFrame(teclaC, columns=["tecla"])

#print(listaB)

#print(type(ParametrosB))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria B
ParametrosC=pd.concat([ParametrosC, teclaC], axis=1)

#Para D
teclaD=[]
for i in range(40):
    teclaD.append("right")
teclaD=pd.DataFrame(teclaD, columns=["tecla"])
ParametrosD=pd.concat([ParametrosD, teclaD], axis=1)

"""
Armo un archivo csv que contenga frecuencia, orientacion y 
categoria tanto C como D

"""

frames=[ParametrosC, ParametrosD]

ParametrosCyD=pd.concat(frames)

print(ParametrosCyD)


ParametrosCyD.to_csv("ParametrosCyD.csv")



"""
En el testeo repito:
Al archivo de parametros C le agrego las columnas left, y right a D
"""
#Para A
teclaC=[]
for i in range(10):
    teclaC.append("left")
teclaC=pd.DataFrame(teclaC, columns=["tecla"])

#print(listaB)

#print(type(ParametrosB))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria B
ParametrosCtest=pd.concat([ParametrosCtest, teclaC], axis=1)

#Para A
teclaD=[]
for i in range(10):
    teclaD.append("right")
teclaD=pd.DataFrame(teclaD, columns=["tecla"])
ParametrosDtest=pd.concat([ParametrosDtest, teclaD], axis=1)

"""
Armo un archivo csv que contenga frecuencia, orientacion y 
categoria tanto A como B

"""

frames=[ParametrosCtest, ParametrosDtest]

ParametrosCyDtest=pd.concat(frames)

print(ParametrosCyDtest)


ParametrosCyDtest.to_csv("ParametrosCyDtest.csv")