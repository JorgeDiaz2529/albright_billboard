import pygame
import sys

class Billboard:
    def __init__(self):
        pygame.init()
        
        self.designs = []
        self.screen = pygame.display.set_mode((1280,640))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.clock.tick(60)

    def change_style(self):
        pass

    def draw(self):
        pass

if __name__ == '__main__':
    program = Billboard()
    program.run()