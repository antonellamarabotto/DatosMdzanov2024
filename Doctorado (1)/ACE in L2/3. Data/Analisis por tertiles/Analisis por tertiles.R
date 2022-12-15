#Anova de Grupos por tertiles
ls()
rm(list=ls())
ls()

install.packages("dplyr")
install.packages("readxl")
library(readxl)
library(dplyr)

#Directorio de trabajo: Analisis por tertiles
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis por tertiles")
#Dataset
DatosTertiles<-read.csv("GruposTertiles.csv")

#Nombro las variables
MoveTime<-DatosTertiles$MoveTime
Individuo<-DatosTertiles$ptid
CueDirection<-DatosTertiles$CueDirection
SentenceDirection<-DatosTertiles$SentenceDirection
GrupoLiftOff<-DatosTertiles$Grupo.Lift.Off
LiftOff<-DatosTertiles$LiftOffLatency
GrupoMoveTime<-DatosTertiles$Grupo.Move.Time
MoveTime<-DatosTertiles$MoveTime
LiftOffDiff<-DatosTertiles$liftOffDiff
GrupoLiftOffDiff<-DatosTertiles$Grupo.Lift.Off.Diff
SentenceDuration<-DatosTertiles$SentDur

#Proporciones

DatosTertiles %>% group_by(Grupo.Lift.Off) %>% tally()
DatosTertiles %>% group_by(Grupo.Lift.Off.Diff) %>% tally()
DatosTertiles %>% group_by(Grupo.Move.Time) %>% tally()


AovLiftOff<-aov(LiftOff~GrupoLiftOff, data=DatosTertiles)
summary(AovLiftOff)
TukeyHSD(AovLiftOff)###Todos los grupos son diferentes

AovMoveTime<-aov(MoveTime~GrupoMoveTime, data=DatosTertiles)
summary(AovMoveTime)
TukeyHSD(AovMoveTime)###Todos los grupos son diferentes

AovLiftOffDiff<-aov(LiftOffDiff~GrupoLiftOffDiff, data=DatosTertiles)
summary(AovLiftOffDiff)
TukeyHSD(AovLiftOffDiff)###Todos los grupos son diferentes


####Boxplots

#Boxplot LiftOff

boxplot(LiftOff ~ GrupoLiftOff , col = c("blue", "green","red"), ylab = "Lift Off Latency")
png(filename = "BoxplotLiftOff.png", width = 800, height = 600)

#Boxplot Lift Off Diff

boxplot(LiftOffDiff ~ GrupoLiftOffDiff , col = c("blue", "green","red"), ylab = "Lift Off Difference")
png(filename = "BoxplotLiftOffDiff.png", width = 800, height = 600)

#Boxplot Move Time

boxplot(MoveTime ~ GrupoMoveTime , col = c("blue", "green","red"), ylab = "Lift Off Difference")
png(filename = "BoxplotMoveTime.png", width = 800, height = 600)


##############Modelo Anova con interaccion MoveTime######################
#Movelo 1: Anova de 3 factores con interaccion: Las variables explicatorias son Sentence Direction, Grupo, y Cue Direction
modelo1MoveTime<-aov(MoveTime~CueDirection*SentenceDirection*GrupoMoveTime, data=DatosTertiles)
summary(modelo1MoveTime)
Aov1MoveTime<-summary(modelo1MoveTime)
capture.output(Aov1MoveTime, file="AOV1MoveTime.doc")

#Modelo 2: Anova sin interaccion de 3 factores
Modelo2MoveTime<-update(modelo1MoveTime, . ~ . -CueDirection:SentenceDirection:GrupoMoveTime)
summary(Modelo2MoveTime)
Aov2MoveTime<-summary(Modelo2MoveTime)
capture.output(Aov2MoveTime, file="AOV2MoveTime.doc")

#Es igual al primer modelo

##Modelo 3: Anova sin interaccion
Modelo3MoveTime <- update(Modelo2MoveTime, .~CueDirection+SentenceDirection+GrupoMoveTime)
summary(Modelo3MoveTime)
Aov3MoveTime<-summary(Modelo3MoveTime)
capture.output(Aov3MoveTime, file="AOV3MoveTime.doc")

#Es igual al modelo anterior. Vamos a corroborarlo comparandolos.
anova(Modelo2MoveTime,Modelo3MoveTime)
#Son iguales.

#####Incorporo Sentence Duration como factor
#Movelo 1: Anova de 3 factores con interaccion: Las variables explicatorias son Sentence Direction, Grupo, y Cue Direction
modeloAMoveTime<-aov(MoveTime~CueDirection*SentenceDirection*GrupoMoveTime*SentenceDuration, data=DatosTertiles)
summary(modeloAMoveTime)
AovAMoveTime<-summary(modeloAMoveTime)
capture.output(AovAMoveTime, file="AOVAMoveTime.doc")

#Modelo 2: Anova sin interaccion de 3 factores
ModeloBMoveTime<-update(modeloAMoveTime, . ~ . -CueDirection:SentenceDirection:GrupoMoveTime:SentenceDuration)
summary(ModeloBMoveTime)

