ls()
rm(list=ls())

#Abro archivo con medias
Datamedias<-read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\DatosMedias.csv")

######Calculo de la mediana de las medias
#LiftoffTime
medianaLiftOff<-median(Datamedias$LiftOffMean) 
#Movetime
medianaMovetime<-median(Datamedias$MoveTimeMean) 
#LiftOffDiff
medianaLiftOffDiff<-median(Datamedias$LiftOffDiffMean) 


########## 1. Analisis de Lift Off Time
####Grupos LiftOff
#Separo los sujetos en grupo A y B, lento y rapido
gruposliftoff<-data.frame(Datamedias$LiftOffMean.Group.1)#Nro de sujeto
gruposliftoff$Media<-Datamedias$LiftOffMean#Media de los LiftOff para el sujeto
gruposliftoff$grupo<-ifelse(as.numeric(gruposliftoff$Media) < medianaLiftOff, 'Grupo A', 'Grupo B')


########## 2. Analisis de Move Time
####Grupos Movetime
#Separo los sujetos en grupo A y B, lento y rapido
gruposMovetime<-data.frame(Datamedias$LiftOffMean.Group.1)#Nro de sujeto
gruposMovetime$Media<-Datamedias$MoveTimeMean#Media de los Move Time para el sujeto
gruposMovetime$grupo<-ifelse(as.numeric(gruposMovetime$Media) < medianaMovetime, 'Grupo A', 'Grupo B')



########## 3. Analisis de Lift Off Diff
####Grupos Lift Off Diff
#Separo los sujetos en grupo A y B, lento y rapido
gruposLiftOffDiff<-data.frame(Datamedias$LiftOffMean.Group.1)#Nro de sujeto
gruposLiftOffDiff$Media<-Datamedias$LiftOffDiffMean#Media de los Move Time para el sujeto
gruposLiftOffDiff$grupo<-ifelse(as.numeric(gruposLiftOffDiff$Media) < medianaLiftOffDiff, 'Grupo A', 'Grupo B')

