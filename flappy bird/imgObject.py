import pygame
pygame.init()


class ButtonStart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = pygame.transform.scale(pygame.image.load('sprites/playButton.png').convert_alpha(), (52*3, 29*3))

        self.image = self.imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = 130, 350

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.scaleBird = 2 #Quantidade de vezes que a imagem será ampliada
        self.numerator = 0
        self.x_position = 100 #Posição da imagem em x
        self.y_position = 150 #Posição da imagem em y
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

        if self.y_acceleration > 5 :
            self.image = pygame.transform.rotate(self.image, -10)
        elif self.y_acceleration < 4:
            self.image = pygame.transform.rotate(self.image, 10)
        else:
            self.image = pygame.transform.rotate(self.image, 0)
        
    def gravidade(self, seconds):
        self.time = seconds
        self.f = self.gravity * self.time
        self.y_acceleration += self.f

        self.y_position += self.y_acceleration
        self.rect.topleft = self.x_position, self.y_position

    def Click(self):
        self.y_acceleration = -5

class Ground(pygame.sprite.Sprite):
    def __init__(self, p = 0):
        pygame.sprite.Sprite.__init__(self)
        self.scaleX = 168*3
        self.scaleY = 55*3
        self.xPosition = p
        self.image = pygame.transform.scale(pygame.image.load('sprites/chao.png').convert_alpha(), (self.scaleX, self.scaleY))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.xPosition, (762 - self.scaleY)
    
    def update(self):
        self.xPosition -= 4
        self.rect.topleft = self.xPosition, (762 - self.scaleY)
        if self.xPosition < -432:
            self.kill()

class CanoUp(pygame.sprite.Sprite):
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 452
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('sprites/canoUp.png').convert_alpha(), (26*3, 160*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self):
        self.x -= 4
        self.rect.topleft = self.x, self.y
        if self.x < -100:
            self.kill()

class CanoDown(pygame.sprite.Sprite):
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = 452
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('sprites/canoDown.png').convert_alpha(), (26*3, 160*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,  self.y

    def update(self):
        self.x -= 4
        self.rect.topleft = self.x,  self.y
        if self.x < -100:
            self.kill()

        