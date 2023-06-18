import pygame as py
from imgObject import ButtonStart

class Intro():
    def __init__(self, tela):
        self.tela = tela
        self.laco_jogo = True
        self.closeGame = False

        self.imgFundo = py.image.load('imagens/background.jpg')
        self.logo = py.image.load('imagens/logo.png')

        self.botao = ButtonStart()
        self.grupo = py.sprite.Group(self.botao)
        

    def rum(self):
        while self.laco_jogo:
            (self.xMouse, self.yMouse) = py.mouse.get_pos()
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.laco_jogo = False
                    self.closeGame = True
                
                if event.type == py.MOUSEBUTTONUP:
                    if self.xMouse > 50 and self.xMouse < 250 and self.yMouse > 220 and self.yMouse < 420:
                        self.laco_jogo = False
            
        
            self.tela.fill('black')
            self.tela.blit(self.imgFundo, (0, 0))
            self.tela.blit(self.logo, (40, 10))
            self.grupo.draw(self.tela)
            py.display.flip()
        