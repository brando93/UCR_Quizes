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
"""


class Lista():
           
    def generarReporteAnio(self):
        lista = []
        dic = {}
        temblores = open("temblores.csv","r+", encoding='utf-8-sig')
        #f = open("test.txt","w+")
        for linea in temblores:
            linea1 = linea.replace(",",".")
            linea2 = linea1.replace(";",",").strip()
            year = linea2.split(',')[0] # 2015
            month = linea2.split(',')[1] # 1
            magnitud = linea2.split(',')[2] #4.0
            if year in dic:
                dic[year].append(float(magnitud))
            else:
                dic[year] = [float(magnitud)]
        #print(dic)
        for i in dic:
            cantidad=len(dic.get(i))
            suma= sum(dic.get(i))
            promedio = suma / cantidad
            anio=str("Year: "+i+" \n")
            cant_sismo=str("Cantidad Sismos: "+ str(cantidad))
            promedio_s=str(" Promedio Sismos:"+" %.2f " % promedio+"\n")
            resultado= anio+cant_sismo+promedio_s
            print(resultado)
            space = "\n"
            #f.write(space)
            #f.write(str(resultado))
            #f.write(foo.encode('utf8'))
      
generar = Lista()
generar.generarReporteAnio()