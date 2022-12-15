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
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad\\Analisis por tertiles")


Dataset<- read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad\\Analisis por tertiles\\GruposTertiles.csv")


Dataset$Compatibilidad <- ifelse(Dataset$CueDirection>Dataset$SentenceDirection, 0,
                                 ifelse(Dataset$CueDirection < Dataset$SentenceDirection, 0, 1))

write.csv(Dataset,"C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad\\Analisis por tertiles\\DatosCompattertiles.csv", row.names = FALSE)

#### Outliers de Move Time
Dataset$Compatibilidad<- as.integer(Dataset$Compatibilidad) 


m<-mean(Dataset$MoveTime)
sd<-sd(Dataset$MoveTime)
out.max<-m+2*sd
out.min<-m-2*sd

no.outliers<-subset(Dataset,Dataset$MoveTime<out.max & Dataset$MoveTime>out.min)

write.csv(no.outliers, "MoveTimeNoOutliers.csv")

#### Outliers de Lift Off Latency


m<-mean(Dataset$LiftOffLatency)
sd<-sd(Dataset$LiftOffLatency)
out.max<-m+2*sd
out.min<-m-2*sd

no.outliers<-subset(Dataset,Dataset$LiftOffLatency<out.max & Dataset$LiftOffLatency>out.min)

write.csv(no.outliers, "LiftOffNoOutliers.csv")


#### Outliers de Lift Off Diff


m<-mean(Dataset$liftOffDiff)
sd<-sd(Dataset$liftOffDiff)
out.max<-m+2*sd
out.min<-m-2*sd

no.outliers<-subset(Dataset,Dataset$liftOffDiff<out.max & Dataset$liftOffDiff>out.min)

write.csv(no.outliers, "LiftOffDiffNoOutliers.csv")
