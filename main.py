from GUI2D import GUI2D
from config import BLOCK_SIZE, SCALE


# <--- Функція запуску основної програми --->
def start_function():
    labyrinth_size = "middle"
    match labyrinth_size:
        case "min":
            GUI2D(49, 20).run()
        case "middle":
            GUI2D(SCALE, BLOCK_SIZE).run()
        case "max":
            GUI2D(9, 40).run()


if __name__ == '__main__':
    start_function()
