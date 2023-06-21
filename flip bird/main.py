from gamesccene import Game
from introscene import Intro
from endgame import Over
import pygame

pygame.init()
tela = pygame.display.set_mode((432, 762))
pygame.display.set_caption("Flip bird - python")

loopGame = True

jogo = Game(tela)

while loopGame:
    jogo.rum()
    if jogo.closeGame:
        break
    

    """
    jogo = Game(tela)
    fim = Over(tela)
    intro = Intro(tela)

    intro.rum()
    if intro.closeGame:
        break 

    jogo.rum()
    if jogo.closeGame:
        break
        
    fim.rum()
    if fim.closeGame:
        break
    """



pygame.quit()