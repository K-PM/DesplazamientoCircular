import pygame
import math

# Función para calcular el radio
def calcular_radio(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    radio = distancia / 2
    return radio

ancho_pantalla = 800
alto_pantalla = 600

# Crea una ventana de 800x600 píxeles
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Establece el color de fondo
color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)

# Coordenadas de los puntos iniciales y finales
x1, y1, x2, y2 = 0, 0, 0, 0

# Variable para controlar el primer clic
primer_click = False

# Bucle principal
while True:
    # Obtiene los eventos del usuario
    eventos = pygame.event.get()    
    # Maneja los eventos
    for evento in eventos:
        if evento.type == pygame.QUIT or evento.type==pygame.K_ESCAPE:
            # Sale del bucle y termina el programa si se cierra la ventana
            pygame.quit()            
            exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = evento.pos
            primer_click = True

        if evento.type == pygame.MOUSEMOTION:
            if primer_click:
                x2, y2 = evento.pos
                radio = calcular_radio(x1, y1, x2, y2)
                ventana.fill(color_pantalla)  # Limpia la ventana
                pygame.draw.circle(ventana, color_dibujo, (x1, y1), int(radio))
                pygame.draw.circle(ventana, color_pantalla, (x1, y1), radio-2)

        if evento.type == pygame.MOUSEBUTTONUP:
            primer_click = False

    # Actualiza la ventana
    pygame.display.update()