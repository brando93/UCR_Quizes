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
        self.basededatos = open("Base_de_Datos.txt","w")
        if cedula == 1:
            cedula = input("Digite numero de cedula fisica: ")
            self.cedulafisica = cedula
            self.ID = self.cedulafisica
            linea1 = "Cedula Juridica: ", self.cedulafisica
            linea2 = "Nombre: ",self.nombre
            linea3 = " Telefono:", self.telefono
            linea = str(linea1)+str(linea2)+str(linea3)
            print(linea)
            self.basededatos.write(str(linea))
        elif cedula == 2:
            cedula = input("Digite numero de cedula juridica: ")
            self.cedulajuridica = cedula
            self.ID = self.cedulajuridica
            linea1 = "Cedula Juridica: ", self.cedulajuridica
            linea2 = "Nombre: ",self.nombre
            linea3 = " Telefono:", self.telefono
            linea = str(linea1)+str(linea2)+str(linea3)
            print(linea)
            self.basededatos.write(str(linea))

class Factura(Contribuyente):
    
    def __init__(self,fecha,monto, validar):
        self.dic = {}
        super().__init__(cedula,nombre, telefono)
        self.fecha = fecha
        self.monto = monto
        self.iva = 13
        self.validar = validar
        
        
    def crearDic(self):
        self.dic[self.ID] = self.nombre

    def detalle(self):
        self.dic1 = {}
        self.total = (self.monto+((float(self.monto)*float(self.iva))/100))
        self.dic1[self.validar] = str(self.fecha), str(self.monto), str(self.iva)+"%", str(self.total)

    def validarMetodo(self):
        print(self.dic)
        if self.validar in self.dic:
            Factura.detalle()
        else:
            print("ID no registrado")
                
                
    
    def ImprimirVenta(self):
        self.imprimr = input("Ingrese ID :")
        if self.imprimr in self.dic1:
            linea=("Nombre: ",self.nombre+"\nFecha de Factura: ",self.dic1[self.imprimr][0]+"\nMonto: ",self.dic1[self.imprimr][1]+"\n")
            print(linea)
            self.basededatos.write(str(linea))
        else:
            print("Incorrect ID")


def menu():
    opt = 0
    try:
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
                validar = input(("Validar cedula existente: "))
                fecha = input("Digite fecha: ")
                monto = float(input("Digite el monto: ")) 
                factura1 = Factura(fecha, monto, validar)
                factura1.crearDic()
                factura1.validarMetodo()  
            elif opt ==3:
                factura1.ImprimirVenta() 
            elif opt ==4:
                None
            elif opt ==5:
                break
    except:
        print("Invalid option")

menu()