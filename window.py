import pygame
from pygame.locals import *
import createFigure

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

# Создание класса окна
class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Labyrinth")
        self.clock = pygame.time.Clock()
        self.button = createFigure.createButton(800, 500, 50, 20)


    def run(self):
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.button.collidepoint(event.pos):
                        print("click))))")

            self.screen.fill(WHITE)

            # some code here
            # example from createFigure.py
            pygame.draw.rect(self.screen, BLACK, self.button)
            pygame.display.update()
            self.clock.tick(60)


pygame.quit()