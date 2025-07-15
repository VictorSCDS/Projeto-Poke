import pygame
from config import fps, cores

class Game:
    def __init__(self,janela):
        self.janela = janela
        self.clock = pygame.time.Clock()
        self.running = True
    def run(self):
        while self.running:
            self.clock.tick(fps)
            self.handle_events()
            self.update()
            self.draw()
    def hundle_events(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                self.running = False
    def update(self):
        pass
    def draw(self):
        self.janela.fill(cores['white'])