# Analisis de datos incorporando compatibilidad en lugar de Sentence dir y cue dir

ls()
rm(list=ls())
ls()

####Analisis multifactorial
install.packages("dplyr")
install.packages("readxl")
install.packages("ggpubr")
install.packages("gplot2")

install.packages("qqplotr")
library(ggplot2)
library(ggpubr)
library(qqplotr)
library(readxl)
library(dplyr)
#Seteo dir de trabajo
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad\\Analisis por medias\\Lift Off Latency")

#Abro los datos que voy a usar
Dataset <-read.csv("LiftOffNoOutliers.csv")
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

######## No es normal

hist(Compatibilidad)
boxplot(Compatibilidad)
hist(LiftOff)
boxplot(LiftOff)
shapiro.test(LiftOff)
ggplot(mapping = aes(sample = LiftOff)) + stat_qq_point(size = 2)

##########  ANOVA Lift Off Latency ########## 


####### Compatibilidad ########

##Modelo Anova con interaccion:      LiftOff~Compatibilidad*GrupoLiftOff
modeloLiftOff1<-aov(LiftOff~Compatibilidad*GrupoLiftOff, data=Dataset)
summary(modeloLiftOff1)
AovLiftOffSum1<-summary(modeloLiftOff1)
capture.output(AovLiftOffSum1, file="AovLiftOffSum1.doc")

#Modelo 2: Anova sin interaccion de 3 factores
modeloLiftOff2 <- update(modeloLiftOff1, . ~ . -Compatibilidad:GrupoLiftOff)
summary(modeloLiftOff2)
AovLiftOff2<-summary(modeloLiftOff2)
capture.output(AovLiftOff2, file="AOVLiftOff2.doc")

##Modelo Anova con interaccion:  LiftOff~Compatibilidad*GrupoLiftOff*SentenceDur
modeloLiftOffA<-aov(LiftOff~Compatibilidad*GrupoLiftOff*SentenceDur, data=Dataset)
summary(modeloLiftOffA)
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
CueDir<-as.character(CueDir)
modeloLiftOffxDirA<-aov(LiftOff~SenDir*GrupoLiftOff*CueDir, data=Dataset)
summary(modeloLiftOffxDirA)
AovLiftOffSumA<-summary(modeloLiftOffxDirA)
capture.output(AovLiftOffSumA, file="AOV1LiftOff1xDir.doc")
str(modeloLiftOffxDirA)

#Testeo de componentes principales con Tukey

Tukey1<-TukeyHSD(modeloLiftOffxDirA)
print(Tukey1)


#Guardo los resultados de Tukey
SenDirGrupoLiftOffCueDir<-as.data.frame(Tukey1$`SenDir:GrupoLiftOff:CueDir`)
write.csv(SenDirGrupoLiftOffCueDir, "TukeyInteraccion.csv", row.names=FALSE, quote=FALSE)

SenDirGrupoLiftOff<-as.data.frame(Tukey1$`SenDir:GrupoLiftOff`)
write.csv(SenDirGrupoLiftOff, "TukeySenDir:GrupoLiftOff.csv", row.names=FALSE, quote=FALSE)

SenDirCueDir<-as.data.frame(Tukey1$`SenDir:CueDir`)
write.csv(SenDirCueDir, "TukeySenDir:CueDir.csv", row.names=FALSE, quote=FALSE)

GrupoLiftOffCueDir<-as.data.frame(Tukey1$`GrupoLiftOff:CueDir`)
write.csv(GrupoLiftOffCueDir, "TukeyGrupoLiftOffCueDir.csv", row.names=FALSE, quote=FALSE)

TukeyGrupoLiftOff<-as.data.frame(Tukey1$GrupoLiftOff)
write.csv(TukeyGrupoLiftOff, "TukeyGrupoLiftOff.csv", row.names=FALSE, quote=FALSE)

TukeyCueDir<-as.data.frame(Tukey1$CueDir)
write.csv(TukeyCueDir, "TukeyCueDir.csv", row.names=FALSE, quote=FALSE)

TukeySenDir<-as.data.frame(Tukey1$SenDir)
write.csv(TukeysenDir, "TukeySenDir.csv", row.names=FALSE, quote=FALSE)

#Armo los resultados con letras
TukeyLO<-summary(Tukey1)
install.packages("multcompView")
library(multcompView)
tukey.cld<-multcompLetters4(modeloLiftOffxDirA, Tukey1)
print(tukey.cld)
Dataset$CueDirection<-as.character(CueDir)
Dataset$SentenceDirection<-as.character(SenDir)

#Plot de diferencia de medias por comparacion
tukey.plot.aov<-aov(MoveTime ~ CueDir:GrupoMoveTime:SenDir, data=Dataset)
tukey.plot.test<-Tukey1
par(mar=c(4,6,3,1))
plot(tukey.plot.test, las=1, cex.axis = 0.5)

#Tabla de medias por comparacion
mean.LiftOff.data <- Dataset %>%
  group_by(Grupo.Lift.Off, CueDirection, SentenceDirection) %>%
  summarise(
    LiftOff = mean(LiftOffLatency)
    )

mean.LiftOff.data$group <- c("b","b","b","b","a","a","a","a")


#Graficos de interaccion
with(Dataset, interaction.plot(GrupoLiftOff, SenDir, LiftOff, fun = mean,
                             main = "Interaction Plot"))


with(Dataset, interaction.plot(CueDir, SenDir, LiftOff, fun = mean,
                               main = "Interaction Plot"))

with(Dataset, interaction.plot(SentenceDur, SenDir, LiftOff, fun = mean,
                               main = "Interaction Plot"))




#Modelo 2: Anova sin interaccion de 3 factores
modeloLiftOffxDirB <- update(modeloLiftOffxDirA, . ~ . -CueDir:SenDir:GrupoLiftOff)
summary(modeloLiftOffxDirB)
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
modeloLiftOffC<-aov(LiftOff~SenDir*CueDir*GrupoLiftOff*SentenceDur, data=Dataset)
summary(modeloLiftOffC)
AovLiftOffSumSentDur<-summary(modeloLiftOffC)
capture.output(AovLiftOffSumSentDur, file="AOV2LiftDiffxSenDur.doc")


#Relacion sentence direction y sen dur
DuryDir<-aov(LiftOff~SenDir*SentenceDur, data = Dataset)
summary(DuryDir)


#Indepencia de los residuos
SenDir<-as.character(SenDir)
TukeyHSD(DuryDir, wich="SenDir")

Residuos1<-plot(modeloLiftOffxDirA$residuals)
View(Residuos1)
Residuos2<-plot(modeloLiftOffxDirB$residuals)
View(Residuos2)
Residuosa<-plot(modeloLiftOffC$residuals)
View(Residuosa)
