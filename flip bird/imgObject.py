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
        self.scaleBird = 2 #Quantidade de vezes que a imagem será ampliada
        self.numerator = 0
        self.x_position = 100 #Posição da imagem em x
        self.y_position = 50 #Posição da imagem em y
        self.y_acceleration = 0 #Aceleração do objeto no eixo y
        self.gravity = 9.807 #Aceleração da gravidade

        #Carregando imagens
        self.imagens = [pygame.transform.scale(pygame.image.load('sprites/bird1.png').convert_alpha(), (17*self.    scaleBird, 12*self.scaleBird)), 
                        pygame.transform.scale(pygame.image.load('sprites/bird2.png').convert_alpha(), (17*self.scaleBird, 12*self.scaleBird)), 
                        pygame.transform.scale(pygame.image.load('sprites/bird3.png').convert_alpha(), (17*self.scaleBird, 12*self.scaleBird))]
        
        self.image = self.imagens[self.numerator] 
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x_position, self.y_position
    
    def update(self):
        if self.numerator < 2:
            self.numerator += 0.25
        else:
            self.numerator = 0
        self.image = self.imagens[int(self.numerator)]
        
    def gravidade(self, seconds):
        self.time = seconds
        self.f = self.gravity * self.time
        self.y_acceleration += self.f

        self.y_position += self.y_acceleration
        self.rect.topleft = self.x_position, self.y_position






