import turtle

dib = turtle.Turtle()
src = turtle.Screen()

# dib.color('red', 'yellow')
# dib.begin_fill()
# while True:
#     dib.forward(200)
#     dib.left(170)
#     if abs(dib.pos()) < 1:
#         break
# dib.end_fill()
# dib.done()
TAM_X = 900
TAM_Y = 700
TAM_Y_1_PORCIENTO = 10
TAM_X_BARRA = 75
TAM_X_SALTO_BARRAS = 100
DESPLAZAMIENTO_TEXTO = 25
COLOR_BASE = "red"

datos = [10, 30, 40, 20]
etiquetas = ["Apro", "Sufi", "Bien", "Sobr"]
colores = ["orange", "lightblue", "yellow", "green"]

# dib.speed(speed="slowest")
dib.hideturtle()
dib.up()
dib.setx(-TAM_X/2)
dib.sety(-TAM_Y/2)
dib.down()
# Cuadrado externo
for _ in range(2):
    dib.forward(TAM_X)
    dib.left(90)
    dib.forward(TAM_Y)
    dib.left(90)

pos_x_actual = -200
pos_y_actual = -200


for valor in range(len(datos)):
    dib.up()
    dib.setpos((pos_x_actual, pos_y_actual))
    dib.down()
    dib.color(COLOR_BASE, colores[valor])
    dib.begin_fill()
    dib.forward(TAM_X_BARRA)
    dib.left(90)
    dib.forward(TAM_Y_1_PORCIENTO * datos[valor])
    dib.left(90)
    dib.forward(TAM_X_BARRA)
    dib.left(90)
    dib.forward(TAM_Y_1_PORCIENTO * datos[valor])
    dib.left(90)
    dib.end_fill()
    dib.up()
    dib.setpos((pos_x_actual + DESPLAZAMIENTO_TEXTO, pos_y_actual + TAM_Y_1_PORCIENTO * datos[valor] + DESPLAZAMIENTO_TEXTO))
    dib.write(str(datos[valor]) + "%")
    dib.setpos((pos_x_actual + DESPLAZAMIENTO_TEXTO, pos_y_actual - DESPLAZAMIENTO_TEXTO))
    dib.write(etiquetas[valor])

    pos_x_actual += TAM_X_SALTO_BARRAS

input("")
