import pygame
pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sesión 5 Sprite animado")

blanco = (255, 255, 255)

sprite_sheet = pygame.image.load("C:\\Users\\PC\\Downloads\\humans.jpg").convert_alpha()

frame_ancho = sprite_sheet.get_width() // 4
frame_alto = sprite_sheet.get_height()

frames = []
for i in range(4):
    rect = pygame.Rect(i * frame_ancho, 0, frame_ancho, frame_alto)
    frame = sprite_sheet.subsurface(rect)
    frames.append(frame)

reloj = pygame.time.Clock()
tiempo_cambio = 100 
ultimo_cambio = 0
frame_actual = 0

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_cambio >= tiempo_cambio:
        frame_actual = (frame_actual + 1) % len(frames)
        ultimo_cambio = tiempo_actual

    ventana.fill(blanco)
    ventana.blit(frames[frame_actual], (350, 250))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
