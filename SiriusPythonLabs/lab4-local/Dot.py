# Created by Hannah at 06.10.2023 9:24
import math


class Dot:
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except TypeError:
            print("So sorry, but point used to have numeric coordinates")

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        else:
            if self.y < other.y:
                return True
            else:
                return False

    def dot_dist_kv(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def print_it(self):
        print("x = {}, y = {}".format(self.x, self.y))

    def get_two_okr(self, other, r):
        c = Dot((self.x + other.x)/2, (self.y + other.y)/2)
        half_hord_kv = self.dot_dist_kv(c)
        part_of_r = math.sqrt(r ** 2 - half_hord_kv)
        if self.y != other.y:
            normal_x = self.y - other.y
        else:
            normal_x = 0
        if self.x != other.x:
            normal_y = other.x - self.x
        else:
            normal_y = 0
        len_normal = math.sqrt(normal_y**2+normal_x**2)
        if len_normal != 0:
            normal_x = normal_x * part_of_r / len_normal
            normal_y = normal_y * part_of_r / len_normal
        return c.x + normal_x, c.y + normal_y, c.x - normal_x, c.y - normal_y
