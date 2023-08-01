import pygame as py
from imgObject import Bird
from imgObject import Ground
from imgObject import ButtonStart
from time import sleep
py.init()

class Game():
    def __init__(self):
        self.tela = py.display.set_mode((432, 762))
        py.display.set_caption("Flip bird - python")
        self.laco_jogo = True
        self.primeiroClick = False

        # Carregando das imagens imagem
        self.background = py.transform.scale(py.image.load('sprites/background1.png').convert_alpha(), (432, 762))
        self.getReady = py.transform.scale(py.image.load('sprites/logo.png').convert_alpha(), (89*3, 24*3))

        self.fps = py.time.Clock()
        self.bird = Bird()
        self.button = ButtonStart()

        # Declarando os grupos de sprites 
        self.playerGroup = py.sprite.Group()
        self.playerGroup.add(self.bird)
        self.groundGroup = py.sprite.Group()
        self.groundGroup.add(Ground())
        self.canoGroup = py.sprite.Group()
        self.buttonGroup = py.sprite.Group()
        self.buttonGroup.add(self.button)

        self.controlador_tempo = 0
        self.segundos = 0

    def rum(self):
        while self.laco_jogo:  
            self.fps.tick(50) # Configuração do fps

            # Manipulando o tempo
            self.controlador_tempo += 1
            if self.controlador_tempo == 50:
                self.segundos += 1
                self.controlador_tempo = 0

            #Detecção da posição no mouse
            (self.x_mouse, self.y_mouse) = py.mouse.get_pos()

            # Desenhando sprites na tela
            self.tela.blit(self.background, (0, 0))
            self.playerGroup.draw(self.tela)
            self.canoGroup.draw(self.tela)
            self.groundGroup.draw(self.tela)

            # Segundos dentro do laço de x frames por segundo
            self.seconds = self.fps.get_time() / 1000 

            self.list_ground = list(self.groundGroup) #Lista com os elementos do grupo chão
            if self.list_ground[-1].xPosition < 0: #Controlando a aparição de objetos chão
                self.groundGroup.add(Ground(p=432)) 
            
            # Deteção de colisão
            self.colisaoChao = py.sprite.spritecollide(self.bird, self.groundGroup, False) # Pássaro - chão
            if self.colisaoChao:
                sleep(1)
                self.laco_jogo = False # Vai fechar o laço self.laco_jogo
            else:
                if self.primeiroClick:
                    self.bird.gravidade(self.seconds)
                else:
                    self.bird.gravidade(self.seconds)
                    self.tela.blit(self.getReady, (80, 50))
                    self.buttonGroup.draw(self.tela)
                    if self.controlador_tempo == 15:
                        self.bird.Click()
                
            # Geração aleátoria de canos

        
            # Função update dos objetos
            self.playerGroup.update()
            self.groundGroup.update()
            self.canoGroup.update()

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.laco_jogo = False
                
                if event.type == py.MOUSEBUTTONUP: #evento de pulo com o clique do mouse
                    if self.primeiroClick == False:
                        if self.x_mouse > 130 and self.x_mouse < (130+52*3) and self.y_mouse > 350 and self.y_mouse < (350+29*3):
                            self.primeiroClick = True
                    else:
                        self.bird.Click() 
            
            py.display.flip()

game = Game()
game.rum()