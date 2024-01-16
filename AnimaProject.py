import pygame
import math

# Función para calcular el radio
def calcular_radio(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    radio = distancia / 2
    return radio

# Función para limpiar la pantalla
def limpiar_pantalla():
    ventana.fill(color_pantalla)

ancho_pantalla = 800
alto_pantalla = 600

# Crea una ventana de 800x600 píxeles
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Establece el color de fondo
color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)

# Variable para el círculo dibujado actual
circulo_dibujado = None

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
                if circulo_dibujado is not None:
                    # Si hay un círculo dibujado, lo borra antes de dibujar uno nuevo
                    r = calcular_radio(circulo_dibujado['inicio'][0], circulo_dibujado['inicio'][1],
                                       circulo_dibujado['final'][0], circulo_dibujado['final'][1])
                    limpiar_pantalla()
                # Inicia el nuevo círculo
                inicio = (x0, y0)
                final = inicio

        if evento.type == pygame.MOUSEMOTION:
            if evento.buttons[0] and circulo_dibujado is not None:
                # Si el botón izquierdo del mouse está presionado y hay un círculo dibujado,
                # borra el círculo antes de dibujar uno nuevo
                r = calcular_radio(circulo_dibujado['inicio'][0], circulo_dibujado['inicio'][1],
                                   circulo_dibujado['final'][0], circulo_dibujado['final'][1])
                limpiar_pantalla()

            if circulo_dibujado is not None:
                # Dibuja el círculo actual en movimiento
                x1, y1 = evento.pos
                radio = calcular_radio(inicio[0], inicio[1], x1, y1)
                pygame.draw.circle(ventana, color_dibujo, inicio, int(radio))
                pygame.draw.circle(ventana, color_pantalla, inicio, int(radio) - 2)

        if evento.type == pygame.MOUSEBUTTONUP:
            if circulo_dibujado is not None:
                # Cuando se suelta el botón del mouse, guarda las coordenadas finales del círculo dibujado
                final = (x1, y1)
                circulo_dibujado = {'inicio': inicio, 'final': final}
            else:
                # Si no hay un círculo dibujado, crea uno nuevo
                final = (x1, y1)
                circulo_dibujado = {'inicio': inicio, 'final': final}

    # Dibuja el círculo dibujado actual
    if circulo_dibujado is not None:
        r = calcular_radio(circulo_dibujado['inicio'][0], circulo_dibujado['inicio'][1],
                           circulo_dibujado['final'][0], circulo_dibujado['final'][1])
        pygame.draw.circle(ventana, color_dibujo, circulo_dibujado['inicio'], int(r))
        pygame.draw.circle(ventana, color_pantalla, circulo_dibujado['inicio'], int(r) - 2)

    # Actualiza la ventana
    pygame.display.update()
