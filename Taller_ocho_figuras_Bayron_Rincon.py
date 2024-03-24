import turtle
import random

def dibujar_poligono(tortuga, lados, color):
    angulo = 360 / lados
    tortuga.color(color)

    for _ in range(lados):
        tortuga.forward(100)
        tortuga.left(angulo)

def dibujar_figuras_desde_triangulo_a_octagono():
    ventana = turtle.Screen()  # Importante: Aquí importamos Screen
    ventana.bgcolor("white")
    ventana.title("Dibujando polígonos")

    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.speed(2)

    colores = ["red", "green", "blue", "orange", "purple", "yellow", "cyan", "magenta"]

    for lados in range(3, 9):
        # Ajustar la posición inicial para que se dibuje encima del polígono anterior
        tortuga.penup()
        tortuga.setposition(0, 0)
        tortuga.pendown()

        # Dibujar el polígono
        color = random.choice(colores)  # Seleccionar un color aleatorio
        dibujar_poligono(tortuga, lados, color)

    ventana.mainloop()

dibujar_figuras_desde_triangulo_a_octagono()









screen=Screen()
screen.exitonclick()
