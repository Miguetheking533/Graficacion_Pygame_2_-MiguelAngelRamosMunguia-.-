import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 4 Rebote con velocidad variable de 0.1")

blanco = (255, 255, 255)
rojo = (255, 0, 0)

x, y = 400, 300
velocidad_x = 5
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    x += velocidad_x

    if x > 770 or x < 30:
        velocidad_x = -velocidad_x
        if velocidad_x > 0:
            velocidad_x += 0.1
        else:
            velocidad_x -= 0.1

    ventana.fill(blanco)
    pygame.draw.circle(ventana, rojo, (int(x), y), 30)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
