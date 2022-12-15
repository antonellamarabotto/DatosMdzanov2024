# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 17:13:47 2022

@author: UdeSA
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:07:19 2021

@author: Antonella
"""
import numpy as np
import pandas as pd
"""
Scritp para generar los parametros de frecuencia y orientacion
de los parches de Gabor segun Maddox 2004. Estoy usando los datos 
de la funcion normal bivariada de ellos.

"""

"""
Categoria A

MUf=200
sigma(f)=60
MUo=125
sigma(o)=9

"""
"""
Creo los parametros de A para la evaluacion

"""
#Uf y Uo
mediasA=[200,125]
#Sigma de f y O
covarA=[[60,0], [0,9]]

A=np.random.multivariate_normal(mediasA, covarA, size=40)

#Transformo la Frecuencia en ciclos/grados
i=0
for i in range(len(A)):
    j=0
    if j%2==0:
        A[i][j]=.25+(A[i][j]/50)
        j+=1
    else:
        continue
    

print(A)

#Armo una lista con A repetido 80 veces para agregar a mi dataframe ParametrosA

lista=[]
for i in range(40):
    lista.append("A")
listaA=pd.DataFrame(lista, columns=["Categoria"])
print(listaA)

ParametrosA=pd.DataFrame(A, columns=['Frecuencia', 'Orientacion'])

#print(type(ParametrosA))#Pandas core dataframe

ParametrosA=pd.concat([ParametrosA, listaA], axis=1)
print(ParametrosA)

ParametrosA.to_csv("ParametrosA.csv")

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

Categoria B:
    
MUf=315
sigma(f)=60
MUo=125
sigma(o)=9

"""
#Uf y Uo
mediasB=[315,125]
#Sigma de f y O
covarB=[[60,0], [0,9]]

B=np.random.multivariate_normal(mediasB, covarB, size=40)

#Transformo la Frecuencia en ciclos/grados
i=0
for i in range(len(B)):
    j=0
    if j%2==0:
        B[i][j]=.25+(B[i][j]/50)
        j+=1
    else:
        continue

#print(B)
ParametrosB=pd.DataFrame(B)

#Armo una lista con B repetido 80 veces para agregar a mi dataframe ParametrosA

lista=[]
for i in range(40):
    lista.append("B")
listaB=pd.DataFrame(lista, columns=["Categoria"])
#print(listaB)

ParametrosB=pd.DataFrame(B, columns=['Frecuencia', 'Orientacion'])

#print(type(ParametrosB))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria B
ParametrosB=pd.concat([ParametrosB, listaB], axis=1)

print(ParametrosB)

ParametrosB.to_csv("ParametrosB.csv")

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
for i in range(40):
    teclaA.append("left")
teclaA=pd.DataFrame(teclaA, columns=["tecla"])

#print(listaB)

#print(type(ParametrosB))#Pandas core dataframe
#Concateno los parametros con lista que dice categoria B
ParametrosA=pd.concat([ParametrosA, teclaA], axis=1)

#Para A
teclaB=[]
for i in range(40):
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