ls()
rm(list=ls())
ls()

install.packages("dplyr")
library(dplyr)
install.packages("tidyr")
library(tidyr)
#Seteo dir de trabajo
setwd("C:\\Users\\UdeSA\\Desktop\\Antonella\\Doctorado\\Experimento prototipos\\Results")
#Miro los datos
View(dataset)


#Abro los datos que voy a usar

datosFranco<-readxl::read_excel("PruebaFranco 16-6.xlsx")
datosGonza<-readxl::read_excel("PruebaGonza16-6.xlsx")
#Tratamiento de datos Franco
tablaFranco<-filter(datosFranco, datosFranco$`'Accuracy'`!="NaN")
L2<-filter(tablaFranco, tablaFranco$Figura=="L2", tablaFranco$`'Accuracy'`==1)

summary(datosFranco)

#Tratamiento de datos Gonza
tablaGonza<-filter(datosGonza, datosGonza$`'Accuracy'`!="NaN")
L2G<-filter(tablaGonza, tablaGonza$Figura=="L2", tablaGonza$`'Accuracy'`==1)

L3G<-filter(tablaGonza, tablaGonza$Figura=="L3", tablaGonza$`'Accuracy'`==1)
L4G<-filter(tablaGonza, tablaGonza$Figura=="L4", tablaGonza$`'Accuracy'`==1)
L5G<-filter(tablaGonza, tablaGonza$Figura=="L5", tablaGonza$`'Accuracy'`==1)
L7G<-filter(tablaGonza, tablaGonza$Figura=="L7", tablaGonza$`'Accuracy'`==1)
RG<-filter(tablaGonza, tablaGonza$Figura=="R", tablaGonza$`'Accuracy'`==1)

#Tratamiento de datos Franco
tablaFranco<-filter(datosFranco, datosFranco$`'Accuracy'`!="NaN")
L2F<-filter(tablaFranco, tablaFranco$Figura=="L2", tablaFranco$`'Accuracy'`==1)
L3F<-filter(tablaFranco, tablaFranco$Figura=="L3", tablaFranco$`'Accuracy'`==1)
L4F<-filter(tablaFranco, tablaFranco$Figura=="L4", tablaFranco$`'Accuracy'`==1)
L5F<-filter(tablaFranco, tablaFranco$Figura=="L5", tablaFranco$`'Accuracy'`==1)
L7F<-filter(tablaFranco, tablaFranco$Figura=="L7", tablaFranco$`'Accuracy'`==1)
RF<-filter(tablaFranco, tablaFranco$Figura=="R", tablaFranco$`'Accuracy'`==1)


#Abro los datos que voy a usar: Aciertos gonza y franco

Aciertos<-readxl::read_excel("AciertosGonza y franco.xlsx")
install.packages("ggplot2")
library(ggplot2)
library(scales)
Aciertos$Figura<-as.factor(Aciertos$Figura)

barplot(Aciertos$Gonza, names.arg = Aciertos$Figura)
barplot(Aciertos$Franco, names.arg = Aciertos$Figura)
