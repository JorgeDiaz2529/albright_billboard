# credit for original code goes to Irv Kalb's chapter 6 of Object Oriented Python
# credit for code that was memorized here also goes to vlogize from Youtube. Link: https://www.youtube.com/watch?v=51ZozZ1cIW0

# 1 - Import packages
import pygame
from pygame.locals import *
from pygame import mixer
import sys
import random
from Ball import *  # bring in the Ball class code


# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  






 
  

   


# 4 - Load assets: image(s), sounds, etc.
         

# 5 - Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)  # append the new Ball to the list of Balls   

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()       


    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()  # tell each Ball to update itself

   # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    for oBall in ballList:
        oBall.draw()   # tell each Ball to draw itself

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

    def check_events(oBall):
        for event in pygame.event.get():
            event.type == pygame.QUIT
            pygame.quit
            sys.exit
            event.type == pygame.MOUSEBUTTONDOWN
            click_pos = pygame.mouse.get_pos
            oBall.check_collisions(click_pos)
    def __init__(self, screen, oBall_positions):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('assignments/15_final_game/CSC142/Practice_Timer.py/ball.png')
        self.oBall_positions = oBall_positions
        oBall_positions = [(x * 10 + 10, y * 3 + 3)for x in range[10] for y in range [3]]
        oBall = oBall(display, oBall_positions)

    def oBall_action(oBall):
        for o in oBall.oBall_positions:
         oBall.blitme(o(0), o(1))

    def check_collisions(pos, self):
        r = 5
        for o in self.oBall_positions:
            if (o[0] -pos [0]) **2 + (o[1]) -pos [1]:
                self.oBall_positions.remove(0)
                break



    
           
             
            
            
        
        

        

    



    


