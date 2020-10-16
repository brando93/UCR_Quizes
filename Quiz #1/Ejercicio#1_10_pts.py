#Ejercicio 1 (10 puntos)
#Escribir un programa que haga lectura de dos listas e indique si al menos 1 miembro esta en las dos listas
def en_lista():
    total = []
    iphones = [
            "iphone",
            "iphone 3G",
            "iphone 3GS",
            "iphone 4",
            "iphone 4S",
            "iphone 5"
    ]
    celulares = [
        "iphone",
        "Huawei",
        "Samsung",
        "BlackBerry",
        "iphone 4S"
    ]
    for i in iphones:
        for x in celulares:
            if i == x:
                total.append(i)
                break
    print("Los dispositivos que estan en ambas listas son", total)
en_lista()