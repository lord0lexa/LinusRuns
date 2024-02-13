import pygame

class background:
    background = pygame.image.load("data/bg/bg.png")
    snow1 = pygame.image.load("data/bg/Snow1.png")
    snow2 = pygame.image.load("data/bg/Snow2.png")
    currentSnow = snow1
    floor1 = pygame.image.load("data/bg/Ice1.png")
    floor2 = pygame.image.load("data/bg/Ice2.png")
    lostGame = pygame.image.load("data/bg/lost.png")

    #testing coordinates
    coordinates = pygame.image.load("data/bg/koordinaten.png")

    def update_Snow(self):
        if pygame.time.get_ticks() % 800 < 400:
            self.currentSnow = self.snow2
        else:
            self.currentSnow = self.snow1