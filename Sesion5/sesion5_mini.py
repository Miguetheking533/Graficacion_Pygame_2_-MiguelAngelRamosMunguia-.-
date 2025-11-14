import pygame, math
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 5 Mini proyecto: Nave")

blanco = (255, 255, 255)

nave_original = pygame.image.load("C:\\Users\\PC\\Downloads\\nave.png").convert_alpha()
nave_original = pygame.transform.scale(nave_original, (80, 80)) 
nave = nave_original

x, y = 400, 300
velocidad = 5
angulo = 0

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - x, my - y
    angulo = math.degrees(math.atan2(-dy, dx))
    nave_rotada = pygame.transform.rotate(nave_original, angulo)
    rect = nave_rotada.get_rect(center=(x, y))

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        x += math.cos(math.radians(angulo)) * velocidad
        y -= math.sin(math.radians(angulo)) * velocidad

    ventana.fill(blanco)
    ventana.blit(nave_rotada, rect)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
