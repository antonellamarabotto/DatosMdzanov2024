##Tabla de contingencia

ls()
rm(list=ls())
ls()


#Seteo dir de trabajo
setwd("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad")

#Abro los datos
Data<-read.csv("DatosCompatibilidad.csv")
Data$Compatibilidad <- as.integer(Data$Compatibilidad) 
Compatibilidad<-Data$Compatibilidad
GrupoLiftOff<-Data$Grupo.Lift.Off
GrupoLiftDiff<-Data$Grupo.Lift.Off.Diff
GrupoMoveTime<-Data$Grupo.MoveTime


#####Tablas de contingencia Lift Off Latency
TablaLiftOff<-table(GrupoLiftOff, Compatibilidad)
TablaLiftOff
PropLiftOff<-prop.table(TablaLiftOff)
#BarPlot
par(mfrow = c(1, 2))

colores <- c("#80FFFF", "#FFFFFF")

barplot(PropLiftOff, col = colores, main="Barplot Lift Off Latency")
legend("topleft", legend = c("Grupo A", "Grupo B"), fill = colores)

#Test de chi
chiLiftOff <- chisq.test(TablaLiftOff)
chiLiftOff$statistic
install.packages("DescTools")
library(DescTools)

ContCoef(TablaLiftOff)

#########Tablas de contingencia Lift Off Latency Difference
TablaLiftOffDiff<-table(GrupoLiftDiff, Compatibilidad)
TablaLiftOffDiff
propLiftDiff<-prop.table(TablaLiftOffDiff)

#Test de chi
chiLiftOffDiff <- chisq.test(TablaLiftOffDiff)
chiLiftOffDiff$statistic
ContCoef(TablaLiftOffDiff)

#BarPlot

colores <- c("#80FFFF", "#FFFFFF")

barplot(propLiftDiff, col = colores, main="Barplot Lift Off Difference")
legend("topleft", legend = c("Grupo A", "Grupo B"), fill = colores)

#########Tablas de contingencia Move Time
TablaMoveTime<-table(GrupoMoveTime, Compatibilidad)
TablaMoveTime
propMoveTime<-prop.table(TablaMoveTime)

#BarPlot
colores <- c("#80FFFF", "#FFFFFF")
barplot(propMoveTime, col = colores, main="Barplot MoveTime")
legend("topleft", legend = c("Grupo A", "Grupo B"), fill = colores)

#Test de chi
chiMoveTime <- chisq.test(TablaMoveTime)
chiMoveTime$statistic
ContCoef(TablaMoveTime)
