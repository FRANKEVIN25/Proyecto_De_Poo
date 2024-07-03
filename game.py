import pygame

class Personaje:
    def __init__(self, x, y, tipo, health=100):
        self.x = x
        self.y = y
        self.type = tipo
        self.health = health
        self.image = pygame.image.load(tipo + ".png")

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self, screen):
        screen.blit(self.image, (self.x * 40, self.y * 40))

class Alimento:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.type = tipo
        self.image = pygame.image.load(tipo + ".png")

    def draw(self, screen):
        screen.blit(self.image, (self.x * 40, self.y * 40))

class Mapa:
    def __init__(self, mapa):
        self.tile1 = pygame.image.load("pared.png")
        self.tile2 = pygame.image.load("pared2.png")
        self.tile3 = pygame.image.load("pared3.png")

        self.matrix = []
        with open(mapa, "r", encoding="utf-8") as file:
            for line in file:
                line = line.split('#')[0].strip()  # Eliminar comentarios y espacios
                if line:  # Ignorar líneas vacías
                    self.matrix.append(list(line))

    def draw(self, screen):
        for y, row in enumerate(self.matrix):
            for x, tile in enumerate(row):
                if tile == "A":
                    screen.blit(self.tile1, (x * 40, y * 40))
                elif tile == "B":
                    screen.blit(self.tile2, (x * 40, y * 40))
                elif tile == "C":
                    screen.blit(self.tile3, (x * 40, y * 40))