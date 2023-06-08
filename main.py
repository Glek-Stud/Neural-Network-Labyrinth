from utils import Utils
from GUI2D import GUI2D
from config import buttons


# < Функція запуску основної програми >
def start_function():
    Utils()
    GUI2D(buttons).run()


# Завершение Pygame

if __name__ == '__main__':
    start_function()
