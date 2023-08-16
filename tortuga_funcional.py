import turtle

turtle.setup(600, 600)    #ventana
turtle.bgcolor("black")     #fondo ventana
turtle.color("white")       #color linea

#turtle.register_shape("raton_2.gif")
turtle.shape("turtle")
#turtle.speed(0)     # velocidad
turtle.width(6)     #grueso de la linea
turtle.setheading(90)


def mostrar_menu ():
    print("Las teclas para jugar con las siguientes :")
    print(":::::::::::::::::::::::::::::::::::::::::")
    print(" Para avanzar presione: W")
    print(" Para ir a la derecha presiones: D")
    print(" Para ir a la izquierda presione: A")
    print(" Para ir hacia atras presione: S")
    print(" Para realizar la diagonal derecha presiona 'E' ")
    print(" Para realizar la diagonal Izquierda presiona 'Q' ")
    print(" ..................................")

def avanzar():
    turtle.forward(40)

def derecha():
    turtle.right(90)
    turtle.forward(40)

def izqu():
    turtle.left(90)
    turtle.forward(40)

def atras():
    turtle.back(40)

def diag_dere():
    grados = int(input("Cuantos grados quieres girar hacia la derecha : "))
    turtle.right(grados)
    turtle.back(-40)

def diag_izq():
    grados = int(input("Cuantos grados quieres girar hacia la izquierda : "))
    turtle.left(grados)
    turtle.back(-40) 


while True :
    mostrar_menu()
    cadena = input(" Que accion desea realizar :")

    mov = [caracter for caracter in cadena]

    for i in mov:
        if i == 'W' or i == 'w':
            avanzar()
        elif i == 'D' or i == 'd':
            derecha()
        elif i == 'A' or i == 'a':
            izqu()
        elif i == 'S' or i == 's':
            atras()
        elif i == 'E' or i == 'e':
            diag_dere()
        elif i == 'Q' or i == 'q':
            diag_izq()
        elif i == range(0, 100):
            print("Digito ingrsado no se encuentra de la cadena, no es automata.")
            break
        else:
            print("Error, no se admite la entrada; el programa no es automata.")
            break

turtle.Screen().exitonclick()