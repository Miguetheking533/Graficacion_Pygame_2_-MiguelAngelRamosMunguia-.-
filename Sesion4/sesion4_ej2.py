import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 4 - Pulsación")

blanco = (255, 255, 255)
rojo = (255, 0, 0)

radio = 20
cambio = 1
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    radio += cambio

    if radio >= 50 or radio <= 20:
        cambio = -cambio

    ventana.fill(blanco)
    pygame.draw.circle(ventana, rojo, (400, 300), radio)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
