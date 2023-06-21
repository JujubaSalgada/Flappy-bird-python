import pygame as py
from imgObject import Bird
from imgObject import Ground
from time import sleep

class Game():
    def __init__(self, tela):
        self.tela = tela
        self.laco_jogo = True
        self.closeGame = False

        # Carregando imagem de fundo
        self.background = py.transform.scale(py.image.load('sprites/background1.png').convert_alpha(), (432, 762))

        self.fps = py.time.Clock()
        self.bird = Bird()

        # Declarando os grupos de sprites 
        self.playerGroup = py.sprite.Group()
        self.playerGroup.add(self.bird)
        self.groundGroup = py.sprite.Group()
        self.groundGroup.add(Ground())


    def rum(self):
        while self.laco_jogo:  
            self.fps.tick(50) # Configuração do fps
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.closeGame = True # Vai fechar o laço no arquivo Main.py
                    self.laco_jogo = False # Vai fechar o laço self.laco_jogo
                
                if event.type == py.MOUSEBUTTONUP: #evento de pulo com o clique do mouse
                    self.bird.Click() 
                
            self.seconds = self.fps.get_time() / 1000 # Segundos dentro do laço de x frames por segundo

            self.list_ground = list(self.groundGroup) #Lista com os elementos do grupo chão
            if self.list_ground[-1].xPosition < 0: #Controlando a aparição de objetos chão
                self.groundGroup.add(Ground(p=432)) 
            
            # Deteção de colisão
            self.colisaoChao = py.sprite.spritecollide(self.bird, self.groundGroup, False) # Pássaro - chão
            if self.colisaoChao:
                sleep(1)
                self.laco_jogo = False # Vai fechar o laço self.laco_jogo
            else:
                self.bird.gravidade(self.seconds)
                

            self.tela.blit(self.background, (0, 0))
            # Desenhando sprites na tela
            self.playerGroup.draw(self.tela)
            self.groundGroup.draw(self.tela)
            # Função update dos objetos
            self.playerGroup.update()
            self.groundGroup.update()
            
            py.display.flip()

