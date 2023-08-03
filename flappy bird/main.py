# Creat by Miquéias Ferreira dos santos 
# GitHub jujubaSalgada / Youtube goticula
# Youtube Channel: https://www.youtube.com/@goticula/videos
# this code was created only for  funny and study


import pygame as py
from imgObject import *
from time import sleep
from random import randint

py.init()

class Game():
    def __init__(self):
        self.tela = py.display.set_mode((432, 762))
        py.display.set_caption("Flip bird - python")
        self.laco_jogo = True
        self.lacoChefe = True

        # Carregando das imagens imagem
        self.background = py.transform.scale(py.image.load('sprites/background1.png').convert_alpha(), (432, 762))
        self.getReady = py.transform.scale(py.image.load('sprites/logo.png').convert_alpha(), (89*3, 24*3))
        self.gameOver = py.transform.scale(py.image.load('sprites/gameOver.png').convert_alpha(), (96*3, 21*3))

        self.fps = py.time.Clock()

    def rum(self):
        while self.lacoChefe:
            self.laco_jogo = True
            self.primeiroClick = False
            self. estadoDoJogo = 'inicial'
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

            while self.laco_jogo:  
                self.fps.tick(50)
                self.yCano = randint(-300, -70)

                # Manipulando o tempo
                self.controlador_tempo += 1
                if self.controlador_tempo == 50:
                    self.segundos += 1
                    self.controlador_tempo = 0

                # Detecção da posição no mouse
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

                if self.colisaoChao or self.colisaoCanoUp or self.colisaoCanoDown:
                    self.estadoDoJogo = 'final'
    
                if self.estadoDoJogo == 'jogando':
                    self.bird.gravidade(self.seconds)

                    # Controlando a aparição de objetos CanoDown
                    self.canoDownList = list(self.canoDownGroup)
                    if self.canoDownList[-1].x == 140:
                        self.canoDownGroup.add(CanoDown(self.yCano))

                    # Controlando a aparição de objetos CanoUp
                    self.canoUpList = list(self.canoUpGroup)
                    if self.canoUpList[-1].x == 140:
                        self.canoUpGroup.add(CanoUp(480+self.yCano+120))
                    
                    self.playerGroup.update()
                    self.groundGroup.update()
                    self.canoDownGroup.update()
                    self.canoUpGroup.update()
                    
                elif self.estadoDoJogo == 'inicial':
                    self.bird.gravidade(self.seconds)
                    self.tela.blit(self.getReady, (80, 50))
                    self.buttonGroup.draw(self.tela)
                    if self.controlador_tempo == 15:
                        self.bird.Click()
                    self.playerGroup.update()
                    self.groundGroup.update()
                
                #Quando o jogador bater em algum lugar / self.estadoDoJogo == 'final' 
                else: 
                    self.tela.blit(self.gameOver, (80, 100))
                    self.buttonGroup.draw(self.tela)
                    

                for event in py.event.get():
                    if event.type == py.QUIT:
                        self.lacoChefe = False
                        self.laco_jogo = False
                    
                    if event.type == py.MOUSEBUTTONUP: #evento de pulo com o clique do mouse
                        if self.estadoDoJogo == 'inicial':
                            if self.x_mouse > 130 and self.x_mouse < (130+52*3) and self.y_mouse > 350 and self.y_mouse < (350+29*3):
                                self.estadoDoJogo = 'jogando'
                                self.canoDownGroup.add(CanoDown(self.yCano))
                                self.canoUpGroup.add(CanoUp(480+self.yCano+120))
                        elif self.estadoDoJogo == 'final':
                            if self.x_mouse > 130 and self.x_mouse < (130+52*3) and self.y_mouse > 350 and self.y_mouse < (350+29*3):
                                self.laco_jogo = False
                        else:
                            self.bird.Click() 
                
                py.display.flip()

game = Game()
game.rum()