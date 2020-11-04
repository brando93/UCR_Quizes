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
		if cedula == 1:
			cedula = input("Digite numero de cedula fisica")
			self.cedulafisica = cedula
			self.ID = self.cedulafisica
			print("Cedula Fisica: ", self.cedulafisica,"Nombre: ",self.nombre, " Telefono:", self.telefono)
		elif cedula == 2:
			cedula = input("Digite numero de cedula juridica")
			self.cedulajuridica = cedula
			self.ID = self.cedulajuridica
			print("Cedula Juridica: ", self.cedulajuridica ,"Nombre: ",self.nombre, " Telefono:", self.telefono)

class Factura(Contribuyente):
    
    def __init__(self,fecha,monto, validar):
        self.fecha = fecha
        self.monto = monto
        self.iva = 13
        self.dic = {}
        self.validar = validar

    def detalle(self):
        super().__init__()
        self.total = (self.monto+(float(self.monto)*float(self.iva)/100))
        self.dic[self.ID] = self.fecha, self.monto,self.iva, self.total

    
    def validarMetodo(self):
        for k in self.dic.items():
            print(k)
            print(self.validar)
            if self.validar == k:
                Factura.detalle()
            else:
                print("ID no registrado")
def menu():
    nombre = input("Digite el nombre: ")
    telefono = int(input("Digite el telefono: "))
    cedula = int(input(("Escoja el tipo de cedula: \n"
		"1) Fisica"
		"2) Juridica"
	)))
    contri = Contribuyente(cedula, nombre, telefono)

def registarVentas():
    validar = int(input(("Valir cedula existente: ")))
    fecha = input("Digite fecha: ")
    monto = int(input("Digite el monto: "))
    factura1 = Factura(fecha, monto, validar)
    factura1.validarMetodo() 

menu()
registarVentas()