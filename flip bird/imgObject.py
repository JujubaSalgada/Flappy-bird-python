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



