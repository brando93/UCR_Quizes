# Universidad Tres Patitos
def program(): 
    alumnos_all = {}
    alumno_info = []
    becas = {}
    while True:
        try:
            print( #MENU
                "\n"
                "Universidad Tres Patitos\n"
                "\n"
                "1) Control de Estudiantes\n" 
                "2) Becas\n" 
                "3) Salir\n"  
            )
            opcion = int(input("Digite una opcion: "))
            if opcion == 1: # CONTROL DE ESTUDIANTE
                print("1) Registro de nuevo estudiante:\n")
                print("2) Listar los estudiantes (Activos):\n")
                print("3) Cambiar estado de estudiante (Activos/Pasivos):\n")
                "\n"
                opcion1 = int(input("Digite una opcion: "))
                if opcion1 == 1: # REGISTRARR ESTUDIANTE
                    numero_carne = int(input("Numero de Carne: "))
                    if numero_carne not in alumnos_all:
                        nombre_estudiante = input("Nombre Completo: ").lower()
                        carrera = input("Carrera: ").lower()
                        while True:
                            estudiante_estado = input("Estado (Activo/Inactivo): ").lower()
                            if estudiante_estado == "activo" or "inactivo":
                                anho_ingreso = int(input("Anho de Ingreso: "))
                                alumno_info = [nombre_estudiante, carrera, estudiante_estado, anho_ingreso]
                                alumnos_all[numero_carne] = alumno_info
                                break
                            else:
                                print("Tiene que ser Activo/Inactivo")        
                    else:
                        print("Ya existe el carne")
                elif opcion1 == 2: #LISTAR ESTUDIANTES ACTIVOS
                    item = "activo"
                    for key in alumnos_all.keys():
                        if item in alumnos_all[key]:
                            print("Carne #", key)
                            print("Information:" ,alumnos_all[key]) 
                            print("------------------------------------------------")  
                elif opcion1 == 3: #CAMBIAR ESTADO DE ESTUDIANTE ACTIVO/INACTIVO
                    numero_carne1 = int(input("Digite el Numero de Carne: "))
                    if numero_carne1 in alumnos_all.keys():
                        for key in alumnos_all.keys():
                            if numero_carne1 == key:
                                print("---------------------------")
                                print("Carne #", numero_carne1)
                                print("Nombre",  alumnos_all[key][0])
                                print("Estado:" ,alumnos_all[key][2])
                                cambio_status = input("Cambiar estado? (y/n) : ").lower()
                                print("---------------------------")
                                if alumnos_all[key][2] == "inactivo":
                                    alumnos_all[key][2] = "activo"
                                    print("CAMBIADO >> ", alumnos_all[key])
                                else:
                                    alumnos_all[key][2] = "inactivo"
                                    print("CAMBIADO >> ", alumnos_all[key])
                    else:
                        print("Invalid Opcion")
                else:
                    print("Invalid Opcion")
            elif opcion == 2: #BECAS
                print("1) Registro de becas:\n")
                print("2) Becar estudiante:\n")
                opcion2 = int(input("Digite una opcion: "))
                if opcion2 == 1: # REGISTRO DE BECAS
                    numero_beca = int(input("Numero de beca: "))
                    descuento_aplicar = int(input("Porcentaje de Descuento a aplicar : "))
                    becas[numero_beca] = descuento_aplicar
                    for key, value in becas.items():
                        print("Beca ---> #",key)
                        print("Descuento ---> ",value,"%")
                elif opcion2 == 2: # BECAR ESTUDIANTE
                    numero_carne1 = int(input("Digite el Numero de Carne: "))
                    if numero_carne1 in alumnos_all.keys():
                        print("Encontrado ", alumnos_all[numero_carne1])
                        numero_beca = int(input("Numero de beca: "))
                        if numero_beca in becas.keys():
                            print("Informacion de gestion:\n", alumnos_all[numero_carne1])
                            print("Beca: [ #",numero_beca,", " ,"%", becas[numero_beca],"]")
                    else:
                        print("Numero de Carne no existe")              
                else:
                    print("Invalid Opcion")
            elif opcion == 3: #SALIR
                break
        except: 
            print("Invalid Option")
            continue
program()