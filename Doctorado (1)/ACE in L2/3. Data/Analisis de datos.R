ls()
rm(list=ls())
ls()


install.packages("dplyr")
library(dplyr)

Dataset<- read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analysis-ready file.csv")
#Mediana y media
mean(Dataset$MoveTime)#Movetime
median(Dataset$MoveTime)
sd(Dataset$MoveTime)
mean(Dataset$LiftOffLatency)
median(Dataset$LiftOffLatency)
sd(Dataset$LiftOffLatency)

###Elimino las filas con Accuracy 0
Data1 = filter(Dataset, Accuracy != "0")
#Mediana y media
mean(Data1$MoveTime)#Movetime
median(Data1$MoveTime)
sd(Data1$MoveTime)

sd(Data1$LiftOffLatency)
mean(Data1$LiftOffLatency)
median(Data1$LiftOffLatency)

#Saco los trials con oraciones sin sentido
Data=filter(Data1, MoveTime!="0")
mean(Data$MoveTime)#Movetime
sd(Data$MoveTime)
median(Data$MoveTime)

mean(Data$LiftOffLatency)#LiftOffLatency
sd(Data$LiftOffLatency)
median(Data$LiftOffLatency)


#Nueva columna llamada liftOffDiff
Data$liftOffDiff<- Data$LiftOffLatency - Data$SentDur
write.csv(Data,"C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Datos.csv", row.names = FALSE)

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

write.csv(Datamedia,"C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\DatosMedias.csv", row.names = FALSE)

######Calculo de la mediana de las medias
#LiftoffTime
median(Datamedia$LiftOffMean) 
sd(Datamedia$LiftOffMean)
#Movetime
median(Datamedia$MoveTimeMean) 
sd(Datamedia$MoveTimeMean)
#LiftOffDiff
median(Datamedia$LiftOffDiffMean) 
sd(Datamedia$LiftOffDiffMean)
