from VectorGraphics import VectorGraphics
from utils import set_logger
# import random
import pygame
from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from LabyrinthLogic import LabyrinthLogic
from config import WHITE, BLACK, GRAY, TITLE, DARK_GRAY, FRAME
from NeuralNetwork import NeuralNetwork

class GUI2D:
    # initialisation of pygame
    pygame.init()
    pygame.mixer.init()

    def __init__(self, scale=25, size=20, sleap_network=5):
        self.logger = set_logger("GUI 2D")

        self.labyrinth_class = LabyrinthLogic(scale)
        self.labyrinth_class.generate_labyrinth()
        self.labyrinth_class.update_border_labyrinth()
        self.labyrinth = self.labyrinth_class.border_labyrinth
        self.player = self.labyrinth_class.get_player()

        self.neural_network_class = NeuralNetwork()
        self.network_bool = False
        self.sleap_network = sleap_network
        self.sleap_network_check = 0

        # CIRCLE
        self.circle_radius = size / 2 - 1
        self.radius_decreasing = True

        # create window
        self.size = size
        self.scale = scale
        self.width, self.height, self.button_height_size, self.labyrinth_size = [0] * 4
        self.screen, self.font, self.bold_font = [None] * 3
        self.init_size_component()

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

        # CIRCLE
        self.circle_radius = self.size / 2 - 1
        # title

        self.text_surface = self.font.render(TITLE, True, WHITE)
        self.rotated_surface = pygame.transform.rotate(self.text_surface, -90)

        # colors for buttons
        self.colorOfButtonClose = GRAY
        self.colorOfButtonHide = GRAY

        # states of buttons
        self.closeButtonState = "normal"
        self.hideButtonState = "normal"

        self.run_bool = True
        self.buttons = [
            {"name": "Тренировка нейросети", "func": lambda: self.neural_network_class.auto_generate_training()},
            {"name": "Включить нейросеть", "func": lambda: self.switch_network_bool()},
        ]
        self.mouse_in_button = None

        self.mouse_in_labyrinth = None


    def init_size_component(self):
        # size of window
        self.labyrinth_size = (self.scale + 2 * 2) * self.size
        self.button_height_size = self.size * 4

        self.width = self.labyrinth_size + FRAME
        self.height = self.labyrinth_size + self.button_height_size + self.size+50

        self.screen = pygame.display.set_mode((self.width, self.height), flags=pygame.NOFRAME | pygame.DOUBLEBUF)

        self.font = pygame.font.Font(None, int(self.size * 1.4))
        self.bold_font = pygame.font.Font(None, int(self.size * 1.6))

    def switch_network_bool(self):
        self.network_bool = not self.network_bool

    # <--- Draw all element --->
    def draw(self):
        self.screen.fill(WHITE)

        # draw labyrinth by random matrix
        self.draw_labyrinth()
        self.draw_button()

        self.draw_panel()

    def draw_panel(self):
        # pygame.draw.rect(self.screen, GRAY, (self.width - 5, 0, 10, self.height), border_radius=40)
        pygame.draw.rect(self.screen, GRAY, (self.width - self.currentSize, -2, 10 + self.currentSize, self.height + 4),
                         border_radius=40)

        # if mouse on panel
        if self.detect:
            # type title
            self.screen.blit(self.rotated_surface,
                             (self.width - 30, int(self.height / 2 + self.rotated_surface.get_width() / 2)))

            # draw buttons

            # button close
            pygame.draw.rect(self.screen, self.colorOfButtonClose, (self.width - 35, 20, 35, 35))

            pygame.draw.line(self.screen, (255, 255, 255), (self.width - 30, 25), (self.width - 5, 50), 2)
            pygame.draw.line(self.screen, (255, 255, 255), (self.width - 30, 50), (self.width - 5, 25), 2)

            # button hide
            pygame.draw.rect(self.screen, self.colorOfButtonHide, (self.width - 35, 55, 35, 35))
            pygame.draw.line(self.screen, (255, 255, 255), (self.width - 30, 73), (self.width - 5, 73), 1)

    def draw_labyrinth(self):
        surfaces = VectorGraphics(self.size, self.circle_radius).surfaces

        for row in range(len(self.labyrinth)):
            for col in range(len(self.labyrinth[row])):
                x = (col + 1) * self.size
                y = (row + 1) * self.size

                surface = surfaces[self.labyrinth[row][col]]

                self.screen.blit(surface, (x, y))

    def draw_button(self):
        button_width = (self.labyrinth_size - self.size * 2 + 10) / len(self.buttons)
        for num, button in enumerate(self.buttons):
            if self.mouse_in_button == num:
                pygame.draw.rect(self.screen, BLACK,
                                 (self.size + num * button_width - 5, self.labyrinth_size - 5, button_width,
                                  self.button_height_size + 10),
                                 int(self.size * 0.6))
                text_surface = self.bold_font.render(button["name"], True, BLACK)
            else:
                pygame.draw.rect(self.screen, BLACK,
                                 (self.size + num * button_width, self.labyrinth_size, button_width - 10,
                                  self.button_height_size),
                                 int(self.size * 0.6))
                text_surface = self.font.render(button["name"], True, BLACK)
            self.screen.blit(text_surface,
                             (self.size + num * button_width + button_width / 2 - text_surface.get_width() / 2 - 5,
                              self.labyrinth_size + self.button_height_size / 2 - text_surface.get_height() / 2))

    # <--- Mouse event --->
    def mouse_motion(self, position):
        mouse_x, mouse_y = position

        # if mouse is on panel
        if self.width - self.currentSize <= mouse_x <= self.width and 0 <= mouse_y <= self.height:
            self.currentSize = self.hoveredSize
            self.detect = True

            # if mouse is on close button
            if self.width - 35 <= mouse_x <= self.width and 20 <= mouse_y <= 55:
                self.colorOfButtonClose = DARK_GRAY
                self.closeButtonState = True
            else:
                self.colorOfButtonClose = GRAY

            # if mouse is on hide button
            if self.width - 35 <= mouse_x <= self.width and 55 <= mouse_y <= 90:
                self.colorOfButtonHide = DARK_GRAY
                self.hideButtonState = True

            else:
                self.colorOfButtonHide = GRAY

        else:
            self.currentSize = self.originSize
            self.detect = False

        if self.size <= mouse_x <= self.width - self.size and self.labyrinth_size <= mouse_y <= self.height - self.size:
            button_width = (self.labyrinth_size - self.size * 2 + 10) / len(self.buttons)
            for num in range(len(self.buttons)):
                start_x = self.size + num * button_width
                if start_x <= mouse_x <= start_x + button_width - 10:
                    self.mouse_in_button = num

        else:
            self.mouse_in_button = None

        two_size = self.size * 2
        if two_size <= mouse_x <= self.width - two_size and two_size <= mouse_y <= self.labyrinth_size - two_size:
            for row in range(len(self.labyrinth)):
                for col in range(len(self.labyrinth[row])):
                    x = (col + 1) * self.size  # (self.width - len(self.labyrinth) * self.size) / 2
                    y = (row + 1) * self.size  # (self.height - len(self.labyrinth) * self.size) / 2
                    if x <= mouse_x <= x + self.size and y <= mouse_y <= y + self.size:
                        self.mouse_in_labyrinth = [row - 1, col - 1]
        else:
            self.mouse_in_labyrinth = None

    def mouse_clicked(self, button):
        if button == 1:
            if self.detect:
                mouse_pos = pygame.mouse.get_pos()
                if self.width - 35 < mouse_pos[0] < self.width and 20 < mouse_pos[1] < 55:
                    self.closeButtonState = "clicked"
                if self.width - 35 < mouse_pos[0] < self.width and 55 < mouse_pos[1] <= 90:
                    self.hideButtonState = "clicked"

            if self.mouse_in_button is not None:
                self.buttons[self.mouse_in_button]["func"]()

            if self.mouse_in_labyrinth is not None:
                if self.player.point.get_xy() == [0, 1]:
                    self.labyrinth_class.get_point(self.mouse_in_labyrinth[0], self.mouse_in_labyrinth[1]).switch()
                    self.labyrinth_class.update_border_labyrinth()

    def mouse_un_clicked(self, button):
        if button == 1:
            if self.detect:
                if self.closeButtonState == "clicked":
                    self.run_bool = False
                elif self.hideButtonState == "clicked":
                    pygame.display.iconify()

    def key_clicked(self, key):
        # Time element, will refactor
        # Збільшення масштабу поля
        if key in [1073741911, 61]:
            self.size += 5
            self.init_size_component()

        # Зменшення масштабу поля
        elif key in [1073741910, 45]:
            if self.size > 20:
                self.size -= 5
                self.init_size_component()
            else:
                print("Це мінімальний масштаб")

        # Рух по матричному полю (керування гравця)
        if key == pygame.K_UP:
            self.player.move_up()

        elif key == pygame.K_DOWN:
            self.player.move_down()

        elif key == pygame.K_RIGHT:
            self.player.move_right()

        elif key == pygame.K_LEFT:
            self.player.move_left()

    def run_neural_network(self):
        if self.sleap_network_check != 0:
            self.sleap_network_check -= 1
            return
        self.sleap_network_check = self.sleap_network

        player_move = {1: self.player.move_right,
                       2: self.player.move_down,
                       3: self.player.move_left,
                       4: self.player.move_up}

        get_ans = self.neural_network_class.generate_ans(self.player.point.get_data_point())

        player_move[get_ans]()


    def display_score(self):
        # display score
        score = self.font.render(f"score: {str(self.player.point.score)}", True, self.player.point.color_of_score)
        text_rect = score.get_rect()
        text_rect.center = (self.width / 2, self.height - 55)
        self.screen.blit(score, text_rect)

        # display the best score
        best_score = self.font.render(f"best score: {str(self.player.point.best_score)}", True, BLACK)
        text_rect = best_score.get_rect()
        text_rect.center = (100, self.height - 25)
        self.screen.blit(best_score, text_rect)

        #dispaly count of victory
        victories = self.font.render(f"victories: {str(self.player.point.count_of_victories)}", True, BLACK)
        text_rect = best_score.get_rect()
        text_rect.center = (self.width-100, self.height - 25)
        self.screen.blit(victories, text_rect)

    # <--- Run game --->
    def run(self):
        while self.run_bool:
            # to detect some events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run_bool = False

                # mouse motion
                if event.type == MOUSEMOTION:
                    self.mouse_motion(event.pos)

                # if clicked
                if event.type == MOUSEBUTTONDOWN:
                    self.mouse_clicked(event.button)

                # if un clicked
                elif event.type == MOUSEBUTTONUP:
                    self.mouse_un_clicked(event.button)

                if event.type == pygame.KEYDOWN:
                    self.key_clicked(event.key)

            if self.network_bool:
                self.run_neural_network()
            self.player.point.time+=1
            self.player.is_move()

            # some code here
            self.draw()

            # CIRCLE
            if self.radius_decreasing:
                self.circle_radius -= self.size * 0.3 / 20
                # если радиус достиг 0 или меньше, меняем направление
                if self.circle_radius <= 0:
                    self.radius_decreasing = False

            else:
                self.circle_radius += self.size * 0.3 / 20
                # если радиус достиг максимального значения, меняем направление
                if self.circle_radius >= self.size / 2 - 1:
                    self.radius_decreasing = True

            self.display_score()




            pygame.display.update()
            # fps on screen
            self.clock.tick(60)

        pygame.quit()
