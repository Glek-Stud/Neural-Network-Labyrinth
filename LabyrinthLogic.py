from utils import set_logger
import random


class LabyrinthLogic:

    def __init__(self, scale: int = 5):
        self.border_labyrinth = []
        self.logger = set_logger("Labyrinth Logic")
        self.scale = scale
        self.labyrinth = [[0] * scale for _ in range(scale)]

    def get_point(self, y: int = 0, x: int = 1):
        return Point(self, y, x)

    def get_player(self):
        return Player(self.get_point(), self.border_labyrinth)

    def update_border_labyrinth(self):

        self.border_labyrinth.clear()
        up_lid = [1] * (self.scale + 2)
        up_lid[1] = 2
        self.border_labyrinth.append(up_lid)

        for stage in self.labyrinth:
            copy_stage = stage.copy()
            copy_stage.insert(0, 1)
            copy_stage.append(1)
            self.border_labyrinth.append(copy_stage)

        down_lid = [1] * (self.scale + 2)
        down_lid[-2] = 3
        self.border_labyrinth.append(down_lid)


    def show_labyrinth(self):
        self.update_border_labyrinth()
        for y in self.border_labyrinth:
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
    def __init__(self, labyrinth_logic: LabyrinthLogic, y: int, x: int):
        assert 0 <= x < labyrinth_logic.scale, "Значення індексу x не вірне"
        assert 0 <= y < labyrinth_logic.scale, "Значення індексу y не вірне"
        self.labyrinth_logic = labyrinth_logic
        self.x = x
        self.y = y
        self.finish = False
    def up(self):
        if self.labyrinth_logic.border_labyrinth[self.y-1][self.x] == 4 or self.labyrinth_logic.border_labyrinth[self.y - 1][self.x] ==1:
            return False

        self.y -= 1
        return True

    def down(self):
        if self.labyrinth_logic.border_labyrinth[self.y+1][self.x] == 4 or self.labyrinth_logic.border_labyrinth[self.y + 1][self.x] ==1:
            return False
        if self.labyrinth_logic.border_labyrinth[self.y + 1][self.x] == 3:
            self.finish=True
        self.y += 1
        return True

    def left(self):
        if self.labyrinth_logic.border_labyrinth[self.y][self.x-1] == 4 or self.labyrinth_logic.border_labyrinth[self.y][self.x-1] ==1:
            return False
        if self.labyrinth_logic.border_labyrinth[self.y][self.x-1] == 3:
            self.finish=True
        self.x -= 1
        return True

    def right(self):
        if self.labyrinth_logic.border_labyrinth[self.y][self.x+1] == 4 or self.labyrinth_logic.border_labyrinth[self.y][self.x+1] ==1:
            return False
        if self.labyrinth_logic.border_labyrinth[self.y ][self.x+ 1] == 3:
            self.finish=True
        self.x += 1
        return True

    def get_xy(self):
        return [self.y, self.x]

    def turn_on(self):
        self.labyrinth_logic.labyrinth[self.y][self.x] = 1

    def turn_off(self):
        self.labyrinth_logic.labyrinth[self.y][self.x] = 0

    def switch(self):
        if self.labyrinth_logic.labyrinth[self.y][self.x]:
            self.labyrinth_logic.labyrinth[self.y][self.x] = 0
        else:
            self.labyrinth_logic.labyrinth[self.y][self.x] = 4

    def get_point(self):
        return self.labyrinth_logic.labyrinth[self.y][self.x]


class Player:
    def __init__(self, point, labyrinth):
        self.point = point
        self.labyrinth = labyrinth
    def moveUp(self):
        if self.point.up():
            if self.labyrinth[self.point.y][self.point.x] == 9:

                self.labyrinth[self.point.y+1][self.point.x] = 0
            else:
                self.labyrinth[self.point.y+1][self.point.x] = 9
            self.labyrinth[self.point.y][self.point.x] = 2


    def moveDown(self):

        if self.point.down():

            if self.labyrinth[self.point.y][self.point.x] == 9:
                self.labyrinth[self.point.y-1][self.point.x] = 0
            else:
                self.labyrinth[self.point.y-1][self.point.x] = 9

            self.labyrinth[self.point.y][self.point.x] = 2


    def moveRight(self):
        if self.point.right():
            if self.labyrinth[self.point.y][self.point.x] == 9:
                self.labyrinth[self.point.y][self.point.x-1] = 0
            else:
                self.labyrinth[self.point.y][self.point.x-1] = 9
            self.labyrinth[self.point.y][self.point.x] = 2


    def moveLeft(self):
        if self.point.left():
            if self.labyrinth[self.point.y][self.point.x] == 9:
                self.labyrinth[self.point.y][self.point.x+1] = 0
            else:
                self.labyrinth[self.point.y][self.point.x+1] = 9
            self.labyrinth[self.point.y][self.point.x] = 2


if __name__ == '__main__':
    labyrinth_class = LabyrinthLogic(5)
    labyrinth_class.random_matrix()
    point_class = labyrinth_class.get_point()
    # point_class.switch()
    labyrinth_class.show_labyrinth()
