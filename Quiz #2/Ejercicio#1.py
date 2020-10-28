"""
1 - Ejercicio 1 (60 puntos)
La Red Sismológica Nacional, dentro de su proyecto de investigación en el estudio de temblores de
Costa Rica, ha generado un archivo plano de los temblores registrados desde el 2008 al 2020, con el
siguiente detalle de la información
1. Año del temblor registrado.
2. Mes del temblor registrado.
3. Grado del temblor registrado.
Usted ha sido contratado para hacer un programa que tome este archivo y realice las siguientes
acciones:
1. Estadísticas por mes: se debe de generar un archivo .txt el cual debe contener el año, mes,
cantidad de temblores del correspondiente mes y el promedio de los temblores que se
registraron en ese mes.
2. Estadísticas por año: se debe de generar un archivo .txt el cual debe contener el año, cantidad de
temblores registrados en ese año y el promedio de los temblores registrados en ese año.
Rúbrica
Descripción Puntaje
Menú 20 puntos
Estadísticas por mes 20 puntos
Estadísticas por año 20 puntos
 2 - Ejercicio 2 (20 puntos)
Escribir dos funciones que permitan calcular:
a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
b) La duración en horas, minutos y segundos de un intervalo dado en segundos.
 3 - Ejercicio 3 (20 puntos)
Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario dos
intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la
duración total en horas, minutos y segundos.
"""


class ReporteAnual():# Generates anual report
    def generarAnual(self):
        self.lista=[]
        self.dic={}
        temblores=open("temblores.csv","r", encoding='utf-8-sig')
        f = open("ReporteAnual.csv","w")
        for linea in temblores:
            linea1=linea.replace(",",".")
            linea2=linea1.replace(";",",").strip()
            year=linea2.split(',')[0] # 2015
            month=linea2.split(',')[1] # 1
            magnitud=linea2.split(',')[2] # 4.0
            if year in self.dic:
                self.dic[year].append(float(magnitud))
            else:
                self.dic[year]=[float(magnitud)]
                
        for i in self.dic:
            cantidad=(len(self.dic.get(i)))
            promedio=sum(self.dic.get(i))/cantidad
            anio=str("Year: "+i+" \n")
            cant_sismo=str("Cantidad Sismos: "+ str(cantidad))
            promedio_s=str(" Promedio Sismos:"+" %.2f " % promedio+"\n")
            resultado= anio+cant_sismo+promedio_s
            f.write(str(resultado))

class ReporteMensual():# Generates anual/montly report
    def generarMensual(self):
        self.dic={}
        self.dic2={}
        temblores=open("temblores.csv","r", encoding='utf-8-sig')
        f1 = open("ReporteMensual.csv","w")
        for linea in temblores:
            linea1=linea.replace(",",".")
            linea2=linea1.replace(";",",").strip()
            year=linea2.split(',')[0] # 2015
            month=linea2.split(',')[1] # 1
            magnitud=linea2.split(',')[2] # 4.0b
            if year in self.dic:
                self.dic[year].append(str(month))
            else:
                self.dic[year]=[str(month)]

            if year in self.dic:
                self.dic[year].append(float(magnitud))
            else:
                self.dic[year]=[float(magnitud)]

        for key, value in self.dic.items():
            for element in value:
                    mes=(self.dic2.get(key))
                    anio="año: " + key
        for key, value in self.dic.items():
            for element in value:
                if type(element) is str:
                    output=str("Year: "+key+"mes"+element+" \n")
                    f1.write(str(output))
                if type(element) is float:
                    output2=str("magnitud del mes: "+ str(element)+"\n")
                    f1.write(str(output2))
                        
generar=ReporteAnual()                        
generar1=ReporteMensual()

opt = 8
while opt != 0:
    
    print("\n",
        " 1) Generar reporte anual\n",
        " 2) Generar report mensual\n",
        " 3) Calcular segundos/minutos\n",
        " 5) Salir"
    )
    opt= input("Digite una opcion: ")
    if opt == "1":
        generar.generarAnual()
        print("GENERATING FILE --> ReporteAnual.csv")
    if opt == "2":
        generar1.generarMensual()
        print("GENERATING FILE --> ReporteMensual.csv")
    if opt == "3":
        None
    if opt == "5":
        break      