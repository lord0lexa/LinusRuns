import pygame

class obstacle:
    puddle1 = pygame.image.load("data/obstacles/puddle1.png")
    puddle2 = pygame.image.load("data/obstacles/puddle2.png")
    seal = pygame.image.load("data/obstacles/seal.png")
    gull = pygame.image.load("data/obstacles/gull.png")
    obstacles = [puddle1, puddle2, seal, gull]
    hitbox = [[240,70],[220,76],[220,113], [240,163]]
    
