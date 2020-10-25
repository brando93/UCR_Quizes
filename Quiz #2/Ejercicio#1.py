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
           
    def crearList(self):
        temblores = open("temblores1.csv","r+", encoding='utf-8-sig')
        #newfile = open("test.txt","w+")
        mes = 0
        anio = 0
        tem_mag = 0.0
        year = []
        years = 0
        month = []
        months = 0
        total = 0
        total1 = 0
        #read the whole document linea by line and save in list
        for linea in temblores:
            linea1 = linea.replace(",",".")
            linea2 = linea1.replace(";",",").strip() #['2015;1;4,0','2020;1;4,1','2020;7;1,1']
            #create constants with year, month, mangnitud for current loop
            a_year = linea2.split(',')[0] # 2015
            a_month = linea2.split(',')[1] # 1
            a_magnitud = linea2.split(',')[2] #4.0
            
            b_year = linea2.split(',')[0] # 2015
            b_month = linea2.split(',')[1] # 1
            b_magnitud = linea2.split(',')[2] #4.0
            
            if a_year == b_year and a_month == b_month:
                total = float(a_magnitud) + float(b_magnitud)
                total1 = total1 + total
                print("Year: ", a_year)
                print("Month: ", a_month)
                print("Total Magnitud:", total)
            else:
                continue

                
            
            #construct list with unique years in document
            #years = linea2.split(',')[0] 
            #year.append(years)
            #my_year = set(year) #['2015','2020']  
            
            #construct unique months in document
            #months = linea2.split(',')[1]
            #month.append(months)
            #my_month = set(month) # ['1','7']
            
generar = Lista()
generar.crearList()