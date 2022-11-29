
import math
import sys
import time
import pygame as glfw
from OpenGL.GL import *
from numpy import *
import random
from pygame import mixer

# Constantes de tamaño de pantalla

w = 600
h = 600

# Colores parecidos a los propuestos en canvas
purple = (0.2, 0, 0.2)
yellow = (1, 1, 0.5)


# Configuracion inicial
glfw.init()
window = glfw.display.set_mode((w, h), glfw.OPENGL | glfw.DOUBLEBUF)
glfw.mouse.set_pos(w / 2, h / 2)
glfw.display.set_caption("Lab 3 - El Juego del Conway")

# Musica
mixer.init()
mixer.music.load("Conway.mp3")
mixer.music.play(loops=1000)



def EscribirPuntosTexto(lista):
    with open("Conway.txt", "w") as filehandle:
        for listitem in lista:
            filehandle.write("%s\n" % listitem)


# Se definen los puntos iniciales
Coordenadas = [
    [80, 50],
    [90, 50],
    [100, 50],
    [100, 60],
    [90, 70],
    [130, 100],
    [500, 100],
    [150, 100],
    [150, 110],
    [140, 120],
    [50, 100],
    [60, 100],
    [70, 100],
    [180, 150],
    [190, 150],
    [200, 150],
    [200, 160],
    [190, 170],
]


randomNumber = random.randint(1, 5)

# Generacion de figuras "aleatorias" siguiendo algunos patrones comunes de Conway
for i in range(0, randomNumber):
    # Generacion de varios numberos random para la posicion de los puntos
    randomNumber2 = random.randint(100, 200)
    Coordenadas.append([180 + randomNumber2, 150 + randomNumber2])
    Coordenadas.append([190 + randomNumber2, 150 + randomNumber2]),
    Coordenadas.append([200 + randomNumber2, 150 + randomNumber2]),
    Coordenadas.append([200 + randomNumber2, 160 + randomNumber2]),
    Coordenadas.append([190 + randomNumber2, 170 + randomNumber2]),

    Coordenadas.append([90 + randomNumber2, 75 + randomNumber2])
    Coordenadas.append([95 + randomNumber2, 75 + randomNumber2]),
    Coordenadas.append([100 + randomNumber2, 76 + randomNumber2]),
    Coordenadas.append([100 + randomNumber2, 80 + randomNumber2]),
    Coordenadas.append([95 + randomNumber2, 85 + randomNumber2]),


# Defincion de array vacio
limitesPantalla = []
# Constantes
x = 0

funcionar = True
inicial = 0

inicialB = 24
inicialC = 74


# Agregar otra figura random
figuraRandom = random.choice([inicialB, inicialC])


for i in range(0, 5):
    Coordenadas.append([inicial + i, figuraRandom])


def ClearWait():
    FlipScreen()
    time.sleep(1.5)


# Draw a pixel
def pixel(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, 9, 9)
    glClearColor(color[0], color[1], color[2], 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)


# Draw a bar
def pixelBar(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, 10, 100)
    glClearColor(color[0], color[1], color[2], 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)


# Clean screen
def CleanScreen():
    glClearColor(0.0, 0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)


# Flip framebuffer
def FlipScreen():
    glfw.display.flip()


# Algoritmo principal
def conwayGameOfLife(celdas, tamano, actualizarse):

    shapeTuple = (celdas.shape[0], celdas.shape[1])
    celulasVacias = zeros(shapeTuple)
  

    for i, j in ndindex(celdas.shape[0], celdas.shape[1]):
        tempValue1 = i - 1
        tempValue2 = j - 1
        tempValue3 = i + 2
        tempValue4 = j + 2

        # Referencia de slices en python:
        # https://stackoverflow.com/questions/44633798/what-is-the-meaning-of-list-in-this-code
        celdasVivas = sum(celdas[tempValue1:tempValue3, tempValue2:tempValue4])
        celdasVivas = celdasVivas - celdas[i, j]

        if celdas[i, j] == 0:
            color = purple
        else:
            color = yellow

        if celdas[i, j] == 1:
            if celdasVivas < 2:
                if actualizarse == True:
                    color = purple
            if celdasVivas > 3:
                if actualizarse == True:
                    color = purple

            if 2 <= celdasVivas <= 3:
                celulasVacias[i, j] = 1
                if actualizarse == True:
                    color = yellow

        else:
            if celdasVivas == 3:
                celulasVacias[i, j] = 1
                if actualizarse == True:
                    color = yellow

        var1 = i * tamano
        var2 = j * tamano
        pixel((var2), (var1), (color))

    return celulasVacias


w1 = glfw.display.get_window_size()[0]
h1 = glfw.display.get_window_size()[1]
numberOfZerosW = round(w1 / 10)
numberOfZerosH = round(h1 / 10)
numberOfZeros = (numberOfZerosW, numberOfZerosH)
CELDAS = zeros(numberOfZeros)
conwayGameOfLife(CELDAS, 10, False)
FlipScreen()
for i in Coordenadas:
    firstDivision = i[0] / 10
    secondDivision = i[1] / 10
   
    firstDivision = math.ceil(firstDivision)
    secondDivision = math.ceil(secondDivision)
    CELDAS[secondDivision, firstDivision] = 1
    conwayGameOfLife(CELDAS, 10, False)
    FlipScreen()

celdasFuncionando = False


try:
    while funcionar:
        for e in glfw.event.get():
            if e.type == glfw.QUIT:
                funcionar = False
                glfw.quit()
                sys.exit()
            else:
                celdasFuncionando = True
                conwayGameOfLife(CELDAS, 10, False)

            glClear(GL_COLOR_BUFFER_BIT)
            if celdasFuncionando == True:
                CELDAS = conwayGameOfLife(CELDAS, 10, True)
                ClearWait()

except SystemExit:
    glfw.quit()

EscribirPuntosTexto(Coordenadas)
