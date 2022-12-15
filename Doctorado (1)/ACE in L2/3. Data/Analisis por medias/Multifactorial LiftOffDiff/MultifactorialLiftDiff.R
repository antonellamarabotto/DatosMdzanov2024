####Analisis multifactorial


ls()
rm(list=ls())
ls()


install.packages("dplyr")
install.packages("readxl")
library(readxl)
library(dplyr)
#
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis por medias\\Multifactorial LiftOffDiff")
MultifactorialLiftDiff<- read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis por medias\\Multifactorial LiftOffDiff\\MultifactorialLiftOffDiff.csv")

#Nombro las variables
LiftDiff<-MultifactorialLiftDiff$liftOffDiff
Individuo<-MultifactorialLiftDiff$ID
CueDirection<-MultifactorialLiftDiff$CueDirection
SentenceDirection<-MultifactorialLiftDiff$SentenceDirection
Grupo<-MultifactorialLiftDiff$Grupo
SentenceDuration<-MultifactorialLiftDiff$SentDur





############Cantidad de datos en Grupo A y B
MultifactorialLiftDiff %>% group_by(Grupo) %>% tally()

############3Cantidad de datos por Cue direction
MultifactorialLiftDiff %>% group_by(CueDirection) %>% tally()

############Cantidad de datos por Sentence direction direction
MultifactorialLiftDiff %>% group_by(SentenceDirection) %>% tally()

####
boxplot(LiftDiff ~ Grupo , col = c("blue", "green"), ylab = "Lift Off Difference")
png(filename = "BoxplotLiftOffDiff.png", width = 800, height = 600)



###############Normalidad################3

ggdensity(LiftDiff, 
          main = "Density plot of Lift Off Latency Difference",
          xlab = "LiftOffDiff")
ggqqplot(LiftDiff)

shapiro.test(LiftDiff) ### No es Normal

##Modelo Anova con interaccion
modelo1<-aov(LiftDiff~CueDirection*SentenceDirection*Grupo, data=MultifactorialLiftDiff)
summary(modelo1)
Aov1LiftDiffSum<-summary(modelo1)
capture.output(Aov1LiftDiffSum, file="AOV1LiftDiff.doc")

#Modelo 2: Anova sin interaccion de 3 factores
Modelo2 <- update(modelo1, . ~ . -CueDirection:SentenceDirection:Grupo)
summary(Modelo2)
Aov2LiftDiffSum<-summary(Modelo2)
capture.output(Aov2LiftDiffSum, file="AOV2LiftDiff.doc")

#Es igual al primer modelo

##Modelo 3: Anova sin interaccion
Modelo3 <- update(Modelo2, .~CueDirection+SentenceDirection+Grupo)
summary(Modelo3)
Aov3LiftDiffSum<-summary(Modelo3)
capture.output(Aov3LiftDiffSum, file="AOV3LiftDiff.doc")

#Es igual al modelo anterior. Vamos a corroborarlo comparandolos.
anova(Modelo2,Modelo3)
#Son iguales.

######El unico factor que marca diferencias en el LifOff es el grupo, pero ya lo sabiamos.

#Indepencia de los residuos

Residuos1<-plot(modelo1$residuals)
View(Residuos1)
Residuos2<-plot(Modelo2$residuals)
Residuos3<-plot(Modelo3$residuals)

#Normalidad: No hay normalidad de los residuos
boxplot(modelo1$residuals)
hist(modelo1$residuals)
qqnorm(modelo1$residuals) 
qqline(modelo1$residuals)

boxplot(Modelo2$residuals)
hist(Modelo2$residuals)
qqnorm(Modelo2$residuals) 
qqline(Modelo2$residuals)



######Agrego Sentence Duration como factor
##Modelo Anova con interaccion
modeloA<-aov(LiftDiff~CueDirection*SentenceDirection*Grupo*SentenceDuration, data=MultifactorialLiftDiff)
summary(modeloA)
AovALiftDiffSum<-summary(modeloA)
capture.output(AovALiftDiffSum, file="AOVALiftDiff.doc")
#Hay efecto de interaccion entre sentence Direction and duration y efecto de grupo y sentene duration

#Normalidad: No hay normalidad de los residuos
boxplot(modeloA$residuals)
hist(modeloA$residuals)
qqnorm(modeloA$residuals) 
qqline(modeloA$residuals)

