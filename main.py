from utils import Utils
from GUI2D import GUI2D
from config import BLOCK_SIZE, SCALE


# < Функція запуску основної програми >
def start_function():
    Utils()
    labyrinth_size = "middle"
    match labyrinth_size:
        case "min":
            GUI2D(50, 20).run()
        case "middle":
            GUI2D(SCALE, BLOCK_SIZE).run()
        case "max":
            GUI2D(9, 40).run()


# Завершение Pygame

if __name__ == '__main__':
    start_function()
