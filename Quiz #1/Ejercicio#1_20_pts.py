#Ejercicio 1 (20 puntos)
#Realice un programa donde se le escribe una palabra e indique si es palíndromo (es decir, palabras que
#tienen el mismo aspecto escritas invertidas), ejemplos; ana, ala, arenera, arepera, anilina, aviva,
#Malayalam, Menem, Neuquen, oro, Oruro, oso, ojo, radar, reconocer, rotor, salas, seres, somos,
#sometemos,mama. 

txt = input("Digite una palabra: ")
txt1 = txt[::-1]
print("normal: ", txt)
print("inverso: ", txt1)
if txt == txt1:
    print("****************************")
    print(txt,"es palindromo")
    print("****************************")
else:
    print("****************************")
    print(txt,"no es palindromo")
    print("****************************")



            
        
