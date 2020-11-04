"""
El presente examen corto tiene como fecha de entrega el lunes 9 de noviembre a las 11:59 p.m.
Ejercicio 1 (40 puntos)
1- Desarrollar un programa que conste de una clase padre Cuenta  que contenga:
1.	Atributos:   titular  tipo texto   y cantidad tipo entero
2.	Método para imprimir los datos en la clase Cuenta.
Definir dos clases PlazoFijo y CajaAhorro que herede de la clase Cuenta, donde
1.	La clase CajaAhorro  
1.	Defina el __init__ que pase los datos heredados de la Clase Cuenta
2.	Tendrá un método para mostrar la información.
2.	La clase PlazoFijo tendrá:
1.	Defina el __init__ que pase los datos heredados de la Clase Cuenta ademas tener un atributo plazo  tipo entero e interés tipo flotante.
2.	Métodos:
1.	Método para obtener el importe del interés  que debe devolver el resultado de (cantidad*interés/100)
2.	Método para mostrar la información, datos del titular plazo, interés y total de interés.
Cree un programa principal donde defina una variable de PlazoFijo y CajaAhorro, llene información necesaria y valide la funcionalidad de cada método.
"""

class Cuenta():
    
    def __init__(self,titular,cantidad):
        self.titular = str(titular)
        self.cantidad = int(cantidad)
        
    def imprimir(self):
        print( "Titutlar: ", self.titular, "Cantidad: ", self.cantidad)
    
class CajaAhorro(Cuenta):
    
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
    
class PlazoFijo(Cuenta):
    
    def __init__(self,plazo,interes):
        super().__init__(plazo,interes)
        self.plazo = int(plazo)
        self.interes = float(interes)
        self.porcentaje = 0
        
    def ImporteInteres(self):
        self.porcentaje = (self.cantidad*self.interes/100)
        
    def mostrarInfo(self):
        print("Plazo: ",self.plazo, "Interes: ",self.interes, "Porcentaje: ",self.porcentaje)


nombre = input("Ingrese Nombre: ")
cantidad = int(input("Ingrese cantidad: "))
plazo = int(input("Ingrese plazo: "))
interes = float(input("Ingrese interes: "))

CajaAhorro1=CajaAhorro(nombre,cantidad)
PlazoFijo1=PlazoFijo(plazo,interes)
CajaAhorro1.imprimir()
PlazoFijo1.ImporteInteres()
PlazoFijo1.mostrarInfo()
