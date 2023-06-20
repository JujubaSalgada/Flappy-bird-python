import pygame as py
from imgObject import Bird

class Game():
    def __init__(self, tela):
        self.tela = tela
        self.laco_jogo = True
        self.closeGame = False
        self.fps = py.time.Clock()
        self.bird = Bird()
        self.grupo = py.sprite.Group(self.bird)


    def rum(self):
        while self.laco_jogo:
            self.fps.tick(30)
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.closeGame = True # Vai fechar o laço no arquivo Main.py
                    self.laco_jogo = False # Vai fechar o laço self.laco_jogo
        
            self.tela.fill('blue')
            self.grupo.draw(self.tela)
            self.grupo.update()
            py.display.flip()

        print('Fechou aqui')

