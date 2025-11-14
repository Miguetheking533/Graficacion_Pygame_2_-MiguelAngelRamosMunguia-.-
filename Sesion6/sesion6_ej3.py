import pygame, random
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 6 Evitar obstáculos")

blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)
negro = (0, 0, 0)

jugador = pygame.Rect(400, 500, 60, 60)
velocidad = 6

obstaculos = []
for i in range(5):
    x = random.randint(50, 750)
    y = random.randint(50, 550)
    velocidad_x = random.choice([-4, -3, -2, 2, 3, 4])
    obstaculos.append([x, y, velocidad_x])

fuente = pygame.font.Font(None, 50)
reloj = pygame.time.Clock()
corriendo = True
game_over = False

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    if not game_over:

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            jugador.x -= velocidad
        if teclas[pygame.K_RIGHT]:
            jugador.x += velocidad
        if teclas[pygame.K_UP]:
            jugador.y -= velocidad
        if teclas[pygame.K_DOWN]:
            jugador.y += velocidad

        if jugador.x < 0:
            jugador.x = 0
        if jugador.x > 800 - jugador.width:
            jugador.x = 800 - jugador.width
        if jugador.y < 0:
            jugador.y = 0
        if jugador.y > 600 - jugador.height:
            jugador.y = 600 - jugador.height

        for obst in obstaculos:
            obst[0] += obst[2]
            if obst[0] > 780 or obst[0] < 20:
                obst[2] = -obst[2]

        for obst in obstaculos:
            if jugador.colliderect(pygame.Rect(obst[0] - 20, obst[1] - 20, 40, 40)):
                game_over = True

    ventana.fill(blanco)
    if not game_over:
        pygame.draw.rect(ventana, azul, jugador)
        for obst in obstaculos:
            pygame.draw.circle(ventana, rojo, (int(obst[0]), int(obst[1])), 20)
    else:
        texto = fuente.render("¡Game Over!", True, negro)
        ventana.blit(texto, (300, 250))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()