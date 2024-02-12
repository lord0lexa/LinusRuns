import pygame

class obstacle:
    puddle1 = pygame.image.load("data/obstacles/puddle1.png")
    puddle2 = pygame.image.load("data/obstacles/puddle2.png")
    seal = pygame.image.load("data/obstacles/seal.png")
    gull = pygame.image.load("data/obstacles/gull.png")
    obstacles = [puddle1, puddle2, seal, gull]
    hitbox = [[200,60],[130,30],[200,100], [200,120]]
    
