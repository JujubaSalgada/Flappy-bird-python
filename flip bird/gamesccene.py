import pygame as py
from imgObject import Bird

class Game():
    def __init__(self, tela):
        self.tela = tela
        self.laco_jogo = True
        self.closeGame = False

        self.background = py.transform.scale(py.image.load('sprites/background1.png').convert_alpha(), (432, 762))

        self.fps = py.time.Clock()
        self.bird = Bird()

        self.playerGroup = py.sprite.Group(self.bird)
        self.groundGroup = py.sprite.Group()


    def rum(self):
        while self.laco_jogo:  
            self.fps.tick(50)
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.closeGame = True # Vai fechar o laço no arquivo Main.py
                    self.laco_jogo = False # Vai fechar o laço self.laco_jogo
                
                if event.type == py.MOUSEBUTTONUP: #evento de pulo com o clique do mouse
                    self.bird.Click() 
                
            self.seconds = self.fps.get_time() / 1000 # Segundos dentro do laço de x frames por segundo
            self.bird.gravidade(self.seconds)

            self.tela.blit(self.background, (0, 0))
            self.playerGroup.draw(self.tela)
            self.playerGroup.update()
            print(self.bird.y_acceleration)
            py.display.flip()

