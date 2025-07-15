import pygame
from game import Game

def main():
    pygame.init()

    janela = pygame.display.set_mode((1056,720))
    pygame.display.set_caption("Monster Fantasy")

    game = Game(janela)
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()