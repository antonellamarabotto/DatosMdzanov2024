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
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad\\Analisis por medias\\Move Time")

#Abro los datos que voy a usar
Dataset <-read.csv("MoveTimeNoOutliers.csv")
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
CueDir<-Dataset$CueDirection
SenDir<-Dataset$SentenceDirection
###############Normalidad################3
shapiro.test(MoveTime)
ggplot(mapping = aes(sample = LiftOff)) + stat_qq_point(size = 2)
######## No es normal

hist(Compatibilidad)
boxplot(Compatibilidad)
hist(MoveTime)
boxplot(MoveTime)



##########  ANOVA Move Time ########## 


####### Compatibilidad ########

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
modeloMoveTimeA<-aov(MoveTime~Compatibilidad*GrupoMoveTime*SentenceDur, data=Datafactor)
summary(modeloMoveTimeA)
AovMoveTimeSumSentDur<-summary(modeloMoveTimeA)
capture.output(AovMoveTimeSumSentDur, file="AOV1MoveTimeconSentDur.doc")

Datafactor <- within(Dataset, {
  GrupoMoveTime  <- factor(GrupoMoveTime)
  Compatibilidad  <- factor(Compatibilidad)
})

str(modeloMoveTimeA)
#Tukey
TukeyMovetime<-TukeyHSD(modeloMoveTimeA)

#Indepencia de los residuos

Residuos1<-plot(modeloMovetime1$residuals)
View(Residuos1)
Residuos2<-plot(modeloMovetime2$residuals)
View(Residuos2)
Residuosa<-plot(modeloMoveTimeA$residuals)
View(Residuosa)


###############  ANOVA con Sent Dir y Cue Dir

##Modelo Anova con interaccion
modeloMovetimeA<-aov(MoveTime~CueDir+SenDir+GrupoMoveTime+CueDir*SenDir+CueDir*GrupoMoveTime+SenDir*GrupoMoveTime, data=Datafactor)
summary(modeloMovetimeA)
AovMoveTimeSumA<-summary(modeloMovetimeA)
capture.output(AovMoveTimeSumA, file="AOV1MoveTime1xsentdirxcueDir.doc")


Datafactor <- within(Dataset, {
  GrupoMoveTime  <- factor(GrupoMoveTime)
})

str(modeloMovetimeA)
#Tukey
TukeyMovetime<-TukeyHSD(modeloMovetimeA)



#Modelo 2: Anova sin interaccion de 3 factores
modeloMovetimeB <- update(modeloMovetimeA, . ~ . -CueDir:SenDir:GrupoMoveTime)
summary(modeloMovetimeB)
AovMoveTimeSumB<-summary(modeloMovetimeB)
#capture.output(AovMoveTimeSumB, file="AOV1MoveTime2.doc")

##Modelo Anova con interaccion y sentence duration
modeloMoveTimeC<-aov(MoveTime~SenDir*CueDir*GrupoMoveTime*SentenceDur, data=Dataset)
summary(modeloMoveTimeC)
AovMoveTimeSumSentDur<-summary(modeloMoveTimeC)
capture.output(AovMoveTimeSumSentDur, file="AOV2MoveTimeconSentDur.doc")

#Indepencia de los residuos

Residuos1<-plot(modeloMovetime1$residuals)
View(Residuos1)
Residuos2<-plot(modeloMovetime2$residuals)
View(Residuos2)
Residuosa<-plot(modeloMoveTimeA$residuals)
View(Residuosa)
