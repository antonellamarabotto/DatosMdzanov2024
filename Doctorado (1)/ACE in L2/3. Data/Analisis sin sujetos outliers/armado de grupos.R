ls()
rm(list=ls())
ls()

####Analisis multifactorial
install.packages("dplyr")
install.packages("readxl")
install.packages("ggpubr")
library(ggpubr)
library(readxl)
library(dplyr)

#Seteo dir de trabajo
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis sin sujetos outliers")

#Abro los datos
Dataset<- read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Datos.csv")

#Saco outlier nro 56 de Lift Off
ID<-Dataset$ptid
no.outliersLiftOff<-subset(Dataset,ID!=456)
write.csv(no.outliersLiftOff, "LiftOffNoOutliers", row.names = FALSE)

#Calculo la media total de Lift Off
MediaLiftoff<-mean(no.outliersLiftOff$LiftOffLatency)
MediaLiftoffDiff<-mean(no.outliersLiftOff$liftOffDiff)

#Abro archivo con medias
Datamedias<-read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\DatosMedias.csv")
#Saco el sujeto 456 de el dataset
DataMediasOutliers<-subset(Datamedias,Datamedias$LiftOffMean.Group.1!=456)
#Mediana lift Off
medianaLiftOff<-median(DataMediasOutliers$LiftOffMean)

#Mediana lift Off Diff
medianaLiftOffDiff<-median(DataMediasOutliers$LiftOffDiffMean)

########## 1. Analisis de Lift Off Time
####Grupos LiftOff
#Separo los sujetos en grupo A y B, lento y rapido
gruposliftoff<-data.frame(DataMediasOutliers$LiftOffMean.Group.1)#Nro de sujeto
gruposliftoff$Media<-DataMediasOutliers$LiftOffMean#Media de los LiftOff para el sujeto
gruposliftoff$grupo<-ifelse(as.numeric(gruposliftoff$Media) < medianaLiftOff, 'Grupo A', 'Grupo B')


########## 3. Analisis de Lift Off Diff
####Grupos Lift Off Diff
#Separo los sujetos en grupo A y B, lento y rapido
gruposLiftOffDiff<-data.frame(DataMediasOutliers$LiftOffMean.Group.1)#Nro de sujeto
gruposLiftOffDiff$Media<-DataMediasOutliers$LiftOffDiffMean#Media de los Move Time para el sujeto
gruposLiftOffDiff$grupo<-ifelse(as.numeric(gruposLiftOffDiff$Media) < medianaLiftOffDiff, 'Grupo A', 'Grupo B')