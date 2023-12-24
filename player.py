import pygame 

class Player:
    firstPeng = pygame.image.load('data/peng/pengr.png')
    SecondPeng = pygame.image.load('data/peng/pengl.png')
    jump = pygame.image.load('data/peng/pengjump.png')
    slide = pygame.image.load('data/peng/pengslide.png')
    currentSprite = firstPeng
    position = pygame.Vector2()
    position.xy = 295,100
    velocity = pygame.Vector2()
    velocity.xy = 3, 0
    acceleration = 0.1

    def update_sprite(self, jump, slide):
        if jump == True:
            self.currentSprite = self.jump
            return
        
        if slide == True:
            self.currentSprite = self.slide
            return
        
        if pygame.time.get_ticks() % 500 < 250:
            self.currentSprite = self.SecondPeng
        else:
            self.currentSprite = self.firstPeng

