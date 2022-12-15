
ls()
rm(list=ls())
ls()


install.packages("dplyr")
library(dplyr)

Dataset<- read.csv("C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Datos.csv")


Dataset$Compatibilidad <- ifelse(Dataset$CueDirection>Dataset$SentenceDirection, 0,
                     ifelse(Dataset$CueDirection < Dataset$SentenceDirection, 0, 1))

write.csv(Dataset,"C:\\Users\\Antonella\\Desktop\\Doctorado\\ACE in L2\\3. Data\\Analisis con compatibilidad\\DatosCompatibilidad.csv", row.names = FALSE)
