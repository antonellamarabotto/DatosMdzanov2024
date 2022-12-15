


install.packages("dplyr")
library(dplyr)
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data")
Data1<-read.csv("Datos.csv")

#Elimino las filas con Accuracy 0
Data1 = filter(Dataset, Accuracy != "0")
DatosMedias<-read.csv("DatosMedias.csv")

# Encontrar los tertiles de LiftOff
TertLiftOff = quantile(DatosMedias$LiftOffMean, c(0:3/3))
TertLiftOffdiff = quantile(DatosMedias$LiftOffDiffMean, c(0:3/3))
TertMoveTime = quantile(DatosMedias$MoveTimeMean, c(0:3/3))

# clasifico los ind por tertiles
DatosMedias$tertLiftOff = with(DatosMedias, 
               cut(LiftOffMean, 
                   TertLiftOff, 
                   include.lowest = T, 
                   labels = c("Lento", "Medio", "Rapido")))

DatosMedias$TertLiftOffDiff = with(DatosMedias, 
                               cut(LiftOffDiffMean, 
                                   TertLiftOffdiff, 
                                   include.lowest = T, 
                                   labels = c("Lento", "Medio", "Rapido")))

DatosMedias$TertMoveTime = with(DatosMedias, 
                                   cut(MoveTimeMean, 
                                       TertMoveTime, 
                                       include.lowest = T, 
                                       labels = c("Lento", "Medio", "Rapido")))
#Guardo los datos con tertiles
DatosTertiles=DatosMedias
write.csv(DatosTertiles, "C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis por tertiles\\DatosTertiles.csv", row.names = FALSE)
