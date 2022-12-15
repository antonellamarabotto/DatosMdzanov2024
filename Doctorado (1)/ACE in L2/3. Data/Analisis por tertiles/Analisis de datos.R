install.packages("dplyr")
library(dplyr)

#Elimino las filas con Accuracy 0
Data1 = filter(Dataset, Accuracy != "0")

#Saco los trials con oraciones sin sentido
Data=filter(Data1, MoveTime!="0")

#Nueva columna llamada liftOffDiff
Data$liftOffDiff<- Data$LiftOffLatency - Data$SentDur
write.csv(Data,"C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis\\Datos.csv", row.names = FALSE)

#####Media por sujeto de liftOff, Movetime y LiftOffDiff
#LIftOff
LiftOffMean<-aggregate(x = Data$LiftOffLatency,                # Specify data column
          by = list(Data$ptid),              # Specify group indicator
          FUN = mean) 
#LIftOffDiff
LiftOffDiffMean<-aggregate(x = Data$liftOffDiff,                # Specify data column
          by = list(Data$ptid),              # Specify group indicator
          FUN = mean) 
#Movetime
MoveTimeMean<-aggregate(x = Data$MoveTime,                # Specify data column
          by = list(Data$ptid),              # Specify group indicator
          FUN = mean) 

#Tabla de medias
Datamedia<-data.frame(LiftOffMean$Group.1)
Datamedia$LiftOffMean<-LiftOffMean$x
Datamedia$LiftOffDiffMean<-LiftOffDiffMean$x
Datamedia$MoveTimeMean<-MoveTimeMean$x

write.csv(Datamedia,"C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis\\DatosMedias.csv", row.names = FALSE)

######Calculo de la mediana de las medias
#LiftoffTime
median(Datamedia$LiftOffMean) 
#Movetime
median(Datamedia$MoveTimeMean) 
#LiftOffDiff
median(Datamedia$LiftOffDiffMean) 
