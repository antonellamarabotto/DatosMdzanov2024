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
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad\\Analisis por tertiles\\Lift Off Difference")

#Abro los datos que voy a usar
Dataset <-read.csv("LiftOffDiffNoOutliers.csv")
Dataset$Compatibilidad <- as.integer(Dataset$Compatibilidad) 

#Nombro las variables
LiftOff<-Dataset$LiftOffLatency
MoveTime<-Dataset$MoveTime
LiftOffDiff<-Dataset$liftOffDiff
Individuo<-Dataset$ptid
Compatibilidad<-Dataset$Compatibilidad
GrupoLiftOffDiff<-Dataset$Grupo.Lift.Off.Diff
GrupoMoveTime<-Dataset$Grupo.MoveTime
SentenceDur<-Dataset$SentDur
CueDir<-Dataset$CueDirection
SenDir<-Dataset$SentenceDirection
###############Normalidad################3

hist(Compatibilidad)
boxplot(Compatibilidad)
hist(LiftOffDiff)
boxplot(LiftOffDiff)


##########  ANOVA Lift Off Latency ########## 


####### Compatibilidad ########

##Modelo Anova con interaccion
modeloLiftOffDiff1<-aov(LiftOffDiff~Compatibilidad*GrupoLiftOffDiff, data=Dataset)
summary(modeloLiftOffDiff1)
AovLiftOffDiffSum1<-summary(modeloLiftOffDiff1)
capture.output(AovLiftOffDiffSum1, file="AovLiftOffDiffSum1.doc")

#Modelo 2: Anova sin interaccion de 3 factores
modeloLiftOffDiff2 <- update(modeloLiftOffDiff1, . ~ . -Compatibilidad:GrupoLiftOffDiff)
summary(modeloLiftOffDiff2)
AovLiftOffDiffSum2<-summary(modeloLiftOffDiff2)
capture.output(AovLiftOffDiffSum2, file="AOV1LiftOffDiff2.doc")

##Modelo Anova con interaccion y sentence duration
modeloLiftOffDiffA<-aov(LiftOffDiff~Compatibilidad*GrupoLiftOffDiff*SentenceDur, data=Dataset)
summary(modeloLiftOffDiffA)
AovLiftOffDiffSumSentDur<-summary(modeloLiftOffDiffA)
capture.output(AovLiftOffDiffSumSentDur, file="AovLiftOffDiffSumSentDurA.doc")

#Indepencia de los residuos

Residuos1<-plot(modeloLiftOffDiff1$residuals)
View(Residuos1)
Residuos2<-plot(modeloLiftOffDiff2$residuals)
View(Residuos2)
Residuosa<-plot(modeloLiftOffDiffA$residuals)
View(Residuosa)


###############  ANOVA con Sent Dir y Cue Dir


##Modelo Anova con interaccion
SenDir<-as.character(SenDir)
modeloLiftOffDiffAsentDir<-aov(LiftOffDiff~SenDir*CueDir*GrupoLiftOffDiff, data=Dataset)
summary(modeloLiftOffDiffAsentDir)
LiftOffDiffAsentDir<-summary(modeloLiftOffDiffAsentDir)
capture.output(LiftOffDiffAsentDir, file="AovLiftOffDiffAsentDir.doc")


#Testeo de componentes principales con Tukey
TukeyHSD(modeloLiftOffDiffAsentDir, which = "GrupoLiftOffDiff")

TukeyHSD(modeloLiftOffDiffAsentDir, which = "SenDir")

with(Dataset, interaction.plot(GrupoLiftOffDiff, SenDir, LiftOffDiff, fun = mean,
                               main = "Interaction Plot"))


with(Dataset, interaction.plot(CueDir, SenDir, LiftOff, fun = mean,
                               main = "Interaction Plot"))

with(Dataset, interaction.plot(SentenceDur, SenDir, LiftOff, fun = mean,
                               main = "Interaction Plot"))

#Modelo 2: Anova sin interaccion de 3 factores
modeloLiftOffDiffAsentDir2<- update(modeloLiftOffDiffAsentDir, . ~ . -CueDir:SenDir:GrupoLiftOffDiff)
summary(modeloLiftOffDiffAsentDir2)
AovLiftOffDiffsentDirSum2<-summary(modeloLiftOffDiffAsentDir2)
capture.output(AovLiftOffDiffsentDirSum2, file="AOV1LiftOffDiffSenDir2.doc")

##Modelo Anova con interaccion y sentence duration
modeloLiftOffDiffAsentDirSenDurA<-aov(LiftOffDiff~SenDir*CueDir*GrupoLiftOffDiff*SentenceDur, data=Dataset)
summary(modeloLiftOffDiffAsentDirSenDurA)
AovLiftOffDiffAsentDirSenDurA<-summary(modeloLiftOffDiffAsentDirSenDurA)
capture.output(AovLiftOffDiffAsentDirSenDurA, file="AovLiftOffDiffSumSentDurSenDirA.doc")


#Indepencia de los residuos

Residuos1<-plot(modeloLiftOffDiffAsentDir$residuals)
View(Residuos1)
Residuos2<-plot(modeloLiftOffDiffAsentDir2$residuals)
View(Residuos2)
Residuosa<-plot(modeloLiftOffDiffAsentDirSenDurA$residuals)
View(Residuosa)
