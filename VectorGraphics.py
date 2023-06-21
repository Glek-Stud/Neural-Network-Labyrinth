from pygame.draw import rect, circle
from pygame import Surface, SRCALPHA
from config import BLACK
from pygame import transform

class VectorGraphics:
    def __init__(self, size, circle_radius):
        self.surfaces = {
            0: self.surface0_road(size),
            1: self.surface1_break_wall(size),
            2: self.surface2_wall(size),
            3: self.surface3_start(size, circle_radius),
            4: self.surface4_finish(size, circle_radius),
            5: self.surface5_trace(size),
            6: self.surface6_trace2(size),
            7: self.surface7_player(size),
            8: self.surface8_player(size)
        }

    @staticmethod
    def surface0_road(size):
        surface = Surface((size, size))
        rect(surface, (107, 132, 175), (0, 0, size, size))
        rect(surface, (126, 163, 191), (0, 0, size * 7 // 20, size * 14 // 20), size // 20)
        rect(surface, (126, 163, 191), (size * 6 // 20, 0, size * 14 // 20, size * 7 // 20), size // 20)
        rect(surface, (126, 163, 191), (size * 6 // 20, size * 6 // 20, size * 14 // 20, size * 8 // 20),
             size // 20)
        rect(surface, (126, 163, 191), (0, size * 13 // 20, size * 13 // 20, size * 8 // 20), size // 20)
        return surface

    @staticmethod
    def surface1_break_wall(size):
        surface = Surface((size, size))
        rect(surface, (44, 35, 59), (0, 0, size, size), size // 10)
        rect(surface, (226, 180, 126), (size // 10, size // 10, size * 16 // 20, size * 8 // 20))
        rect(surface, (218, 148, 109), (size // 10, size * 8 // 20, size * 16 // 20, size * 4 // 20))
        rect(surface, (196, 113, 95), (size // 10, size * 11 // 20, size * 16 // 20, size * 4 // 20))
        rect(surface, (161, 82, 88), (size // 10, size * 14 // 20, size * 16 // 20, size * 4 // 20))
        return surface

    @staticmethod
    def surface2_wall(size):
        surface = Surface((size, size))
        rect(surface, (44, 35, 59), (0, 0, size, size), size // 10)
        rect(surface, (69, 62, 73), (size // 10, size // 10, size * 16 // 20, size * 6 // 20))
        rect(surface, (77, 76, 131), (size // 10, size * 7 // 20, size * 16 // 20, size * 7 // 20))
        rect(surface, (107, 132, 175), (size // 10, size * 13 // 20, size * 16 // 20, size * 5 // 20))
        return surface

    def surface3_start(self, size, circle_radius):
        surface = self.surface0_road(size)
        circle(surface, (14, 245, 73), (size // 2, size // 2), circle_radius)
        return surface

    def surface4_finish(self, size, circle_radius):
        surface = self.surface0_road(size)
        circle(surface, (245, 28, 12), (size // 2, size // 2), circle_radius)
        return surface

    @staticmethod
    def surface5_trace(size):
        dark_green = (36, 168, 69)
        green = (43, 214, 88)
        surface = Surface((size, size))
        rect(surface, dark_green, (0, 0, size, size))
        rect(surface, green, (0, 0, size * 7 // 20, size * 14 // 20), size // 20)
        rect(surface, green, (size * 6 // 20, 0, size * 14 // 20, size * 7 // 20), size // 20)
        rect(surface, green, (size * 6 // 20, size * 6 // 20, size * 14 // 20, size * 8 // 20), size // 20)
        rect(surface, green, (0, size * 13 // 20, size * 13 // 20, size * 8 // 20), size // 20)
        return surface

    @staticmethod
    def surface6_trace2(size):
        d_red = (179, 51, 51)
        red = (212, 60, 60)
        surface = Surface((size, size))
        rect(surface, d_red, (0, 0, size, size))
        rect(surface, red, (0, 0, size * 7 // 20, size * 14 // 20), size // 20)
        rect(surface, red, (size * 6 // 20, 0, size * 14 // 20, size * 7 // 20),
             size // 20)
        rect(surface, red,
             (size * 6 // 20, size * 6 // 20, size * 14 // 20, size * 8 // 20),
             size // 20)
        rect(surface, red, (0, size * 13 // 20, size * 13 // 20, size * 8 // 20),
             size // 20)
        return surface



    def surface7_player(self, size):
        surface_main = self.surface0_road(size)

        red = (212, 15, 28)
        l_red = (237, 28, 35)
        blue = (153, 217, 234)
        d_blue = (0, 183, 239)

        surface = Surface((size, size), SRCALPHA)

        one = size // 20
        # backpack
        rect(surface, BLACK, (one * 2, one * 4, one * 4, one * 12))
        rect(surface, l_red, (one * 3, one * 5, one * 3, one * 10))
        rect(surface, red, (one * 3, one * 5, one * 1, one * 6))

        # head
        rect(surface, BLACK, (one * 6, one * 0, one * 12, one * 6))
        rect(surface, l_red, (one * 7, one * 1, one * 10, one * 5))
        rect(surface, red, (one * 7, one * 1, one * 1, one * 3))
        rect(surface, BLACK, (one * 9, one * 2, one * 8, one * 4))
        rect(surface, d_blue, (one * 10, one * 3, one * 7, one * 3))
        rect(surface, blue, (one * 11, one * 3, one * 6, one * 2))

        # body
        rect(surface, BLACK, (one * 6, one * 6, one * 12, one * 10))
        rect(surface, l_red, (one * 7, one * 7, one * 10, one * 8))
        rect(surface, red, (one * 9, one * 11, one * 8, one * 4))

        # leg1
        rect(surface, BLACK, (one * 6, one * 16, one * 5, one * 4))
        rect(surface, red, (one * 7, one * 16, one * 3, one * 3))
        # leg2
        rect(surface, BLACK, (one * 13, one * 16, one * 5, one * 4))
        rect(surface, red, (one * 14, one * 16, one * 3, one * 3))

        surface_main.blit(surface, (int(size % 20 / 2), int(size % 20 / 2)))
        return surface_main

    def surface8_player(self, size):
        surface_main = self.surface7_player(size)

        flipped_surface = transform.flip(surface_main, True, False)  # Отражение по вертикали

        surface_main.blit(flipped_surface, (int(size % 20 / 2), int(size % 20 / 2)))
        return surface_main

    @staticmethod
    def surface9_button(self, size, button_width):
        surface = Surface((size, size))
        border_radius = 20

        return surface
