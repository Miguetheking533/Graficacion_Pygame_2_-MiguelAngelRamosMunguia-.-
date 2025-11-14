import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 6 Colisión con cambio de color")

blanco = (255, 255, 255)
azul = (0, 0, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)

jugador = pygame.Rect(400, 300, 60, 60)
objetivo = pygame.Rect(200, 200, 40, 40)

velocidad = 5
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad

    color_jugador = verde if jugador.colliderect(objetivo) else azul

    ventana.fill(blanco)
    pygame.draw.rect(ventana, color_jugador, jugador)
    pygame.draw.rect(ventana, rojo, objetivo)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
