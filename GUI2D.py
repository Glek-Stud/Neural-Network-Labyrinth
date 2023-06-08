from utils import set_logger
# import random
import pygame
from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from LabyrinthLogic import LabyrinthLogic
from config import HEIGHT, WIDTH, WHITE, BLACK, BLOCKSIZE, FRAME, GRAY, TITLE, DARK_GRAY


class GUI2D:
    # initialisation of pygame
    pygame.init()

    def __init__(self):
        self.logger = set_logger("GUI 2D")
        self.labyrinth_class = LabyrinthLogic(25)
        self.labyrinth_class.random_matrix()
        self.labyrinth = self.labyrinth_class.get_border_labyrinth()

        # create window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME | pygame.DOUBLEBUF)

        # name of window
        pygame.display.set_caption("Labyrinth")

        # for fps
        self.clock = pygame.time.Clock()

        # resizing frame
        self.originSize = 5
        self.hoveredSize = 35
        self.currentSize = self.originSize

        # detect mouse on panel
        self.detect = False

        # title
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(TITLE, True, WHITE)
        self.rotated_surface = pygame.transform.rotate(self.text_surface, -90)

        # colors for buttons
        self.colorOfButtonClose = GRAY
        self.colorOfButtonHide = GRAY

        # states of buttons
        self.closeButtonState = "normal"
        self.hideButtonState = "normal"

    def draw(self):
        # draw labyrinth by random matrix
        for row in range(len(self.labyrinth)):
            for col in range(len(self.labyrinth[row])):
                x = (WIDTH + FRAME - len(self.labyrinth) * BLOCKSIZE) / 2 + col * BLOCKSIZE
                y = (HEIGHT - len(self.labyrinth) * BLOCKSIZE) / 2 + row * BLOCKSIZE

                pygame.draw.rect(self.screen, GRAY, (WIDTH - 5, 0, 10, HEIGHT), border_radius=40)
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

                # mouse motion
                if event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos

                    # if mouse is on panel
                    if WIDTH - self.currentSize <= mouse_x <= WIDTH and 0 <= mouse_y <= HEIGHT:
                        self.currentSize = self.hoveredSize
                        self.detect = True

                        # if mouse is on close button
                        if WIDTH - 35 <= mouse_x <= WIDTH and 20 <= mouse_y <= 55:
                            self.colorOfButtonClose = DARK_GRAY
                            self.closeButtonState = True
                        else:
                            self.colorOfButtonClose = GRAY

                        # if mouse is on hide button
                        if WIDTH - 35 <= mouse_x <= WIDTH and 55 <= mouse_y <= 90:
                            self.colorOfButtonHide = DARK_GRAY
                            self.hideButtonState = True

                        else:
                            self.colorOfButtonHide = GRAY

                    else:
                        self.currentSize = self.originSize
                        self.detect = False

                # if clicked
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.detect:
                            mouse_pos = pygame.mouse.get_pos()
                            if WIDTH - 35 < mouse_pos[0] < WIDTH and 20 < mouse_pos[1] < 55:
                                self.closeButtonState = "clicked"
                            if WIDTH - 35 < mouse_pos[0] < WIDTH and 55 < mouse_pos[1] <= 90:
                                self.hideButtonState = "clicked"

                # if unclicked
                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.detect:
                            if self.closeButtonState == "clicked":
                                running = False
                            elif self.hideButtonState == "clicked":
                                pygame.display.iconify()

            self.screen.fill(WHITE)

            # some code here
            self.draw()

            # draw panel
            pygame.draw.rect(self.screen, GRAY, (WIDTH - self.currentSize, -2, 10 + self.currentSize, HEIGHT + 4),
                             border_radius=40)

            # if mouse on panel
            if self.detect:
                # type title
                self.screen.blit(self.rotated_surface, (WIDTH - 30, 250))

                # draw buttons

                # button close
                pygame.draw.rect(self.screen, self.colorOfButtonClose, (WIDTH - 35, 20, 35, 35))

                pygame.draw.line(self.screen, (255, 255, 255), (WIDTH - 30, 25), (WIDTH - 5, 50), 2)
                pygame.draw.line(self.screen, (255, 255, 255), (WIDTH - 30, 50), (WIDTH - 5, 25), 2)

                # button hide
                pygame.draw.rect(self.screen, self.colorOfButtonHide, (WIDTH - 35, 55, 35, 35))
                pygame.draw.line(self.screen, (255, 255, 255), (WIDTH - 30, 73), (WIDTH - 5, 73), 1)

            pygame.display.update()
            # fps on screen
            self.clock.tick(60)

        pygame.quit()
