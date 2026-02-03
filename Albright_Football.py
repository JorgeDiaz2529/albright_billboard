import sys 

import pygame

from settings import Settings

from albight import Albright

class GameCharacter:
    """Overall class to manage game assets add behavior."""

    def __init__(self):
        """Initialize the game, and create game recources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Game Character")
        self.albright = Albright(self)

        # Set the backround color.
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            # Redraw the screen during each pass through the loop.
            # Watch for keyboard and mouse events.
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.albright.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = GameCharacter()
    ai.run_game()