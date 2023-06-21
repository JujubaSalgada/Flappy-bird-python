import pygame as py
from imgObject import ButtonRetry

class Over():
    def __init__(self, tela):
        self.tela = tela
        self.laco_jogo = True
        self.closeGame = False
        self.fps = py.time.Clock()

        self.imagemGameOver = py.image.load('imagens/gameOver.png')
        self.fundo = py.image.load('imagens/background.jpg')
        self.botaoRetry = ButtonRetry()
        self.grupo = py.sprite.Group(self.botaoRetry)

    def rum(self):
        while self.laco_jogo:
            (self.xMouse, self.yMouse) = py.mouse.get_pos()
            self.fps.tick(20)
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.laco_jogo = False
                    self.closeGame = True

                if event.type == py.MOUSEBUTTONUP:
                    if self.xMouse > 110 and self.xMouse < 201 and self.yMouse > 200 and self.yMouse < 291:
                        self.laco_jogo = False

            self.tela.fill('black')
            self.tela.blit(self.fundo, (0, 0))
            self.tela.blit(self.imagemGameOver, (20, 50))
            self.grupo.draw(self.tela)

            py.display.flip()