import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Atari Pong - Versión Básica")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Puntuación
puntos_a = 0
puntos_b = 0

# Paleta A (Jugador 1)
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.color("white")
paleta_a.shapesize(stretch_wid=5, stretch_len=1)
paleta_a.penup()
paleta_a.goto(-350, 0)

# Paleta B (IA / Jugador 2)
paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.color("white")
paleta_b.shapesize(stretch_wid=5, stretch_len=1)
paleta_b.penup()
paleta_b.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.15
pelota.dy = 0.15

# Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador: 0  |  IA: 0", align="center", font=("Courier", 24, "normal"))

# Funciones de movimiento
def paleta_a_arriba():
    y = paleta_a.ycor()
    if y < 240:
        paleta_a.sety(y + 20)

def paleta_a_abajo():
    y = paleta_a.ycor()
    if y > -240:
        paleta_a.sety(y - 20)

# Teclado
ventana.listen()
ventana.onkeypress(paleta_a_arriba, "w")
ventana.onkeypress(paleta_a_abajo, "s")

# Bucle principal del juego
while True:
    ventana.update()

    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Colisión con bordes superiores/inferiores
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Colisión con bordes laterales (Puntuación)
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntos_a += 1
        marcador.clear()
        marcador.write(f"Jugador: {puntos_a}  |  IA: {puntos_b}", align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        puntos_b += 1
        marcador.clear()
        marcador.write(f"Jugador: {puntos_a}  |  IA: {puntos_b}", align="center", font=("Courier", 24, "normal"))

    # IA simple para la paleta B (sigue a la pelota)
    if paleta_b.ycor() < pelota.ycor() and abs(paleta_b.ycor() - pelota.ycor()) > 10:
        if paleta_b.ycor() < 240:
            paleta_b.sety(paleta_b.ycor() + 0.1)
    elif paleta_b.ycor() > pelota.ycor() and abs(paleta_b.ycor() - pelota.ycor()) > 10:
        if paleta_b.ycor() > -240:
            paleta_b.sety(paleta_b.ycor() - 0.1)

    # Colisión paleta y pelota
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta_b.ycor() + 50 and pelota.ycor() > paleta_b.ycor() - 50):
        pelota.setx(340)
        pelota.dx *= -1

    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta_a.ycor() + 50 and pelota.ycor() > paleta_a.ycor() - 50):
        pelota.setx(-340)
        pelota.dx *= -1