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
        up_lid[1] = 2
        border_labyrinth.append(up_lid)

        for stage in self.labyrinth:
            copy_stage = stage.copy()
            copy_stage.insert(0, 1)
            copy_stage.append(1)
            border_labyrinth.append(copy_stage)

        down_lid = [1] * (self.scale + 2)
        down_lid[-2] = 3
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
                self.labyrinth[y][x] = random.choice([0, 4])

    def generate_labyrinth(self, x=0, y=0):
        if x == 0 and y == 0:
            for i in range(self.scale):
                for j in range(self.scale):
                    self.labyrinth[i][j] = 4

        self.labyrinth[y][x] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        random.shuffle(directions)

        for dx, dy in directions:
            new_x, new_y = x + 2 * dx, y + 2 * dy

            if 0 <= new_x < self.scale and 0 <= new_y < self.scale and self.labyrinth[new_y][new_x] == 4:
                self.labyrinth[new_y][new_x] = 0
                self.labyrinth[y + dy][x + dx] = 0
                self.generate_labyrinth(new_x, new_y)


class Point:
    def __init__(self, labyrinth_logic: LabyrinthLogic, index_y: int, index_x: int):
        assert 0 <= index_x < labyrinth_logic.scale, "Значення індексу x не вірне"
        assert 0 <= index_y < labyrinth_logic.scale, "Значення індексу y не вірне"
        self.labyrinth_logic = labyrinth_logic
        self.index_x = index_x
        self.index_y = index_y

    def up(self, x,y, labyrinth):
        if labyrinth[y - 1][x] != 4 and labyrinth[y - 1][x] !=1:
            print("UP TRUE")

            return True
        print("UP FALSE")
        return False

    def down(self, x,y, labyrinth):
        if labyrinth[y + 1][x] != 4 and labyrinth[y + 1][x] !=1:

            print("DOWN TRUE")
            return True
        print("DOWN FALSE")
        return False

    def left(self, x,y, labyrinth):
        if labyrinth[y][x-1] != 4 and labyrinth[y][x-1] !=1:
            print("LEFT TRUE")

            return True
        print("LEFT FALSE")
        return False

    def right(self, x,y, labyrinth):
        if labyrinth[y][x+1] != 4 and labyrinth[y][x+1] !=1:
            print("RIGHT TRUE")

            return True
        print("RIGHT FALSE")
        return False

    def turn_on(self):
        self.labyrinth_logic.labyrinth[self.index_y][self.index_x] = 1

    def turn_off(self):
        self.labyrinth_logic.labyrinth[self.index_y][self.index_x] = 0

    def switch(self):
        if self.labyrinth_logic.labyrinth[self.index_y][self.index_x]:
            self.labyrinth_logic.labyrinth[self.index_y][self.index_x] = 0
        else:
            self.labyrinth_logic.labyrinth[self.index_y][self.index_x] = 4

    def get_point(self):
        return self.labyrinth_logic.labyrinth[self.index_y][self.index_x]




if __name__ == '__main__':
    labyrinth_class = LabyrinthLogic(5)
    labyrinth_class.random_matrix()
    point_class = labyrinth_class.get_point()
    # point_class.switch()
    labyrinth_class.show_labyrinth()
