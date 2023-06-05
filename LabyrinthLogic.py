from utils import set_logger
import random


class LabyrinthLogic:

    def __init__(self, scale: int = 5):
        self.logger = set_logger("Labyrinth Logic")
        self.scale = scale
        self.labyrinth = [[0] * scale for _ in range(scale)]

    def get_point(self, index_y: int = 0, index_x: int = 0):
        return Point(self, index_y, index_x)

    def get_border_labyrinth(self):
        border_labyrinth = []
        up_lid = [1] * (self.scale + 2)
        up_lid[1] = 0
        border_labyrinth.append(up_lid)

        for stage in self.labyrinth:
            copy_stage = stage.copy()
            copy_stage.insert(0, 1)
            copy_stage.append(1)
            border_labyrinth.append(copy_stage)

        down_lid = [1] * (self.scale + 2)
        down_lid[-2] = 0
        border_labyrinth.append(down_lid)
        return border_labyrinth

    def show_labyrinth(self):
        for y in self.get_border_labyrinth():
            for x in y:
                if x:
                    print("██", end="")
                else:
                    print("  ", end="")
            print()

    def random_matrix(self):
        for y in range(self.scale):
            for x in range(self.scale):
                self.labyrinth[y][x] = random.randint(0, 1)


class Point:
    def __init__(self, labyrinth_logic: LabyrinthLogic, index_y: int, index_x: int):
        assert 0 <= index_x < labyrinth_logic.scale, "Значення індексу x не вірне"
        assert 0 <= index_y < labyrinth_logic.scale, "Значення індексу y не вірне"
        self.labyrinth_logic = labyrinth_logic
        self.index_x = index_x
        self.index_y = index_y

    def up(self):
        if self.index_y - 1 < 0:
            return False
        self.index_y -= 1
        return True

    def down(self):
        if self.index_y + 1 >= self.labyrinth_logic.scale:
            return False
        self.index_y += 1
        return True

    def left(self):
        if self.index_x - 1 < 0:
            return False
        self.index_x -= 1
        return True

    def right(self):
        if self.index_x + 1 >= self.labyrinth_logic.scale:
            return False
        self.index_x += 1
        return True

    def turn_on(self):
        self.labyrinth_logic.labyrinth[self.index_y][self.index_x] = 1

    def turn_off(self):
        self.labyrinth_logic.labyrinth[self.index_y][self.index_x] = 0

    def switch(self):
        if self.labyrinth_logic.labyrinth[self.index_y][self.index_x]:
            self.labyrinth_logic.labyrinth[self.index_y][self.index_x] = 0
        else:
            self.labyrinth_logic.labyrinth[self.index_y][self.index_x] = 1

    def get_point(self):
        return self.labyrinth_logic.labyrinth[self.index_y][self.index_x]


if __name__ == '__main__':
    labyrinth_class = LabyrinthLogic(25)
    labyrinth_class.random_matrix()
    point_class = labyrinth_class.get_point()
    point_class.down()
    point_class.down()
    point_class.down()
    # point_class.switch()
    labyrinth_class.show_labyrinth()
