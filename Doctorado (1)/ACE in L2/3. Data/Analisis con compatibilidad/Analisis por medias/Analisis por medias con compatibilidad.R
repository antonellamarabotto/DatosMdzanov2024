# Analisis de datos incorporando compatibilidad en lugar de Sentence dir y cue dir

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
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad")

#Abro los datos que voy a usar
Dataset <-read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad\\DatosCompatibilidad.csv")
Dataset$Compatibilidad <- as.integer(Dataset$Compatibilidad) 

#Nombro las variables
LiftOff<-Dataset$LiftOffLatency
MoveTime<-Dataset$MoveTime
LiftOffDiff<-Dataset$liftOffDiff
Individuo<-Dataset$ptid
Compatibilidad<-Dataset$Compatibilidad
GrupoLiftOff<-Dataset$Grupo.Lift.Off
GrupoLiftOffDiff<-Dataset$Grupo.Lift.Off.Diff
GrupoMoveTime<-Dataset$Grupo.MoveTime
SentenceDur<-Dataset$SentDur
###############Normalidad################3

######## No es normal

hist(Compatibilidad)
boxplot(Compatibilidad)


##########  ANOVA Lift Off Latency ########## 
##Modelo Anova con interaccion
modelo1<-aov(LiftOff~Compatibilidad*GrupoLiftOff, data=Dataset)
summary(modelo1)
AovLiftOFFSum<-summary(modelo1)
capture.output(AovLiftOFFSum, file="AOV1LiftOff.doc")

#Modelo 2: Anova sin interaccion de 3 factores
Modelo2 <- update(modelo1, . ~ . -Compatibilidad:Grupo)
summary(Modelo2)

##Modelo Anova con interaccion y sentence duration
modeloa<-aov(LiftOff~Compatibilidad*GrupoLiftOff*SentenceDur, data=Dataset)
summary(modeloa)
AovLiftOFFSumSentDur<-summary(modeloa)
capture.output(AovLiftOFFSumSentDur, file="AOV1LiftOffconSentDur.doc")

#Indepencia de los residuos

Residuos1<-plot(modelo1$residuals)
View(Residuos1)
Residuos2<-plot(Modelo2$residuals)
View(Residuos2)
Residuosa<-plot(modeloa$residuals)
View(Residuosa)


##########  ANOVA Move Time ########## 
##Modelo Anova con interaccion
modeloMovetime1<-aov(MoveTime~Compatibilidad*GrupoMoveTime, data=Dataset)
summary(modeloMovetime1)
AovMoveTimeSum1<-summary(modeloMovetime1)
capture.output(AovMoveTimeSum1, file="AOV1MoveTime1.doc")

#Modelo 2: Anova sin interaccion de 3 factores
modeloMovetime2 <- update(modeloMovetime1, . ~ . -Compatibilidad:GrupoMoveTime)
summary(modeloMovetime2)
AovMoveTimeSum2<-summary(modeloMovetime2)
capture.output(AovMoveTimeSum2, file="AOV1MoveTime2.doc")

##Modelo Anova con interaccion y sentence duration
modeloMoveTimeA<-aov(MoveTime~Compatibilidad*GrupoMoveTime*SentenceDur, data=Dataset)
summary(modeloMoveTimeA)
AovMoveTimeSumSentDur<-summary(modeloMoveTimeA)
capture.output(AovMoveTimeSumSentDur, file="AOV1MoveTimeconSentDur.doc")

#Indepencia de los residuos

Residuos1<-plot(modeloMovetime1$residuals)
View(Residuos1)
Residuos2<-plot(modeloMovetime2$residuals)
View(Residuos2)
Residuosa<-plot(AovMoveTimeSumSentDur$residuals)
View(Residuosa)
