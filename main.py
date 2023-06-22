from GUI2D import GUI2D
from config import BLOCK_SIZE, SCALE


# <--- Функція запуску основної програми --->
def start_function():
    labyrinth_size = "min"
    match labyrinth_size:
        case "min":
            GUI2D(39, 20).run()
        case "middle":
            GUI2D(SCALE, BLOCK_SIZE).run()


if __name__ == '__main__':
    start_function()
