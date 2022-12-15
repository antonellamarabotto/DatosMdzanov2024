ls()
rm(list=ls())

####Analisis multifactorial
install.packages("dplyr")
install.packages("readxl")
library(readxl)
library(dplyr)
#
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis por medias\\Multifactorial MoveTime")
MultifactorialMoveTime <- read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis por medias\\Multifactorial MoveTime\\MultifactorialMoveTime.csv")
View(MultifactorialMoveTime)

#Nombro las variables
MoveTime<-MultifactorialMoveTime$MoveTime
Individuo<-MultifactorialMoveTime$ID
CueDirection<-MultifactorialMoveTime$CueDirection
SentenceDirection<-MultifactorialMoveTime$SentenceDirection
Grupo<-MultifactorialMoveTime$Grupo
SentenceDuration<-MultifactorialMoveTime$SentDur


summary(MultifactorialMoveTime$CueDirection)
summary(MultifactorialMoveTime$Grupo)


############Cantidad de datos en Grupo A y B
MultifactorialMoveTime %>% group_by(Grupo) %>% tally()

############3Cantidad de datos por Cue direction
MultifactorialMoveTime %>% group_by(CueDirection) %>% tally()

############Cantidad de datos por Sentence direction direction
MultifactorialMoveTime %>% group_by(SentenceDirection) %>% tally()


####
boxplot(MoveTime ~ Grupo , col = c("blue", "green"), ylab = "MoveTime")
png(filename = "MoveTime.png", width = 800, height = 600)


###############Normalidad################3

ggdensity(MoveTime, 
          main = "Density plot of Move Time",
          xlab = "MoveTime")
ggqqplot(MoveTime)

shapiro.test(MoveTime) ### No es Normal



#################Analisis sin duracion de la oracion############

##Modelo Anova con interaccion
modelo1<-aov(MoveTime~CueDirection*SentenceDirection*Grupo, data=MultifactorialMoveTime)
summary(modelo1)
AovMoveTimeSum<-summary(modelo1)
capture.output(AovMoveTimeSum, file="AOV1MoveTime.doc")


#Modelo 2: Anova sin interaccion de 3 factores
Modelo2 <- update(modelo1, . ~ . -CueDirection:SentenceDirection:Grupo)
summary(Modelo2)
Aov2MoveTimeSum<-summary(Modelo2)
capture.output(Aov2MoveTimeSum, file="AOV2MoveTime.doc")

#Es igual al primer modelo

##Modelo 3: Anova sin interaccion
Modelo3 <- update(Modelo2, .~CueDirection+SentenceDirection+Grupo)
summary(Modelo3)
Aov3MoveTimeSum<-summary(Modelo3)
capture.output(Aov3MoveTimeSum, file="AOV3MoveTime.doc")

#Es igual al modelo anterior. Vamos a corroborarlo comparandolos.
anova(Modelo2,Modelo3)
#Son iguales.

######El unico factor que marca diferencias en el LifOff es el grupo, pero ya lo sabiamos.
#Indepencia de los residuos

Residuos1<-plot(modelo1$residuals)
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





##########Incorporo como factor la duracion de la oreacion (Sentende Duration)####
##Modelo Anova con interaccion
modeloA<-aov(MoveTime~CueDirection*SentenceDirection*Grupo*SentenceDuration, data=MultifactorialMoveTime)
summary(modeloA)
AovAMoveTimeSum<-summary(modeloA)
capture.output(AovAMoveTimeSum, file="AOVAMoveTime.doc")

#Modelo 2: Anova sin interaccion de 3 factores
ModeloB <- update(modeloA, . ~ . -CueDirection:SentenceDirection:Grupo:SentenceDuration)
summary(ModeloB)
AovBMoveTimeSum<-summary(ModeloB)
capture.output(AovBMoveTimeSum, file="AOVBMoveTime.doc")

#Es igual al primer modelo

##Modelo 3: Anova sin interaccion
ModeloC <- update(ModeloB, .~CueDirection+SentenceDirection+Grupo+SentenceDuration)
summary(ModeloC)

#Es igual al modelo anterior. Vamos a corroborarlo comparandolos.
anova(modeloA, ModeloB)
anova(ModeloB,ModeloC)

#Son iguales.

######El unico factor que marca diferencias en el LifOff es el grupo, pero ya lo sabiamos.



######El unico factor que marca diferencias en el LifOff es el grupo, pero ya lo sabiamos.
#Indepencia de los residuos

ResiduosA<-plot(modeloA$residuals)
ResiduosB<-plot(ModeloB$residuals)
ResiduosC<-plot(ModeloC$residuals)

#Normalidad: No hay normalidad de los residuos
boxplot(modeloA$residuals)
hist(modeloA$residuals)
qqnorm(modeloA$residuals) 
qqline(modeloA$residuals)

boxplot(ModeloB$residuals)
hist(ModeloB$residuals)
qqnorm(ModeloB$residuals) 
qqline(ModeloB$residuals)
