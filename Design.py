import pygame

class Design:
    def __init__(self, text, bg_color, text_color=(255, 255, 255), delay=2000):
        """
        :param text: Text to display
        :param bg_color: Background color (R, G, B)
        :param text_color: Text color (R, G, B)
        :param delay: Delay in milliseconds before switching to next design
        """
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.delay = delay

    def render(self, size, font):
        """
        Render the design onto its own surface.
        """
        surface = pygame.Surface(size).convert_alpha()
        surface.fill(self.bg_color)

        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=surface.get_rect().center)

        surface.blit(text_surface, text_rect)
        return surface