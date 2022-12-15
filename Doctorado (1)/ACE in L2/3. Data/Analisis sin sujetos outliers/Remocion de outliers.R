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
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis sin sujetos outliers")

#Abro los datos
Dataset<- read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Datos.csv")

#Abro los datos por media
Datamedia<- read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\DatosMedias.csv")

MoveTime<-Datamedia$MoveTimeMean
LiftOff<-Datamedia$LiftOffMean
LiftOffDiff<-Datamedia$LiftOffDiffMean


#### Outliers de Move Time
m<-median(Dataset$MoveTime)
m
M<-mean(Dataset$MoveTime)
M
sd<-sd(Dataset$MoveTime)
sd
out.max<-m+2*sd
out.min<-m-2*sd

no.outliers<-subset(Datamedia,MoveTime<out.max & MoveTime>out.min)

write.csv(no.outliers, "MoveTimeNoOutliers.csv")

###NO hay outliers de MoveTime



#### Outliers de LiftOff
m<-median(Dataset$LiftOffLatency)
m
sd<-sd(Dataset$LiftOffLatency)
sd
out.max<-m+2*sd
out.min<-m-2*sd

no.outliers<-subset(Datamedia,LiftOff<out.max & LiftOff>out.min)

write.csv(no.outliers, "LiftOffNoOutliers.csv")



#### Outliers de LiftOffDiff
m<-median(Dataset$liftOffDiff)
m
sd<-sd(Dataset$liftOffDiff)
sd
out.max<-m+2*sd
out.min<-m-2*sd

no.outliers<-subset(Datamedia,LiftOffDiff<out.max & LiftOffDiff>out.min)

write.csv(no.outliers, "LiftOffDiffNoOutliers.csv")


