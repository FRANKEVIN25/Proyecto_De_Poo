import pygame
from game import Personaje, Mapa, Alimento

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Creación de objetos
principal = Personaje(1, 1, "personaje")
mapa = Mapa("mapa.txt")
alimento = Alimento(5, 5, "chatarra1")


# Bucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Captura eventos de teclado para mover al personaje
            if event.key == pygame.K_UP:
                principal.move(0, -1)
            elif event.key == pygame.K_DOWN:
                principal.move(0, 1)
            elif event.key == pygame.K_LEFT:
                principal.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                principal.move(1, 0)

    #Alimento persigue al personaje
    if alimento.x < principal.x:
        alimento.x += 1
    elif alimento.x > principal.x:
        alimento.x -= 0

    if alimento.y < principal.y:
        alimento.y += 0
    elif alimento.y > principal.y:
        alimento.y -= 1

    # Dibuja el fondo y el mapa
    screen.fill((128, 128, 128))  # Rellena con un color de fondo (gris claro)
    mapa.draw(screen)

    # Dibuja el personaje
    principal.draw(screen)

    # Dibuja el alimento
    alimento.draw(screen)

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla el FPS
    clock.tick(60)  # Limita la velocidad de fotogramas a 60 FPS

pygame.quit()