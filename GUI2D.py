from utils import set_logger
# import random
import pygame
from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from LabyrinthLogic import LabyrinthLogic
from config import HEIGHT, WIDTH, LABYRINTH_SIZE, BUTTON_HEIGHT_SIZE, WHITE, BLACK, BLOCK_SIZE, GRAY, TITLE, DARK_GRAY


class GUI2D:
    # initialisation of pygame
    pygame.init()

    def __init__(self, buttons):
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
        self.bold_font = pygame.font.Font(None, 40)
        self.text_surface = self.font.render(TITLE, True, WHITE)
        self.rotated_surface = pygame.transform.rotate(self.text_surface, -90)

        # colors for buttons
        self.colorOfButtonClose = GRAY
        self.colorOfButtonHide = GRAY

        # states of buttons
        self.closeButtonState = "normal"
        self.hideButtonState = "normal"

        self.run_bool = True
        self.buttons = buttons
        self.mouse_in_button = None

    # <--- Draw all element --->
    def draw(self):
        self.screen.fill(WHITE)

        # draw labyrinth by random matrix
        self.draw_labyrinth()
        self.draw_button()

        self.draw_panel()

    def draw_panel(self):
        # pygame.draw.rect(self.screen, GRAY, (WIDTH - 5, 0, 10, HEIGHT), border_radius=40)
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

    def draw_labyrinth(self):
        for row in range(len(self.labyrinth)):
            for col in range(len(self.labyrinth[row])):
                x = (col + 1) * BLOCK_SIZE  # (WIDTH - len(self.labyrinth) * BLOCKSIZE) / 2
                y = (row + 1) * BLOCK_SIZE  # (HEIGHT - len(self.labyrinth) * BLOCKSIZE) / 2

                if self.labyrinth[row][col] == 1:
                    pygame.draw.rect(self.screen, BLACK, (x, y, BLOCK_SIZE, BLOCK_SIZE))
                else:
                    pygame.draw.rect(self.screen, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    def draw_button(self):
        button_width = (LABYRINTH_SIZE - 50 + 10) / len(self.buttons)
        for num, button in enumerate(self.buttons):
            if self.mouse_in_button == num:
                pygame.draw.rect(self.screen, BLACK,
                                 (25 + num * button_width - 5, LABYRINTH_SIZE - 5, button_width,
                                  BUTTON_HEIGHT_SIZE + 10),
                                 15)
                text_surface = self.bold_font.render(button["name"], True, BLACK)
            else:
                pygame.draw.rect(self.screen, BLACK,
                                 (25 + num * button_width, LABYRINTH_SIZE, button_width - 10, BUTTON_HEIGHT_SIZE),
                                 15)
                text_surface = self.font.render(button["name"], True, BLACK)
            self.screen.blit(text_surface,
                             (25 + num * button_width + button_width / 2 - text_surface.get_width() / 2,
                              LABYRINTH_SIZE + BUTTON_HEIGHT_SIZE / 2 - text_surface.get_height() / 2))

    # <--- Mouse event --->
    def mouse_motion(self, event):
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

        if 25 <= mouse_x <= WIDTH - 25 and LABYRINTH_SIZE <= mouse_y <= HEIGHT - 25:
            button_width = (LABYRINTH_SIZE - 50 + 10) / len(self.buttons)
            for num in range(len(self.buttons)):
                start_x = 25 + num * button_width
                if start_x <= mouse_x <= start_x + button_width - 10:
                    self.mouse_in_button = num

        else:
            self.mouse_in_button = None

    def mouse_clicked(self, event):
        if event.button == 1:
            if self.detect:
                mouse_pos = pygame.mouse.get_pos()
                if WIDTH - 35 < mouse_pos[0] < WIDTH and 20 < mouse_pos[1] < 55:
                    self.closeButtonState = "clicked"
                if WIDTH - 35 < mouse_pos[0] < WIDTH and 55 < mouse_pos[1] <= 90:
                    self.hideButtonState = "clicked"

            if self.mouse_in_button is not None:
                self.buttons[self.mouse_in_button]["func"]()

    def mouse_unclicked(self, event):
        if event.button == 1:
            if self.detect:
                if self.closeButtonState == "clicked":
                    self.run_bool = False
                elif self.hideButtonState == "clicked":
                    pygame.display.iconify()

    # <--- Run game --->
    def run(self):
        while self.run_bool:
            # to detect some events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run_bool = False

                # mouse motion
                if event.type == MOUSEMOTION:
                    self.mouse_motion(event)

                # if clicked
                if event.type == MOUSEBUTTONDOWN:
                    self.mouse_clicked(event)

                # if unclicked
                elif event.type == MOUSEBUTTONUP:
                    self.mouse_unclicked(event)

            # some code here
            self.draw()

            pygame.display.update()
            # fps on screen
            self.clock.tick(60)

        pygame.quit()
