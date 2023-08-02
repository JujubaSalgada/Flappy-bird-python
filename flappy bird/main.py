import pygame as py
from imgObject import Bird
from imgObject import Ground
from imgObject import ButtonStart
from imgObject import CanoUp
from imgObject import CanoDown
from time import sleep
from random import randint
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

        self.canoDownGroup = py.sprite.Group()
        self.canoUpGroup = py.sprite.Group()

        self.buttonGroup = py.sprite.Group()
        self.buttonGroup.add(self.button)

        self.controlador_tempo = 0
        self.segundos = 0

    def rum(self):
        while self.laco_jogo:  
            self.fps.tick(50) # Configuração do fps
            self.yCano = randint(-300, -70)

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
            self.groundGroup.draw(self.tela)
            self.canoDownGroup.draw(self.tela)
            self.canoUpGroup.draw(self.tela)

            # Segundos dentro do laço de x frames por segundo
            self.seconds = self.fps.get_time() / 1000 

            #Controlando a aparição de objetos chão
            self.list_ground = list(self.groundGroup) 
            if self.list_ground[-1].xPosition < 0: 
                self.groundGroup.add(Ground(p=432)) 
            
            
            # Deteção de colisão
            self.colisaoChao = py.sprite.spritecollide(self.bird, self.groundGroup, False) # Pássaro - chão
            self.colisaoCanoUp = py.sprite.spritecollide(self.bird, self.canoUpGroup, False) # Pássaro - canoup
            self.colisaoCanoDown = py.sprite.spritecollide(self.bird, self.canoDownGroup, False) # Pássaro - canodown

            if self.colisaoCanoUp or self.colisaoCanoDown:
                self.laco_jogo = False


            if self.colisaoChao:
                sleep(1)
                self.laco_jogo = False # Vai fechar o laço self.laco_jogo
            else:
                if self.primeiroClick:
                    self.bird.gravidade(self.seconds)

                    #Controlando a aparição de objetos CanoDown
                    self.canoDownList = list(self.canoDownGroup)
                    if self.canoDownList[-1].x == 140:
                        self.canoDownGroup.add(CanoDown(self.yCano))

                    #Controlando a aparição de objetos CanoUp
                    self.canoUpList = list(self.canoUpGroup)
                    if self.canoUpList[-1].x == 140:
                        self.canoUpGroup.add(CanoUp(480+self.yCano+120))
                    
                else:
                    self.bird.gravidade(self.seconds)
                    self.tela.blit(self.getReady, (80, 50))
                    self.buttonGroup.draw(self.tela)
                    if self.controlador_tempo == 15:
                        self.bird.Click()
                
            # Função update dos objetos
            self.playerGroup.update()
            self.groundGroup.update()
            self.canoDownGroup.update()
            self.canoUpGroup.update()

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.laco_jogo = False
                
                if event.type == py.MOUSEBUTTONUP: #evento de pulo com o clique do mouse
                    if self.primeiroClick == False:
                        if self.x_mouse > 130 and self.x_mouse < (130+52*3) and self.y_mouse > 350 and self.y_mouse < (350+29*3):
                            self.primeiroClick = True
                            self.canoDownGroup.add(CanoDown(self.yCano))
                            self.canoUpGroup.add(CanoUp(480+self.yCano+120))
                    else:
                        self.bird.Click() 
            
            py.display.flip()

game = Game()
game.rum()