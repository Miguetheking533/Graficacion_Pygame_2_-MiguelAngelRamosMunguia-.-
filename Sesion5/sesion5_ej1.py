import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 5 Ajuste de tamaño dinámico")

blanco = (255, 255, 255)

imagen_original = pygame.image.load("C:\\Users\\PC\\Downloads\\MX_logo.png").convert_alpha()

escala = 1.0
imagen = imagen_original
ancho_original, alto_original = imagen_original.get_size()

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:
                escala += 0.1

            elif evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                escala = max(0.1, escala - 0.1)


            nuevo_ancho = int(ancho_original * escala)
            nuevo_alto = int(alto_original * escala)
            imagen = pygame.transform.smoothscale(imagen_original, (nuevo_ancho, nuevo_alto))

    ventana.fill(blanco)

    rect = imagen.get_rect(center=(400, 300))
    ventana.blit(imagen, rect)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
