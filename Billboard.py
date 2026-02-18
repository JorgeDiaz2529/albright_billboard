import pygame
from Design import Design
from PIL import Image

class Billboard:
    def __init__(self, width=800, height=400, transition_duration=800):
        pygame.init()
        self.clock =pygame.time.Clock()

        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Animated Billboard")

        pygame.mixer.music.load('audio/background.mp3')
        
        pygame.mixer.music.play(-1, 0.0)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 64)

        self.designs = []
        self.current_design_index = 0
        self.last_switch_time = pygame.time.get_ticks()

        self.transition_duration = transition_duration
        self.is_transitioning = False
        self.transition_start_time = 0

        self.current_surface = None
        self.next_surface = None

    def add_design(self, design):
        self.designs.append(design)

    def start_transition(self):
        self.is_transitioning = True
        self.transition_start_time = pygame.time.get_ticks()

        next_index = (self.current_design_index + 1) % len(self.designs)

        self.current_surface = self.designs[self.current_design_index].render(
            self.size, self.font
        )
        self.next_surface = self.designs[next_index].render(
            self.size, self.font
        )

        self.current_design_index = next_index
        self.last_switch_time = pygame.time.get_ticks()

    def draw_transition(self):
        elapsed = pygame.time.get_ticks() - self.transition_start_time
        progress = min(elapsed / self.transition_duration, 1)

        self.current_surface.set_alpha(255 * (1 - progress))
        self.next_surface.set_alpha(255 * progress)

        self.screen.blit(self.current_surface, (0, 0))
        self.screen.blit(self.next_surface, (0, 0))
        
        

        if progress >= 1:
            self.is_transitioning = False

    def run(self):
        running = True

        while running:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.designs:
                continue

            current_design = self.designs[self.current_design_index]

            if not self.is_transitioning:
                if current_time - self.last_switch_time >= current_design.delay:
                    self.start_transition()
                else:
                    surface = current_design.render(self.size, self.font)
                    self.screen.blit(surface, (0, 0))
                    
            else:
                self.draw_transition()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    billboard = Billboard()

    billboard.add_design(Design("Albright College: 1856", (255, 0, 255), delay=5000, image_path="images/Albrightlogo2.py.webp"))
    billboard.add_design(Design("Welcome to our school!", (50, 168, 82), delay=2500))
    billboard.add_design(Design("Learn!", (66, 135, 245), delay=2500))
    billboard.add_design(Design("Pursue your passions!", (9, 107, 96), delay=2500))
    billboard.add_design(Design("Make new friends!", (245, 170, 66), delay=2500))
    billboard.add_design(Design("Join in on our activities!", (75, 66, 245), delay=2500))
    billboard.add_design(Design("Thanks for visiting!", (34, 139, 34), delay=2500))

    billboard.run()
