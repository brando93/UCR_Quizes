"""
Ejercicio 2 (60 puntos)
Simulador de  Hacienda.
Cree un programa que simule el sistema nacional de tributación, en hacienda existen Empresas y Personas que 
tributan generalmente el 13% de sus ingresos.

Para registrar un contribuyente se necesita el número de cédula (jurídica o física),  el nombre y el teléfono, 
la información de las personas registradas debe leerse  por pantalla.

Cree un programa que permita:

1- Registrar un vendedor donde se almacena en un diccionario  como llave el ID del vendedor que contenga:
1.	Nombre del vendedor
2.	Teléfono.

2- Registrar ventas.
Permita un diccionario como llave ID del vendedor registrar facturas de ventas de un vendedor, 
donde se registra una clase factura el cual debe detallar.
-Id vendedor
-Fecha factura
-Monto:
-Monto IVA. :
-Monto Total: Monto + Monto IVA

3- Imprimir Ventas:
	Imprimir las ventas registradas de un vendedor que se busca por el ID
- Nombre del vendedor.
- fecha factura.
- monto total.

4- Guardar los datos:
	Guardar los datos del vendedor en un archivo con nombre “Vendedores.bin”

	Guardar los datos de facturas en un archivo con nombre “Facturas.bin”



empresas y persoans tributan el 13%

"""
class Contribuyente():
    
    def __init__(self,cedula,nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.basededatos = open("Base_de_Datos.txt","r")
        caracter = ")(,''"
        if cedula == 1:
            cedula = input("Digite numero de cedula fisica: ")
            self.cedulafisica = cedula
            self.ID = self.cedulafisica
            linea1 = self.cedulafisica
            linea2 = self.nombre
            linea3 = self.telefono
            linea4 = (" %-30s  %-34s  %-10s " % (linea1, linea2, linea3))
            linea = linea4
            for i in caracter:
                linea = linea.replace(i,"")
            #titulo = (" %-30s  %-34s  %-10s " % ("Cedula Fisica", "Nombre", "Telefono"))
            self.basededatos = open("Base_de_Datos.txt","a")
            self.basededatos.write(str(linea+"\n"))
            #self.basededatos.close()
        elif cedula == 2:
            cedula = input("Digite numero de cedula juridica: ")
            self.cedulajuridica = cedula
            self.ID = self.cedulajuridica
            linea1 = "Cedula Juridica: ", self.cedulajuridica
            linea2 = "Nombre: ",self.nombre
            linea3 = " Telefono:", self.telefono
            linea = (" %-20s  %-20s  %-20s " % (linea1, linea2, linea3))
            self.basededatos = open("Base_de_Datos.txt","a")
            self.basededatos.write(str(linea+"\n"))
            
            #self.basededatos.close()
            

class Factura(Contribuyente):
    
    def __init__(self,fecha,monto, validar):
        self.dic = {}
        #super().__init__(cedula,nombre, telefono)
        self.fecha = fecha
        self.monto = monto
        self.iva = 13
        self.validar = validar
        
    def validarMetodo(self):
        self.basededatos = open("Base_de_Datos.txt","r")
        for line in self.basededatos:
            if self.validar in line:
                self.total = (self.monto+((float(self.monto)*float(self.iva))/100))
                linea_dic = self.validar,self.fecha, self.monto, self.iva, self.total
                dos_ob = str(self.fecha), str(self.total)
            self.basededatos = open("Base_de_Datos.txt","a")
            self.basededatos.write(str(dos_ob))
            print(dos_ob)
            self.basededatos.close()
                
    
    def ImprimirVenta(self):
        self.basededatos = open("Base_de_Datos.txt","r")
        self.factura = open("Factura.txt","r")
        self.imprimir = input("Ingrese ID :")
        for line in self.basededatos:
            if self.imprimir in line:
                line = line.split()
                for a in line:
                    self.factura = open("Factura.txt","a")
                    self.factura.write(str(line+"\n"))
        print(self.total)
        self.factura.close()


def menu():
    opt = 0
    #try:
    while opt != 5:
        print(
            "1) Registrar Vendedor \n"
            "2) Registrar Ventas\n"
            "3) Imprimir Ventas\n"
            "4) Guardar datos\n"
            "5) Salir\n"
        )
        opt=int(input("Ingrese una opcion: "))
        if opt == 1:
            nombre = input("Digite el nombre: ")
            telefono = int(input("Digite el telefono: "))
            cedula = int(input(("Escoja el tipo de cedula: \n"
                "1) Fisica: \n"
                "2) Juridica: \n"
            )))
            contri = Contribuyente(cedula, nombre, telefono)
        elif opt ==2:
            validar = input(("Registrar cedula: "))
            fecha = input("Digite fecha: ")
            monto = float(input("Digite el monto: ")) 
            factura1 = Factura(fecha, monto, validar)
            #factura1.crearDic()
            factura1.validarMetodo()  
        elif opt ==3:
            factura1.ImprimirVenta() 
        elif opt ==4:
            None
        elif opt ==5:
            break
    #except:
    #    print("Invalid option")

menu()