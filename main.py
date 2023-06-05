from utils import Utils
from GUI2D import GUI2D
from window import Window

# < Функція запуску основної програми >
def start_function():
    Utils()
    GUI2D()


window = Window()
window.run()

# Завершение Pygame

if __name__ == '__main__':
    start_function()
