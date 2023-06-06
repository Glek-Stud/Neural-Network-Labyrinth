import pygame
from pygame.locals import *
from LabyrinthLogic import *


# initialisation of pygame
pygame.init()


# size of window

WIDTH = 800
HEIGHT = 600

#for full screen

screen_info = pygame.display.Info()
# WIDTH = screen_info.current_w
# HEIGHT = screen_info.current_h
flags = pygame.NOFRAME | pygame.DOUBLEBUF

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# size of block
BLOCKSIZE = 20



labyrinth_class = LabyrinthLogic(25)
labyrinth_class.random_matrix()
matrix = labyrinth_class.labyrinth



# creating of class of window
class Window:
    def __init__(self):
        # create window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)

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
                # elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # if button.collidepoint(event.pos):
                    #     print("click))))")
            self.screen.fill(WHITE)

            # some code here
            # example
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    x = (WIDTH-len(matrix)*BLOCKSIZE)/2 + col * BLOCKSIZE
                    y = (HEIGHT-len(matrix)*BLOCKSIZE)/2 + row * BLOCKSIZE

                    if matrix[row][col] == 1:
                        pygame.draw.rect(self.screen, BLACK, (x, y, BLOCKSIZE, BLOCKSIZE))
                    else:
                        pygame.draw.rect(self.screen, WHITE, (x, y, BLOCKSIZE, BLOCKSIZE))
            pygame.display.update()
            # fps on screen
            self.clock.tick(60)

pygame.quit()