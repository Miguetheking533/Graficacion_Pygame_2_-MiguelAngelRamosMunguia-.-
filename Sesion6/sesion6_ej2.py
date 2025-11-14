import pygame, random
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 6 Recolección de objetos")

blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)
negro = (0, 0, 0)

jugador = pygame.Rect(400, 300, 60, 60)
velocidad = 5

objeto_x = random.randint(50, 750)
objeto_y = random.randint(50, 550)
radio = 20

puntos = 0
fuente = pygame.font.Font(None, 36)

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

    if jugador.colliderect(pygame.Rect(objeto_x - radio, objeto_y - radio, radio * 2, radio * 2)):
        puntos += 1
        objeto_x = random.randint(50, 750)
        objeto_y = random.randint(50, 550)

    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, jugador)
    pygame.draw.circle(ventana, rojo, (objeto_x, objeto_y), radio)
    texto = fuente.render(f"Puntos: {puntos}", True, negro)
    ventana.blit(texto, (10, 10))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
