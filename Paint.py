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

# Variable para controlar el modo de dibujo
dibujar_circulo = False
dibujar_linea = False

# Lista para almacenar los puntos de la línea a mano alzada
puntos_linea = []

# Bucle principal
while True:
    # Obtiene los eventos del usuario
    eventos = pygame.event.get()    
    # Maneja los eventos
    for evento in eventos:
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            # Sale del bucle y termina el programa si se cierra la ventana o se presiona Esc
            pygame.quit()            
            exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = evento.pos
            if evento.button == 1:  # Botón izquierdo para dibujar círculos
                dibujar_circulo = True
                inicio = (x0, y0)
                final = inicio
            elif evento.button == 3:  # Botón derecho para dibujar líneas a mano alzada
                dibujar_linea = True
                puntos_linea = [(x0, y0)]  # Inicia la lista con el primer punto

        if evento.type == pygame.MOUSEMOTION:
            if dibujar_circulo:
                x1, y1 = evento.pos
                radio = calcular_radio(inicio[0], inicio[1], x1, y1)
                ventana.fill(color_pantalla)  # Limpia la ventana
                pygame.draw.circle(ventana, color_dibujo, inicio, int(radio))
                pygame.draw.circle(ventana, color_pantalla, inicio, int(radio) - 2)
            elif dibujar_linea:
                x1, y1 = evento.pos
                puntos_linea.append((x1, y1))  # Agrega el nuevo punto

                ventana.fill(color_pantalla)  # Limpia la ventana
                if len(puntos_linea) > 1:
                    pygame.draw.lines(ventana, color_dibujo, False, puntos_linea, 2)  # Dibuja la línea con grosor 2

        if evento.type == pygame.MOUSEBUTTONUP:
            if dibujar_circulo:
                dibujar_circulo = False
            elif dibujar_linea:
                dibujar_linea = False

    # Actualiza la ventana
    pygame.display.update()