AovBMoveTime<-summary(ModeloBMoveTime)
capture.output(AovBMoveTime, file="AOVBMoveTime.doc")

#Es igual al primer modelo

##Modelo 3: Anova sin interaccion
ModeloCMoveTime <- update(ModeloBMoveTime, .~CueDirection+SentenceDirection+GrupoMoveTime+SentenceDuration)
summary(ModeloCMoveTime)
AovCMoveTime<-summary(ModeloCMoveTime)
capture.output(AovCMoveTime, file="AOVCMoveTime.doc")

#Es igual al modelo anterior. Vamos a corroborarlo comparandolos.
anova(ModeloCMoveTime,ModeloBMoveTime)
#Son iguales.

#################Modelo Anova con interaccion LiftOff####################

Modelo1LiftOff<-aov(LiftOff~CueDirection*SentenceDirection*GrupoLiftOff, data=DatosTertiles)
summary(Modelo1LiftOff)
Aov1LiftOff<-summary(Modelo1LiftOff)
capture.output(Aov1LiftOff, file="AOV1LiftOff.doc")

#Modelo 2: Anova sin interaccion de 3 factores
Modelo2LiftOff<-update(Modelo1LiftOff, . ~ . -CueDirection:SentenceDirection:GrupoLiftOff)
summary(Modelo2LiftOff)
Aov2LiftOff<-summary(Modelo2LiftOff)
capture.output(Aov2LiftOff, file="AOV2LiftOff.doc")

#Es igual al primer modelo

##Modelo 3: Anova sin interaccion
Modelo3LiftOff <- update(Modelo2LiftOff, .~CueDirection+SentenceDirection+GrupoLiftOff)
summary(Modelo3LiftOff)
Aov3LiftOff<-summary(Modelo3LiftOff)
capture.output(Aov3LiftOff, file="AOV3LiftOff.doc")

#Es igual al modelo anterior. Vamos a corroborarlo comparandolos.
anova(Modelo2LiftOff,Modelo3LiftOff)
anova(Modelo1LiftOff,Modelo3LiftOff)
anova(Modelo2LiftOff,Modelo1LiftOff)

#Son iguales.

#######Incorporo Sentence Duration como factor
ModeloALiftOff<-aov(LiftOff~CueDirection*SentenceDirection*GrupoLiftOff*SentenceDuration, data=DatosTertiles)
summary(ModeloALiftOff)
AovALiftOff<-summary(ModeloALiftOff)
capture.output(AovALiftOff, file="AOVALiftOff.doc")

#####Hay interaccion entre sentence Direction y Sentence Duracion y entre Cue direction y sentence Direction

ModeloBLiftOff<-update(ModeloALiftOff, . ~ . -CueDirection:SentenceDirection:GrupoLiftOff:SentenceDuration)
summary(ModeloALiftOff)

anova(ModeloBLiftOff, ModeloALiftOff)


#################Modelo Anova con interaccion LiftOffDiff####################

Modelo1LiftOffDiff<-aov(LiftOffDiff~CueDirection*SentenceDirection*GrupoLiftOffDiff, data=DatosTertiles)
summary(Modelo1LiftOffDiff)
Aov1LiftOffDiff<-summary(Modelo1LiftOffDiff)
capture.output(Aov1LiftOffDiff, file="AOV1LiftOffDiff.doc")

###
#Modelo 2: Anova sin interaccion de 3 factores
Modelo2LiftOffDiff<-update(Modelo1LiftOffDiff, . ~ . -CueDirection:SentenceDirection:GrupoLiftOffDiff)
summary(Modelo2LiftOffDiff)

Aov2LiftOffDiff<-summary(Modelo2LiftOffDiff)
capture.output(Aov2LiftOffDiff, file="AOV2LiftOffDiff.doc")
#Es igual al primer modelo

##Modelo 3: Anova sin interaccion
Modelo3LiftOffDiff <- update(Modelo2LiftOffDiff, .~CueDirection+SentenceDirection+GrupoLiftOffDiff)
summary(Modelo3LiftOffDiff)
Aov3LiftOffDiff<-summary(Modelo3LiftOffDiff)
capture.output(Aov3LiftOffDiff, file="AOV3LiftOffDiff.doc")

#Es igual al modelo anterior. Vamos a corroborarlo comparandolos.
anova(Modelo2LiftOffDiff,Modelo3LiftOffDiff)
anova(Modelo1LiftOffDiff,Modelo3LiftOffDiff)
anova(Modelo2LiftOffDiff,Modelo1LiftOffDiff)

#Son iguales.

####Incorpor sentence Duration como factor
ModeloALiftOffDiff<-aov(LiftOffDiff~CueDirection*SentenceDirection*GrupoLiftOffDiff*SentenceDuration, data=DatosTertiles)
summary(ModeloALiftOffDiff)
AovALiftOffDiff<-summary(ModeloALiftOffDiff)
capture.output(AovALiftOffDiff, file="AOVALiftOffDiff.doc")

###Hay efecto de grupo, Sentence Duration, e interaccion Sentence Direction con sentence Duration
