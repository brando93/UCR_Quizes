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


class Terremotos():
    
    def generarLista(self):
        lista = []
        count = 0
        temblores = open("temblores.csv","r+", encoding='utf-8-sig')
        newfile = open("test.txt","w+")
        for linea in temblores:
            count +=1
            linea1 = linea.replace(",",".")
            linea2 = linea1.replace(";",",")
            lista.append(linea2)
            newfile.write(linea2)
            print(linea2)


generar = Terremotos()
generar.generarLista()