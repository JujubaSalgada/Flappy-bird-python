import pygame as py
from imgObject import ButtonStart

class Intro():
    def __init__(self, tela):
        self.tela = tela
        self.laco_jogo = True
        self.closeGame = False

        self.background = py.transform.scale(py.image.load('sprites/background1.png').convert_alpha(), (432, 762))
        self.getReady = py.transform.scale(py.image.load('sprites/logo.png').convert_alpha(), (89*3, 24*3))

        self.button = ButtonStart()
        self.buttonGroup = py.sprite.Group()
        self.buttonGroup.add(self.button)

    def rum(self):
        while self.laco_jogo:
            py.time.Clock().tick(50)
            (self.x_mouse, self.y_mouse) = py.mouse.get_pos()
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.laco_jogo = False
                    self.closeGame = True
                if event.type == py.MOUSEBUTTONUP:

                    if self.x_mouse > 130 and self.x_mouse < (130+52*3) and self.y_mouse > 350 and self.y_mouse < (350+29*3):
                        self.laco_jogo = False
            
        
            self.tela.fill('black')
            self.tela.blit(self.background, (0, 0))
            self.tela.blit(self.getReady, (80, 50))
            self.buttonGroup.draw(self.tela)
            py.display.flip()
        