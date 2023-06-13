from utils import set_logger
# import random
import pygame
from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from LabyrinthLogic import LabyrinthLogic
from LabyrinthLogic import Point
from config import HEIGHT, WIDTH, LABYRINTH_SIZE, BUTTON_HEIGHT_SIZE, WHITE, BLACK, BLOCK_SIZE, GRAY, TITLE, DARK_GRAY




class GUI2D:
    # initialisation of pygame
    pygame.init()


    def __init__(self, buttons):
        self.logger = set_logger("GUI 2D")
        self.labyrinth_class = LabyrinthLogic(25)
        self.labyrinth_class.generate_labyrinth()
        self.labyrinth = self.labyrinth_class.get_border_labyrinth()

        self.player = Point(self.labyrinth_class, 2,0)

        for i in self.labyrinth:
            print(i)

        #CIRCLE
        self.circle_radius = BLOCK_SIZE / 2 - 1
        self.radius_decreasing = True

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
        self.font = pygame.font.Font(None, int(BLOCK_SIZE * 1.4))
        self.bold_font = pygame.font.Font(None, int(BLOCK_SIZE * 1.6))
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

        self.mouse_in_labyrinth = None

        #     player
        self.x = 1
        self.y = 0


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
            self.screen.blit(self.rotated_surface,
                             (WIDTH - 30, int(HEIGHT / 2 + self.rotated_surface.get_width() / 2)))

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
                    pygame.draw.rect(self.screen, (44, 35, 59), (x, y, BLOCK_SIZE, BLOCK_SIZE), 2)
                    pygame.draw.rect(self.screen, (69, 62, 73), (x + 2, y + 2, BLOCK_SIZE - 4, (BLOCK_SIZE - 2) / 3))
                    pygame.draw.rect(self.screen, (77, 76, 131), (x + 2, y + 8, BLOCK_SIZE - 4, (BLOCK_SIZE - 2) / 3))
                    pygame.draw.rect(self.screen, (107, 132, 175), (x + 2, y + 14, BLOCK_SIZE - 4, (BLOCK_SIZE - 2) / 3))

                elif self.labyrinth[row][col] == 2:
                    pygame.draw.rect(self.screen, (107, 132, 175), (x, y, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y, 7, 14), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y, 14, 7), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y + 6, 14, 8), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y + 13, 13, 8), 1)

                    pygame.draw.circle(self.screen, (14, 245, 73), (x + (BLOCK_SIZE / 2), y + (BLOCK_SIZE / 2)),
                                       self.circle_radius)
                elif self.labyrinth[row][col] == 3:
                    pygame.draw.rect(self.screen, (107, 132, 175), (x, y, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y, 7, 14), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y, 14, 7), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y + 6, 14, 8), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y + 13, 13, 8), 1)

                    pygame.draw.circle(self.screen, (245, 28, 12), (x + (BLOCK_SIZE / 2), y + (BLOCK_SIZE / 2)),
                                       self.circle_radius)

                elif self.labyrinth[row][col] == 4:
                    pygame.draw.rect(self.screen, (44, 35, 59), (x, y, BLOCK_SIZE, BLOCK_SIZE), 2)
                    pygame.draw.rect(self.screen, (226, 180, 126), (x + 2, y + 2, BLOCK_SIZE - 4, 7))
                    pygame.draw.rect(self.screen, (218, 148, 109), (x + 2, y + 8, BLOCK_SIZE - 4, 3))
                    pygame.draw.rect(self.screen, (196, 113, 95), (x + 2, y + 11, BLOCK_SIZE - 4, 3))
                    pygame.draw.rect(self.screen, (161, 82, 88), (x + 2, y + 14, BLOCK_SIZE - 4, 5))


                elif self.labyrinth[row][col] == 8:
                    pygame.draw.rect(self.screen, (107, 132, 175), (x, y, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y, 7, 14), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y, 14, 7), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y + 6, 14, 8), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y + 13, 13, 8), 1)
                    pygame.draw.line(self.screen, (255,0,0), (x,y+BLOCK_SIZE/2), (x+BLOCK_SIZE+BLOCK_SIZE, y+BLOCK_SIZE/2), 5)

                elif self.labyrinth[row][col] == 9:
                    pygame.draw.rect(self.screen, (107, 132, 175), (x, y, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y, 7, 14), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y, 14, 7), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y + 6, 14, 8), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y + 13, 13, 8), 1)
                    pygame.draw.line(self.screen, (255,0,0), (x+BLOCK_SIZE/2,y), (x+BLOCK_SIZE/2, y+BLOCK_SIZE*10), 5)

                else:
                    pygame.draw.rect(self.screen, (107, 132, 175), (x, y, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y, 7, 14), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y, 14, 7), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x + 6, y + 6, 14, 8), 1)
                    pygame.draw.rect(self.screen, (126, 163, 191), (x, y + 13, 13, 8), 1)


    def draw_button(self):
        button_width = (LABYRINTH_SIZE - BLOCK_SIZE * 2 + 10) / len(self.buttons)
        for num, button in enumerate(self.buttons):
            if self.mouse_in_button == num:
                pygame.draw.rect(self.screen, BLACK,
                                 (BLOCK_SIZE + num * button_width - 5, LABYRINTH_SIZE - 5, button_width,
                                  BUTTON_HEIGHT_SIZE + 10),
                                 int(BLOCK_SIZE * 0.6))
                text_surface = self.bold_font.render(button["name"], True, BLACK)
            else:
                pygame.draw.rect(self.screen, BLACK,
                                 (BLOCK_SIZE + num * button_width, LABYRINTH_SIZE, button_width - 10,
                                  BUTTON_HEIGHT_SIZE),
                                 int(BLOCK_SIZE * 0.6))
                text_surface = self.font.render(button["name"], True, BLACK)
            self.screen.blit(text_surface,
                             (BLOCK_SIZE + num * button_width + button_width / 2 - text_surface.get_width() / 2 - 5,
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

        if BLOCK_SIZE <= mouse_x <= WIDTH - BLOCK_SIZE and LABYRINTH_SIZE <= mouse_y <= HEIGHT - BLOCK_SIZE:
            button_width = (LABYRINTH_SIZE - BLOCK_SIZE * 2 + 10) / len(self.buttons)
            for num in range(len(self.buttons)):
                start_x = BLOCK_SIZE + num * button_width
                if start_x <= mouse_x <= start_x + button_width - 10:
                    self.mouse_in_button = num

        else:
            self.mouse_in_button = None

        if BLOCK_SIZE * 2 <= mouse_x <= WIDTH - BLOCK_SIZE * 2 and BLOCK_SIZE * 2 <= mouse_y <= LABYRINTH_SIZE - BLOCK_SIZE * 2:
            for row in range(len(self.labyrinth)):
                for col in range(len(self.labyrinth[row])):
                    x = (col + 1) * BLOCK_SIZE  # (WIDTH - len(self.labyrinth) * BLOCKSIZE) / 2
                    y = (row + 1) * BLOCK_SIZE  # (HEIGHT - len(self.labyrinth) * BLOCKSIZE) / 2
                    if x <= mouse_x <= x + BLOCK_SIZE and y <= mouse_y <= y + BLOCK_SIZE:
                        self.mouse_in_labyrinth = [row - 1, col - 1]
        else:
            self.mouse_in_labyrinth = None

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

            if self.mouse_in_labyrinth is not None:
                self.labyrinth_class.get_point(self.mouse_in_labyrinth[0], self.mouse_in_labyrinth[1]).switch()
                self.labyrinth = self.labyrinth_class.get_border_labyrinth()

    def mouse_unclicked(self, event):
        if event.button == 1:
            if self.detect:
                if self.closeButtonState == "clicked":
                    self.run_bool = False
                elif self.hideButtonState == "clicked":
                    pygame.display.iconify()

    def key_clicked(self, event):
        # Time element, will refactor
        global BLOCK_SIZE, FRAME, LABYRINTH_SIZE, BUTTON_HEIGHT_SIZE, WIDTH, HEIGHT
        if event.key in [1073741911, 61]:
            BLOCK_SIZE += 5
            FRAME = 5
            LABYRINTH_SIZE = (25 + 2 * 2) * BLOCK_SIZE
            BUTTON_HEIGHT_SIZE = BLOCK_SIZE * 4

            WIDTH = LABYRINTH_SIZE + FRAME
            HEIGHT = LABYRINTH_SIZE + BUTTON_HEIGHT_SIZE + BLOCK_SIZE
            self.__init__(self.buttons)
        if event.key in [1073741910, 45]:
            BLOCK_SIZE -= 5
            FRAME = 5
            LABYRINTH_SIZE = (25 + 2 * 2) * BLOCK_SIZE
            BUTTON_HEIGHT_SIZE = BLOCK_SIZE * 4

            WIDTH = LABYRINTH_SIZE + FRAME
            HEIGHT = LABYRINTH_SIZE + BUTTON_HEIGHT_SIZE + BLOCK_SIZE
            self.__init__(self.buttons)


    def drawPlayer(self, key):
        # # CIRCLE
        # if self.radius_decreasing:
        #     self.circle_radius -= 0.1
        #     if self.circle_radius <= 0:  # если радиус достиг 0 или меньше, меняем направление
        #         self.radius_decreasing = False
        #
        # else:
        #     self.circle_radius += 0.1
        #     if self.circle_radius >= BLOCK_SIZE / 2 - 1:  # если радиус достиг максимального значения, меняем направление
        #         self.radius_decreasing = True



        # player move
        if key[pygame.K_UP]:
            if self.player.up(self.x, self.y, self.labyrinth):
                if self.labyrinth[self.y-1][self.x] ==9:

                    self.labyrinth[self.y][self.x] = 0
                else:
                    self.labyrinth[self.y][self.x] = 9
                self.labyrinth[self.y - 1][self.x] = 2
                self.y -= 1


        if key[pygame.K_DOWN]:
            if self.player.down(self.x, self.y, self.labyrinth):
                if self.labyrinth[self.y+1][self.x] == 9 :
                    self.labyrinth[self.y][self.x] = 0
                else:
                    self.labyrinth[self.y][self.x] = 9

                self.labyrinth[self.y+1][self.x] = 2
                self.y+=1

        if key[pygame.K_RIGHT]:
            if self.player.right(self.x, self.y, self.labyrinth):
                if self.labyrinth[self.y][self.x+1] == 8:
                    self.labyrinth[self.y][self.x] = 0
                else:
                    self.labyrinth[self.y][self.x] = 8
                self.labyrinth[self.y][self.x + 1] = 2
                self.x+=1

        if key[pygame.K_LEFT]:
            if self.player.left(self.x, self.y, self.labyrinth):
                if self.labyrinth[self.y][self.x-1] == 8:
                    self.labyrinth[self.y][self.x] = 0
                else:
                    self.labyrinth[self.y][self.x] = 8
                self.labyrinth[self.y][self.x - 1] = 2
                self.x-=1

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

                # if event.type == pygame.KEYDOWN:
                #     self.key_clicked(event)
                key = pygame.key.get_pressed()
                self.drawPlayer(key)

            # some code here
            self.draw()



            pygame.display.update()
            # fps on screen
            self.clock.tick(60)

        pygame.quit()
