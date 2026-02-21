import pygame

class Design:
    def __init__(self, text, bg_color, text_color=(255, 255, 255),
                 delay=2000, image_path=None, image_size=(120, 120)):
        """
        :param text: Text to display
        :param bg_color: Background color (R, G, B)
        :param text_color: Text color (R, G, B)
        :param delay: Delay in milliseconds before switching to next design
        :param image_path: Path to logo image (optional)
        :param image_size: Size to scale the logo (width, height)
        """
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.delay = delay

        self.image = None
        self.image_size = image_size

        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, image_size)

    def render(self, size, font):
        """
        Render the design onto its own surface.
        """
        surface = pygame.Surface(size).convert_alpha()
        surface.fill(self.bg_color)

        padding = 40  # space from left edge
        text_offset_x = padding

        # Draw image if it exists
        if self.image:
            image_rect = self.image.get_rect()
            image_rect.left = padding
            image_rect.centery = surface.get_rect().centery
            surface.blit(self.image, image_rect)

            # Shift text to the right of image
            text_offset_x = image_rect.right + 30

        # Render text
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        
        text_rect.centery = surface.get_rect().centery

        if self.image:
            text_rect.left = text_offset_x
        else:
            text_rect.centerx = surface.get_rect().centerx

        surface.blit(text_surface, text_rect)

        return surface
