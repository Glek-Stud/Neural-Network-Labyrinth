from utils import set_logger
# import random
import pygame
from pygame.locals import QUIT
from LabyrinthLogic import LabyrinthLogic
from config import HEIGHT, WIDTH, WHITE, BLACK, BLOCKSIZE


class GUI2D:
    def __init__(self):
        self.logger = set_logger("GUI 2D")

        # initialisation of pygame
        pygame.init()

        self.labyrinth_class = LabyrinthLogic(25)
        self.labyrinth_class.random_matrix()
        self.labyrinth = self.labyrinth_class.get_border_labyrinth()

        # create window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT ), flags = pygame.NOFRAME | pygame.DOUBLEBUF)

        # name of window
        pygame.display.set_caption("Labyrinth")

        # for fps
        self.clock = pygame.time.Clock()

    def draw(self):
        # example
        for row in range(len(self.labyrinth)):
            for col in range(len(self.labyrinth[row])):
                x = (WIDTH - len(self.labyrinth) * BLOCKSIZE) / 2 + col * BLOCKSIZE
                y = (HEIGHT - len(self.labyrinth) * BLOCKSIZE) / 2 + row * BLOCKSIZE

                if self.labyrinth[row][col] == 1:
                    pygame.draw.rect(self.screen, BLACK, (x, y, BLOCKSIZE, BLOCKSIZE))
                else:
                    pygame.draw.rect(self.screen, WHITE, (x, y, BLOCKSIZE, BLOCKSIZE))

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
            self.draw()

            pygame.display.update()
            # fps on screen
            self.clock.tick(60)

        pygame.quit()