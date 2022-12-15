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
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis por medias\\Multifactorial LiftOFF")

#Abro los datos que voy a usar
MultifactorialLiftOff <-read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis por medias\\Multifactorial LiftOFF\\MultifactorialLiftOff.csv")
#Miro los datos
View(dataset)

#Nombro las variables
LiftOff<-MultifactorialLiftOff$LiftOffLatency
Individuo<-MultifactorialLiftOff$ptid
CueDirection<-MultifactorialLiftOff$CueDirection
SentenceDirection<-MultifactorialLiftOff$SentenceDirection
Grupo<-MultifactorialLiftOff$Grupo
SentenceDuration<-MultifactorialLiftOff$SentDur

summary(MultifactorialLiftOff$CueDirection)
summary(MultifactorialLiftOff$Grupo)

############Cantidad de datos en Grupo A y B
MultifactorialLiftOff %>% group_by(Grupo) %>% tally()

############3Cantidad de datos por Cue direction
MultifactorialLiftOff %>% group_by(CueDirection) %>% tally()

############Cantidad de datos por Sentence direction direction
MultifactorialLiftOff %>% group_by(SentenceDirection) %>% tally()

####
boxplot(LiftOff ~ Grupo , col = c("blue", "green"), ylab = "Lift Off Latency")
png(filename = "BoxplotLiftOff.png", width = 800, height = 600)



###############Normalidad################3

ggdensity(LiftOff, 
          main = "Density plot of Lift Off Latency",
          xlab = "LiftOff")
ggqqplot(LiftOff)

shapiro.test(LiftOff) ### No es Normal

######## No es normal
str(MultifactorialLiftOff)

plot.design(MultifactorialLiftOff$LiftOffLatency ~ ., data =MultifactorialLiftOff)

hist(SentenceDirection)
hist(CueDirection)
boxplot(CueDirection)


##Modelo Anova con interaccion
modelo1<-aov(LiftOff~CueDirection*SentenceDirection*Grupo, data=MultifactorialLiftOff)
summary(modelo1)
AovLiftOFFSum<-summary(modelo1)
capture.output(AovLiftOFFSum, file="AOV1LiftOff.doc")

#Modelo 2: Anova sin interaccion de 3 factores
Modelo2 <- update(modelo1, . ~ . -CueDirection:SentenceDirection:Grupo)
summary(Modelo2)

AOV2LiftOffsum<-summary(Modelo2)
capture.output(AOV2LiftOffsum, file="AOV2LiftOff.doc")
#Es igual al primer modelo

##Modelo 3: Anova sin interaccion
Modelo3 <- update(Modelo2, .~CueDirection+SentenceDirection+Grupo)
summary(Modelo3)
AOV3sum<-summary(Modelo3)
capture.output(AOV3sum, file="AOV3LiftOff.doc")
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


#####Agrego Sentence duration como factor

##Modelo Anova con interaccion
modeloA<-aov(LiftOff~CueDirection*SentenceDirection*Grupo*SentenceDuration, data=MultifactorialLiftOff)
summary(modeloA)
AovLiftOFFSumA<-summary(modeloA)
capture.output(AovLiftOFFSumA, file="AovALiftOff.doc")
###Hay interaccion sent dur y sent dir y efecto de grupo y sentence duration
#Modelo 2: Anova sin interaccion de 3 factores
ModeloB <- update(modeloA, . ~ . -CueDirection:SentenceDirection:Grupo:SentenceDuration)
summary(Modelo2)
AOVBsum<-summary(Modelo2)
capture.output(AOVBsum, file="AOVBLiftOff.doc")

#Es igual al primer modelo
##Modelo 3: Anova sin interaccion
ModeloC <- update(ModeloB, .~CueDirection+SentenceDirection+Grupo+SentenceDuration)
summary(Modelo3)
AOVCsum<-summary(Modelo3)
capture.output(AOVCsum, file="AOVCLiftOff.doc")

#Es igual al modelo anterior. Vamos a corroborarlo comparandolos.
anova(Modelo2,Modelo3)
#Son iguales.

#Indepencia de los residuos

ResiduosA<-plot(modeloA$residuals)
ResiduosB<-plot(ModeloB$residuals)
ResiduosC<-plot(ModeloC$residuals)
#Homocedasticidad
bartlett.test(modeloA$residuals ~ Grupo)
