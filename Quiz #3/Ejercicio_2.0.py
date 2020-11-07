##clase hacienda
#variables globales
dic_id={}
ID=""
fecha=0
monto=0.0
iva=13
total=0.0
basededatos=""
datosfactura=""

class simulador_hacienda():

	def _init_(self,cedula,nombre,telefono):
		self.cedula=cedula
		self.nombre=nombre
		self.telefono=telefono
	def crear_archivo(self):
		self.basededatos=basededatos
		self.basededatos = open("Vendedores.txt","w")
		
##punto 1-Para registrar un contribuyente se necesita el número de cédula (jurídica o física),  el nombre y el teléfono, 
#la información de las personas registradas debe leerse  por pantalla.
#Cree un programa que permita:
#1- Registrar un vendedor donde se almacena en un diccionario  como llave el ID del vendedor que contenga:
#1.	Nombre del vendedor
#2.	Teléfono

	def registrar_vendedor(self):

		self.dic=dic_id
		self.cedula=ID
		print("Ingrese Datos de Tributacion\n\nPara Registrar Ingrese Numero de Cedula jurídica o física, Nombre y Telefono\n")
		print("1) Fisica: \n2) Juridica: \n")
		self.cedula = int(input(("Escoja el tipo de cedula: "

	    )))
		if self.cedula == 1:
			#self.cedula=int(input("Cedula Juridica: "))
			#nombre=input("Nombre: ")
			#telefono=int(input("Telefono: "))
			print("\n")
			mensaje1=" %-20s %-30s %-20s " % ("nombre","cedula jurídica","telefono")
			mensaje2=" %-20s %-30s %-20s " % (self.nombre,self.cedula,self.telefono)
			print(mensaje1)
			print(mensaje2)
			self.dic[self.cedula]=nombre,telefono
			self.basededatos = open("Vendedores.txt","a")
			self.basededatos.write(str(mensaje1+"\n"))
			self.basededatos.write(str(mensaje2+"\n"))
			self.basededatos.close()
			#print(self.dic)
			print("\n")
		elif self.cedula ==2:
			#elf.cedula=int(input("Cedula Fisica: "))
			#nombre=input("Nombre: ")
			#telefono=int(input("Telefono: "))
			print("\n")
			mensaje1=" %-20s %-30s %-20s " % ("nombre","cedula Fisica","telefono")
			mensaje2=" %-20s %-30s %-20s " % (self.nombre,self.cedula,self.telefono)
			print(mensaje1)
			print(mensaje2)
			self.dic[self.cedula]=nombre,telefono
			self.basededatos = open("Vendedores.txt","a")
			self.basededatos.write(str(mensaje1+"\n"))
			self.basededatos.write(str(mensaje2+"\n"))
			self.basededatos.close()
			#print(self.dic)
			print("\n")


class factura(simulador_hacienda):


	##crea archivo y guarda info
	def crear_archivo_factura(self):

		self.datosfactura=datosfactura
		self.datosfactura = open("Facturas.txt","w")

##punto2-2- Registrar ventas.Permita un diccionario como llave ID del vendedor registrar facturas de ventas de un vendedor, 
#donde se registra una clase factura el cual debe detallar.
#-Id vendedor
#-Fecha factura
#-Monto:
#-Monto IVA. :
#-Monto Total: Monto + Monto IVA
	def Registrar_ventas(self):

		self.fecha=fecha
		self.monto=monto
		self.iva=iva
		self.total=total
		self.dic_ventas=dic_id
		self.reg_cedula=ID

		#print("ID Vendedor",self.cedula)
		self.reg_cedula=int(input("Cedula: "))
		if self.reg_cedula in self.dic:
			self.fecha=input("Fecha factura: ")
			self.monto=float(input("Monto de factura: "))
			self.total = (float(self.monto)+(float(self.monto)*float(self.iva))/100)
		else:
			print("cedula no existe")

##punto3- 3- Imprimir Ventas:Imprimir las ventas registradas de un vendedor que se busca por el ID
#- Nombre del vendedor.
#- fecha factura.
#- monto total.
	def Imprimir_Ventas(self):

		self.reg_cedula=int(input("Ingrese Cedula para consulatar factura: "))
		if self.reg_cedula in self.dic:

			print("\n")
			mensaje1=" %-20s %-20s %-20s %-20s %-20s " % ("ID Vendedor","Fecha de Factura","Monto","IVA","Total +IVA")
			mensaje2=" %-20s %-20s %-20s %-20s %-20s" % (self.cedula,self.fecha,self.monto,self.iva,self.total)
			print(mensaje1)
			print(mensaje2)
			self.dic_ventas[self.cedula]=self.fecha,self.monto,self.iva,self.total
			#print(self.dic_ventas)
			self.basededatos = open("Facturas.txt","a")
			self.basededatos.write(str(mensaje1+"\n"))
			self.basededatos.write(str(mensaje2+"\n"))
			self.basededatos.close()
			print("\n")

		else:
			print("cedula no existe")



##llamo al child (factura) que coge herencia de parent(simulador_hacienda)
mifactura=factura()


opt = 0
while opt != 4:
	print(
	    "1) Registrar Vendedor \n"
	    "2) Registrar Ventas\n"
	    "3) Imprimir Ventas\n"
	    "4) Salir\n"
	)
	opt=int(input("Ingrese una opcion: "))
	if opt == 1:
		cedula=int(input("Cedula Juridica: "))
		nombre=input("Nombre: ")
		telefono=int(input("Telefono: "))
		mifactura.crear_archivo()
		mifactura.registrar_vendedor()
	    
	elif opt ==2:
		mifactura.Registrar_ventas()
	    
	elif opt ==3:
		mifactura.crear_archivo_factura()
		mifactura.Imprimir_Ventas()
		
	elif opt ==4:
		pass