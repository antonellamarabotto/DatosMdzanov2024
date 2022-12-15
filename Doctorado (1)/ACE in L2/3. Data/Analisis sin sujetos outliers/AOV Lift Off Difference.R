#Analisis de Lift Off Latency sin sujeto outlier numero 56

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


#Abro los datos que voy a usar
Dataset <-read.csv("LiftOffDiffNOOutrliers.csv")
#Agrego compatibilidad
Dataset$Compatibilidad <- ifelse(Dataset$CueDirection>Dataset$SentenceDirection, 0,
                                 ifelse(Dataset$CueDirection < Dataset$SentenceDirection, 0, 1))


Dataset$Compatibilidad <- as.integer(Dataset$Compatibilidad) 

#Nombro las variables
LiftOff<-Dataset$LiftOffLatency
MoveTime<-Dataset$MoveTime
LiftOffDiff<-Dataset$liftOffDiff
Individuo<-Dataset$ptid
Compatibilidad<-Dataset$Compatibilidad
GrupoLiftOff<-Dataset$Grupo
GrupoLiftOffDiff<-Dataset$Grupo.Lift.Off.Diff

SentenceDur<-Dataset$SentDur
CueDir<-Dataset$CueDirection
SenDir<-Dataset$SentenceDirection


###############Normalidad################3
shapiro.test(LiftOffDiff)
ggplot(mapping = aes(sample = LiftOffDiff)) + stat_qq_point(size = 2)

######## No es normal

hist(LiftOffDiff)
boxplot(LiftOffDiff)


####### Compatibilidad ########

##Modelo Anova con interaccion:      LiftOff~Compatibilidad*GrupoLiftOff
modeloLiftOffDiff1<-aov(LiftOffDiff~Compatibilidad*GrupoLiftOffDiff, data=Dataset)
summary(modeloLiftOffDiff1)
AovLiftOffDiffSum1<-summary(modeloLiftOffDiff1)
capture.output(AovLiftOffDiffSum1, file="AovLiftOffDiffSum1.doc")

#Modelo 2: Anova sin interaccion de 3 factores
modeloLiftOffDiff2 <- update(modeloLiftOffDiff1, . ~ . -Compatibilidad:GrupoLiftOffDiff)
summary(modeloLiftOffDiff2)
AovLiftOff2<-summary(modeloLiftOffDiff2)
capture.output(AovLiftOff2, file="AOVLiftOff2.doc")

##Modelo Anova con interaccion:  LiftOff~Compatibilidad*GrupoLiftOff*SentenceDur
modeloLiftOffDiffA<-aov(LiftOffDiff~Compatibilidad*GrupoLiftOffDiff*SentenceDur, data=Dataset)
summary(modeloLiftOffDiffA)
AovLiftOffSentDur<-summary(modeloLiftOffA)
capture.output(AovLiftOffSentDur, file="AOV1LiftOffconSentDur.doc")

#Indepencia de los residuos


Residuos1<-plot(modeloLiftOff1$residuals)
View(Residuos1)
Residuos2<-plot(modeloLiftOff2$residuals)
View(Residuos2)
Residuosa<-plot(modeloLiftOffA$residuals)
View(Residuosa)


###############  ANOVA con Sent Dir y Cue Dir

##Modelo Anova con interaccion:  LiftOff~CueDir*SenDir*GrupoLiftOff

SenDir<-as.character(SenDir)
modeloLiftOffDiffxDirA<-aov(LiftOffDiff~CueDir*SenDir*GrupoLiftOffDiff, data=Dataset)
summary(modeloLiftOffDiffxDirA)
AovLiftOffSumA<-summary(modeloLiftOffxDirA)
capture.output(AovLiftOffSumA, file="AOV1LiftOff1xDir.doc")


#Testeo de componentes principales con Tukey
TukeyHSD(modeloLiftOffxDirA, which = "GrupoLiftOff")

TukeyHSD(modeloLiftOffxDirA, which = "SenDir")

with(Dataset, interaction.plot(GrupoLiftOff, SenDir, LiftOff, fun = mean,
                               main = "Interaction Plot"))


with(Dataset, interaction.plot(CueDir, SenDir, LiftOff, fun = mean,
                               main = "Interaction Plot"))

with(Dataset, interaction.plot(SentenceDur, SenDir, LiftOff, fun = mean,
                               main = "Interaction Plot"))

#Modelo 2: Anova sin interaccion de 3 factores
modeloLiftOffDiffxDirB <- update(modeloLiftOffDiffxDirA, . ~ . -CueDir:SenDir:GrupoLiftOffDiff)
summary(modeloLiftOffDiffxDirB)
AovLiftOffxDirB<-summary(modeloLiftOffxDirB)
#capture.output(AovMoveTimeSumB, file="AOV1MoveTime2.doc")

#Modelo 3: Anova sin interaccion
modeloLiftOffxDirC <- aov(LiftOff~CueDir+SenDir+GrupoLiftOff)
summary(modeloLiftOffxDirC)
AovLiftOffxDirC<-summary(modeloLiftOffxDirC)
#capture.output(AovMoveTimeSumB, file="AOV1MoveTime2.doc")

# Son diferentes los modelos con interaccion y sin?
anova(modeloLiftOffxDirA, modeloLiftOffxDirC)
#Si

##Modelo Anova con interaccion y sentence duration
modeloLiftOffDiffC<-aov(LiftOffDiff~SenDir*CueDir*GrupoLiftOffDiff*SentenceDur, data=Dataset)
summary(modeloLiftOffDiffC)
AovLiftOffSumSentDur<-summary(modeloLiftOffC)
capture.output(AovLiftOffSumSentDur, file="AOV2LiftDiffxSenDur.doc")

#Indepencia de los residuos

Residuos1<-plot(modeloLiftOffxDirA$residuals)
View(Residuos1)
Residuos2<-plot(modeloLiftOffxDirB$residuals)
View(Residuos2)
Residuosa<-plot(modeloLiftOffC$residuals)
View(Residuosa)

