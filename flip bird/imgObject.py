import pygame
pygame.init()

class ButtonRetry(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = pygame.image.load('imagens/retry.png').convert_alpha()

        self.image = self.imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = 110, 200


class ButtonStart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = pygame.image.load('imagens/play.png').convert_alpha()

        self.image = self.imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = 50, 220


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.scaleBird = 2
        self.numerator = 0
        self.x = 100
        self.y = 50

        self.imagens = [pygame.transform.scale(pygame.image.load('sprites/bird1.png').convert_alpha(), (17*self.    scaleBird, 12*self.scaleBird)), 
                        pygame.transform.scale(pygame.image.load('sprites/bird2.png').convert_alpha(), (17*self.scaleBird, 12*self.scaleBird)), 
                        pygame.transform.scale(pygame.image.load('sprites/bird3.png').convert_alpha(), (17*self.scaleBird, 12*self.scaleBird))]
        
        self.image = self.imagens[self.numerator]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
    
    def update(self):
        if self.numerator < 2:
            self.numerator += 0.25
        else:
            self.numerator = 0
        self.image = self.imagens[int(self.numerator)]





