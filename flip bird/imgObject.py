import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = pygame.image.load('imagens/retry.png').convert_alpha()

        self.image = self.imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = 110, 200



