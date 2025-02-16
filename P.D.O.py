import pygame
from p import pastor

Jugador = pastor (50,50)

pygame.init()

pygame.display.set_caption("Ovejero")

ancho,alto = 1400,800
ventana = pygame.display.set_mode((ancho, alto))

run = True
while run :

    Jugador.draw(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
