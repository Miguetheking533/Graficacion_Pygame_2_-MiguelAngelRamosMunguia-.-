import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 4 Simulación de Gravedad con perdida del 20% de energia")

blanco = (255, 255, 255)
azul = (0, 0, 255)

x, y = 400, 100
vel_y = 0
gravedad = 0.5
restitucion = 0.8 

radio = 30
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    vel_y += gravedad
    y += vel_y

    if y + radio > 600:
        y = 600 - radio
        vel_y = -vel_y * restitucion

        if abs(vel_y) < 0.5:
            vel_y = 0

    ventana.fill(blanco)
    pygame.draw.circle(ventana, azul, (int(x), int(y)), radio)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
