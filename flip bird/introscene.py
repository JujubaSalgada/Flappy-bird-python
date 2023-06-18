import pygame as py

class Intro():
    def __init__(self, tela):
        self.tela = tela
        self.laco_jogo = True
        self.closeGame = False

        self.imgFundo = py.image.load('imagens/background.jpg')
        self.logo = py.image.load('imagens/logo.png')

    def rum(self):
        while self.laco_jogo:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.laco_jogo = False
                    self.closeGame = True
        
            self.tela.fill('black')
            self.tela.blit(self.imgFundo, (0, 0))
            self.tela.blit(self.logo, (40, 10))
            py.display.flip()
        print('Fechou aqui')