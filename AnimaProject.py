import pygame
import math

# Función para calcular el radio
def calcular_radio(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    radio = distancia / 2
    return radio

pygame.init()
ancho_pantalla = 800
alto_pantalla = 600
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Animación de Círculo y Línea")


color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)
x1, y1, x2, y2 = 0, 0, 0, 0
dibujando = False
radio = 10
ruta = []

while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: 
                x1, y1 = evento.pos
                dibujando = True
                ruta = []  
            elif evento.button == 3:  
                x1, y1 = evento.pos
                radio = 6

        if evento.type == pygame.MOUSEMOTION:
            if dibujando and pygame.mouse.get_pressed()[0]: 
                x2, y2 = evento.pos
                ruta.append((x2, y2))

            elif pygame.mouse.get_pressed()[2]:  
                x2, y2 = evento.pos
                radio = calcular_radio(x1, y1, x2, y2)

        # Dibujar el círculo y el dibujo a mano alzada
        ventana.fill(color_pantalla)
        pygame.draw.circle(ventana, color_dibujo, (x1, y1), int(radio), 1)

        if len(ruta) >= 2:
            pygame.draw.lines(ventana, color_dibujo, False, ruta, 1)

        pygame.display.update()

        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1: 
                dibujando = False
                pygame.time.delay(500)
# Desplazar el círculo a lo largo de la línea
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            
            if len(ruta) >= 2:
                steps = 100
                for step in range(1, steps + 1):
                    percentage = step / steps
                    index = int((len(ruta) - 1) * percentage)
                    x, y = ruta[index]
                    ventana.fill(color_pantalla)
                    pygame.draw.circle(ventana, color_dibujo, (int(x), int(y)), int(radio), 1)
                    pygame.draw.lines(ventana, color_dibujo, False, ruta, 1)

                    pygame.display.update()
                    pygame.time.delay(20)

                # Borrar únicamente la línea 
                ventana.fill(color_pantalla)
                pygame.draw.circle(ventana, color_dibujo, (int(x), int(y)), int(radio), 1)
                pygame.display.update()
                pygame.time.delay(500)
