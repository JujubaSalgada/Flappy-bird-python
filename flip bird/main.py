from gamesccene import Game
from introscene import Intro
from endgame import Over
import pygame

pygame.init()
tela = pygame.display.set_mode((300, 450))
pygame.display.set_caption("Flip bird - python")

loopGame = True

while loopGame:
    intro = Intro(tela)
    fim = Over(tela)

    intro.rum()
    if intro.closeGame:
        break

    fim.rum()
    if fim.closeGame:
        break

    """
    jogo = Game(tela)
    fim = Over(tela)

    fim.rum()
    if fim.closeGame:
        break
        
    jogo.rum()
    if jogo.closeGame:
        break
    """



pygame.quit()