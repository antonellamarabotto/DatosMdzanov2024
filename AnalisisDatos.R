"""
Analisis de Datos de prototipos

"

#Instalo paquetes
install.packages("readxl")
library(readxl)
install.packages("dplyr")
library(dplyr)
install.packages("tidyr")
library(tidyr)


#Seteo dir de trabajo
setwd("C:\\Users\\USUARIO\\Desktop\\Doctorado\\Doctorado\\Doctorado\\Experimento prototipos\\Results")
list.files() 


#Importo los datos
datos<-readxl::read_excel("AntonellaAhumadaNov23Prototipos.xlsx")
attach(datos)

#Cambio nombres
colnames(datos) <- c('Trial','Answer','Accuracy','ReactionTime','Time','EventName','Figura') 

#Saco filas NaN
Datoslimpios<-filter(datos, datos$Accuracy !="NaN")

#Cuento las "No Press"
NoPress<-sum(Datoslimpios$Accuracy==-1)
Datoslimpios<-filter(Datoslimpios, Datoslimpios$Accuracy !=-1)


#Separo por categoria de figura
L0<-filter(Datoslimpios, Datoslimpios$Figura=="L0")
L2<-filter(Datoslimpios, Datoslimpios$Figura=="L2")
L3<-filter(Datoslimpios, Datoslimpios$Figura=="L3")
L4<-filter(Datoslimpios, Datoslimpios$Figura=="L4")
L5<-filter(Datoslimpios, Datoslimpios$Figura=="L5")
L7<-filter(Datoslimpios, Datoslimpios$Figura=="L7")

#Grafico de barras
barplot(Datoslimpios$Accuracy, names.arg = Datoslimpios$Figura)



