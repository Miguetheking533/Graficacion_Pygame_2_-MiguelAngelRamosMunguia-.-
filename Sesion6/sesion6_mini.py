import pygame, random, math
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 6 Mini Proyecto")

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
amarillo = (255, 255, 0)

nave_original = pygame.image.load("C:\\Users\\PC\\Downloads\\nave.png").convert_alpha()
nave_original = pygame.transform.scale(nave_original, (60, 60))

x, y = 400, 300
angulo = 0
velocidad = 5

estrella = pygame.Rect(random.randint(50, 750), random.randint(50, 550), 25, 25)

asteroides = []
for _ in range(8):
    rect = pygame.Rect(random.randint(100, 700), random.randint(100, 500), 40, 40)
    vel_x = random.choice([-4, -3, -2, 2, 3, 4])
    vel_y = random.choice([-3, -2, 2, 3])
    asteroides.append([rect, vel_x, vel_y])

puntos = 0
fuente = pygame.font.Font(None, 36)

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        y -= velocidad
    if teclas[pygame.K_s]:
        y += velocidad
    if teclas[pygame.K_a]:
        x -= velocidad
    if teclas[pygame.K_d]:
        x += velocidad

    if x < 30: x = 30
    if x > 770: x = 770
    if y < 30: y = 30
    if y > 570: y = 570

    nave_rect = pygame.Rect(x - 30, y - 30, 60, 60)

    if nave_rect.colliderect(estrella):
        puntos += 1
        estrella.x = random.randint(50, 750)
        estrella.y = random.randint(50, 550)

    for a in asteroides:
        rect, vx, vy = a

        rect.x += vx
        rect.y += vy

        if rect.x < 0 or rect.x > 760:
            a[1] = -vx
        if rect.y < 0 or rect.y > 560:
            a[2] = -vy

        if nave_rect.colliderect(rect):
            puntos = 0
            x, y = 400, 300

    ventana.fill(negro)
    nave_rotada = pygame.transform.rotate(nave_original, angulo)
    rect_nave = nave_rotada.get_rect(center=(x, y))
    ventana.blit(nave_rotada, rect_nave)

    pygame.draw.rect(ventana, amarillo, estrella)

    for rect, vx, vy in asteroides:
        pygame.draw.circle(ventana, rojo, rect.center, 20)

    texto = fuente.render(f"Puntos: {puntos}", True, blanco)
    ventana.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()