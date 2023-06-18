import pygame as py

class Game():
    def __init__(self, tela):
        self.tela = tela
        self.laco_jogo = True
        self.closeGame = False

    def rum(self):
        while self.laco_jogo:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.closeGame = True
                    self.laco_jogo = False
        
            self.tela.fill('blue')
            py.display.flip()

        print('Fechou aqui')

