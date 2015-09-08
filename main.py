import pygame
from libs import *
from libs.game import Game

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Game().main(screen)
