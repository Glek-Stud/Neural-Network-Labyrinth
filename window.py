import pygame
from pygame.locals import *

# initialisation of pygame
pygame.init()


# size of window

# WIDTH = 1920
# HEIGHT = 1080

#for full screen

screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



# creating button
button = pygame.Rect(800, 500, 50, 20)


# creating of class of window
class Window:

    def __init__(self):
        # create window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # name of window
        pygame.display.set_caption("Labyrinth")

        # for fps
        self.clock = pygame.time.Clock()




    def run(self):
        
        running = True
        while running:
            # to detect some events
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                # if was clicked
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if button.collidepoint(event.pos):
                        print("click))))")
            self.screen.fill(WHITE)

            # some code here
            # example
            pygame.draw.rect(self.screen, BLACK, button)



            pygame.display.update()
            # fps on screen
            self.clock.tick(60)


pygame.quit()