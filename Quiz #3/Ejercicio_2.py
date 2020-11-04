"""
Ejercicio 2 (60 puntos)
Simulador de  Hacienda.
Cree un programa que simule el sistema nacional de tributación, en hacienda existen Empresas y Personas que tributan generalmente el 13% de sus ingresos.

Para registrar un contribuyente se necesita el número de cédula (jurídica o física),  el nombre y el teléfono, la información de las personas registradas debe leerse  por pantalla.

Cree un programa que permita:

1- Registrar un vendedor donde se almacena en un diccionario  como llave el ID del vendedor que contenga:
1.	Nombre del vendedor
2.	Teléfono.

2- Registrar ventas.
Permita un diccionario como llave ID del vendedor registrar facturas de ventas de un vendedor, donde se registra una clase factura el cual debe detallar.
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
			print("Cedula Fisica: ", self.cedulafisica,"Nombre: ",self.nombre, " Telefono:", self.telefono)
		elif cedula == 2:
			cedula = input("Digite numero de cedula juridica")
			self.cedulajuridica = cedula	
			print("Cedula Juridica: ", self.cedulajuridica ,"Nombre: ",self.nombre, " Telefono:", self.telefono)

class Vendedor():
    
    def registrarVendedor(self):
		#dic = {}
		#super().__init__()  
		#dic[self.identificacion] = self.nombre, self.telefono
		#print(self.dic)
    	pass

def menu():
	nombre = input("Digite el nombre: ")
	telefono = int(input("Digite el telefono: "))
	cedula = int(input(("Escoja el tipo de cedula: \n"
		"1) Fisica"
		"2) Juridica"
	)))
	contri = Contribuyente(cedula, nombre, telefono)

menu()
   
  

