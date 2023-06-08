# <Window>
# size of window
FRAME = 5
LABYRINTH_SIZE = 725
BUTTON_HEIGHT_SIZE = 100

WIDTH = LABYRINTH_SIZE + FRAME
HEIGHT = LABYRINTH_SIZE + BUTTON_HEIGHT_SIZE + 25

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)

# size of block
BLOCK_SIZE = 25

# title of window
TITLE = "Labyrinth"

# temporary variable
buttons = [
    {"name": "Кнопка 1", "func": lambda: print(1)},
    {"name": "Кнопка 2", "func": lambda: print(2)},
    {"name": "Кнопка 3", "func": lambda: print(3)},
]
